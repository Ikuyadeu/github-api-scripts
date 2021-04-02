rethinkdb-download
==================

This repository contains some scripts to manage download.rethinkdb.com, currently hosted on DigitalOcean.

Files are managed by `git-annex`, which means that git stores only broken symlinks to the files.
Run `git annex get <path>` to download a file.

## Contents

* `version/` contains a list of files for each version of RethinkDB
* `download.rethinkdb.com/` is a mirror of http://download.rethinkdb.com
* `apt-repo/` contains scripts and a package cache to generate `download.rethinkdb.com/apt/`
* `nginx.conf` contains the nginx config for download.rethinkdb.com

## Actions

* `apt-repo/add-version <version>` - adds the packages from `version/<version>/deb/` to a cache in `apt-repo/lib`
* `apt-repo/build-repo` - build the apt repo in `download.rethinkdb.com/apt`
* `apt-repo/freight` - a git submodule: the freight scripts are used by `add-version` and `build-repo`
* `rake update-nginx` - upload the nginx config to the server
* `rake publish` - pretend to publish the files to download.rethinkdb.com using `rsync --dry-run`
* `rake publish[force]` - actually publish the files.
* `vim downloads.rethinkdb.com/latest_version.txt` - for the new update checker when making a new release

## Release instructions

### Prerequisites

You will need to make sure that the following requirements are met.

* You have at least 20GB+ free space on your disk
* The `git`, `git-annex`, `ruby`, `rake` and `createrepo` packages are install
* You have the signing keys in your keychain
* You have access to the git annex server
* You have access to the download server running on DigitalOcean
* You have all the necessary package versions

Please assign at least 2 hours for the release to make sure everything goes well and you did not forget any steps. Also, some steps will take long, so run every command in `screen` to make sure that if the connection lost, you not messed up anything.

### Steps

First of all, clone the github repository and add the git-annex remote created by Sam.

```bash
$ git clone git@github.com:rethinkdb/rethinkdb-download.git
$ cd rethinkdb-download
$ git remote add srh-annex git@<IP_ADDRESS>:rethinkdb-download.git
$ git fetch srh-annex
```

_Note: <IP_ADDRESS> is intentionally not replaced by a real IP._

Next, sync the changes, check the HEAD and sync the content.

```bash
# Ignore complaints about origin not having git-annex installed
$ git annex sync srh-annex --no-push

# HEAD -> master, srh-annex/synced/master, srh-annex/master, origin/synced/master, synced/master, etc
$ git log -1

# This takes a long time - downloads more that 15GB of data
$ git annex sync srh-annex --no-push --content

# get the apt-repo/freight submodule
$ git submodule update --init --recursive
```

Now you need to copy the already built packages to their place. Follow the pattern of the `2.3.6`, `2.3.7` and `2.4.0` directories, so debian **and** ubuntu packages goes to `version/<DB_VERSION>/deb/`, CentOS packages to `version/2.3.7/centos{6,7,8}` and so on. Do not forget the OSX, dist and - if you built - windows packages.

When you are done with all the steps above, you are ready to add version/... to the git-annex remote. To do this, you will need to run `git annex add <path>` where path is the file you copied over. **You need to run `git annex add` not `git add`**.

After adding the mentioned files, it is recommended to commit the changes before running the apt-repo scripts.

At this point, all the packages should be at their dedicated place. The next step is to add a new version to the apt repo, build it and copy over all the other distributions.

```bash
# add a new version to the apt repo and build it
$ VERSION=<DB_VERSION> rake apt

# copy all the other distributions
$ VERSION=<DB_VERSION> rake copy
```

Since the above commands are calling several git commands, please check your git log before going further. If you made sure that no strange things happened, only few steps left.

You will need to update the references for the latest version in `nginx.conf`. Replace `<DB_VERSION>` with the appropriate version number used during the process 

```
rewrite ^/dist/rethinkdb-latest.tgz /dist/rethinkdb-<DB_VERSION>.tgz redirect;
rewrite ^/osx/rethinkdb-latest.dmg /osx/rethinkdb-<DB_VERSION>.dmg redirect;
```

When you are done with the modifications update the nginx configuration on the download server and upload the 

```bash
# Check that the publish command works
$ rake publish

# Publish the config changes
$ rake publish[force]
```

The last step is to make sure your changes applied, check that the new DB version can be downloaded, commit your changes, push to the repository. After all these steps are done, it is possible to update the [Dockerfiles](https://github.com/rethinkdb/rethinkdb-dockerfiles), [DigitalOcean image](https://github.com/rethinkdb/rethinkdb-digitalocean) and the [website config](https://github.com/rethinkdb/www/blob/master/_config.yml#L13).
