[![Build Status](https://travis-ci.org/IBM/node-nano-doc-updater.svg?branch=master)](https://travis-ci.org/IBM/node-nano-doc-updater)

# IBM Cloud DevOps Services - node-nano-doc-updater

[Click here](https://cloud.ibm.com/devops) for more information on IBM Cloud DevOps Services.

This is one of hundreds of [IBM Open Source projects at GitHub](http://ibm.github.io).

## Synopsis

```
var db = require("nano")("http://db").db.use("db");
var updater = require("node-nano-doc-updater");

// Migrates a design document.  Will only perform an *upgrade* 
// of an existing design document with a lower version.
//
updater
.db(db)
.existingDoc(null)
.newDoc({ language: "javascript", version: 1 })
.id("_design/foo")
.shouldUpdate((existing, newVer) => {
	return !existing.version || existing.version < newVer.version;
})
.merge((existing, newVer) => {
	return newVer; 
})
.update((err) => { /* handle errors */  });
```

## Description

A module designed to allow updates of CouchDB documents with configurable conflict resolution.

Because of the way CouchbDB handles concurrency, updating a document is non-trivial.  Instead of asking CouchDB to kindly serialize the updates, the process involves determining the current revision of a document and submitting a request to update that particular revision.  In the event other updates have occurred during this process, the request is rejected.

This module emits an object that can perform this tedious and error-prone flow.  Using it involves priming it with information and then asking it to perform one or more updates.

## Creation

### nanoDocUpdater()

Returns a Nano Doc Updater object.  This object holds the parameters of a particular update and can be reused or stored for a later update.

## Setters

The following methods set parameters of an update

### updater.db(db)

Specifies the database to use for the update.  This should be result of [`nano.db.use()`](https://github.com/dscape/nano#nanodbusename) and is required.

### updater.newDoc(doc)

The document to attempt to insert.  This field is required.

### updater&#046;id(id)

The `_id` of the doc to be updated.  This field is required.

### updater.shouldCreate(boolean)

If `true` ensures that during an `updater.update()`, the `newDoc` is inserted even if it doesn't already exist in the DB.  If not specified, `true` is assumed.

### updater.shouldUpdate((publishedDoc, newDoc) => { ... })

Defines a function that is called to determine whether a document should be updated where one already exists in the DB.  This function is given both the `newDoc` and already published documents and should return a boolean indicating wheter an update should be attempted.  Skipping an update in this way results in `updater.update()` ending without error.

If not specified, an update will always be attempted.

### updater.merge((publishedDoc, newDoc) => { ... })

Defines a function that is used to produce a new document, given an existing document and `newDoc`.  Note that `updater` will overwrite the `_rev` field of the resulting document with the revision of the already published document.  Also note that if this function returns an `Error`, no insert will occur.  Instead, `update.update()` will fail with the returned value.  This can be useful for bubbling unrecoverable merge conflicts.  

If not specified, no sophisticated merging will be attempted and `newDoc` will be used, as is.

## Actions

### updater.update((err) => {})

Performs the update and calls the provided callback.

### updater.updateJob()

Returns a function that can be used to perform an update at a later time.  This function will behave exactly like `updater.update()`, however the parameters for the update are immutable and independent of the `updater` object.

## Examples

Loading the module and binding it to to a database handle:

```
var updater = require("nano-doc-updater");
var db = require("nano")("https://mydatabase.com").use("mydatabase");
updater.db(db);
...
...
```

Updating a design document:

```
var designDocument = {
    language: "javascript",
    version: 1
};

updater
.newDoc(designDocument)
.id("_design/foo")
.shouldUpdate(function (existing, newVer) {
	/* Only publish a new document when it's below the version
	   required by this app */
	return !existing.version || existing.version < newVer.version;
})
.merge(function (existing, newDoc) {
	return newDoc; 
	/* To ensure this process will eventually terminate, 
	   nano-doc-updater will copy `_rev` from the 
       existing document to the newDoc one, just before
       publishing it to CouchDB. */
})
.update(function (err) {
    // handle errors
});
```

Performing another update with the same updater:

```
var newerDesignDocument = {
    language: "javascript",
    version: 2,
    views: {
        count: {
            map: function (d) {
                emit(null, 1);
            },
            reduce: function (k, v, r) {
                sum(v);
            }
        }
    }
};

/*
 * shouldUpdate() is unchanged, so updates will still only
 * occur if the published version is below 2.
 */
updater
.newDoc(newerDesignDocument)
.update((err) => {
    // handle errors
})
;
```

Publish that design document to another document, `foo`:

```
updater
.id("foo")
.shouldUpdate(null) // always update
.merge(null) // overwrite
.update((err) => {
    // handle errors
});
```

Delete that new document:

```
updater
.merge((existing) => {
    existing._deleted = true;
    return existing;
})
.update((err) => {
    // handle errors
});
```

Delete that design document from way back:

```
updater.id("_design/foo").update((err) => {
    // handle errors
});
```

Use `async` to sequence the flow above:

```
var async = require("async");

async.series([
    // Add a design document.  Only publish this if the in-db version is
    // lower.
    updater.db(db).id("_design/foo").newDoc({
        language: "javascript",
        version: 1
    })
    .shouldUpdate((existing, newDoc) => {
        return !existing.version || existing.version < newDoc.version;
    })
    .updateJob(),
    
    
    // Update the design document with an even newer version,
    // but, again, only if it's out of date.
    updater.db(db).id("_design/foo").newDoc({
		language: "javascript",
		version: 2,
		views: {
			count: {
				map: function (d) {
					emit(null, 1);
				},
				reduce: function (k, v, r) {
					sum(v);
				}
			}
		}
    })
    .updateJob(),
    
    
    // Place that same document somewhere else in the db:
    updater.shouldUpdate(null).merge(null).id("foo").updateJob(),
    
    // Delete that document:
    updater
    .merge((existing) => {
      existing._deleted = true;
      return existing;
    })
    .updateJob(),
    
    // Delete the design document:
    updater
    .id("_design/foo")
    .updateJob()
], (err) => {
    if (err) {
        // handle errors in any of the above.
    }
    console.log("All done");
});
```

## License

[The MIT License (MIT)](LICENSE.txt)

## Contributing

Contributions are welcome via Pull Requests. Please submit your very first Pull Request against the [Developer's Certificate of Origin](DCO.txt), adding a line like the following to the end of the file... using your name and email address of course!

```
Signed-off-by: John Doe <john.doe@example.org>
```
