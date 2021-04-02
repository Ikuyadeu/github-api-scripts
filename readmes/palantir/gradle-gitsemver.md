# Gitsemver plugin for gradle [![Build Status](https://travis-ci.org/palantir/gradle-gitsemver.svg?branch=master)](https://travis-ci.org/palantir/gradle-gitsemver) [![Download](https://api.bintray.com/packages/palantir/releases/gradle-gitsemver/images/download.svg) ](https://bintray.com/palantir/releases/gradle-gitsemver/_latestVersion)

## Why?

To create an alternative to using `git describe` for automatic versioning that works nicely with git flow and automatically updates project versions.

## How does it work?

1. Finds all tags of format v?\d+\.\d+\.\d+ accessible from HEAD
2. Uses a slightly modified semantic versioning scheme to sort tags
3. Chooses the 'largest' tag
4. If the tag is not at HEAD, it appends to the version:
   * the number of commits since that tag
   * the git hash in the format g01ABCDEF
   * the dirty state of the repo
4. If the tag is at HEAD, then nothing is appended

### Example:

Suppose we have a git history that looks like this (newest on top):

```
* eeeeeee - (HEAD, develop) fix a bug <EA>
* ddddddd - merge 'feature/stuff' into 'develop' <EA>
|\
| * ccccccc - (feature/stuff) my feature is done <EA>
* | bbbbbbb - (tag: v0.1.0-dev) preparing develop branch <EA>
|/
* aaaaaaa - (master, tag: v0.0.0) Initial commit <EA>
```

For each ref that I could checkout, the version would be:

* `master`: v0.0.0
* `bbbbbb`: v0.1.0-dev
* `feature/stuff`: v0.0.0-1-gccccccc
* `ddddddd`: v0.1.0-dev-2-gddddddd
* `eeeeeee`: v0.1.0-dev-3-geeeeeee

Finally, if I were on the develop branch and had uncommitted changes the version would be v0.1.0-dev+3.geeeeeee.dirty

### Can you explain your modified semver sort?

Sure. Standard semantic versioning sorts words alphabetically. This is not wanted if you're going to be creating tags like `v0.1.0-dev` and `v0.1.0-alpha`. You want to alpha sort everything except 'dev', 'alpha', 'beta', and 'rc', where those are ordered and always bigger than any other word. Thats it.

## Adding to your build

```gradle
buildscript {
  repositories {
    mavenCentral()
    maven {
      url "http://dl.bintray.com/palantir/releases"
    }
  }
  dependencies {
    classpath 'com.palantir:gradle-gitsemver:0.6.0'
  }
}

apply plugin: 'gitsemver'
version semverVersion()
```

Now verify that the version is being applied:

```console
$ gradle properties | grep version
version: v0.0.0-58-g5f78071.dirty
```

## Prefix tags

Gitsemver supports a special mode of operation where it looks for tags with a given prefix. This can be done using the `semverVersionPrefix("prefix")` convention:

```gradle
apply plugin: 'gitsemver'
version semverVersionPrefix("projecta")
```

This will look for all tags with form `projecta-v1.2.3` and ignore everything else. If there are no tags of this form in the repo, it will error out.

This is useful in cases in which multiple subprojects need to be independently versioned.

## Topological Semver

It's also possible to have the tags sorted by how far from HEAD they are. To use the topological sorting, copy this into your build file:

```gradle
apply plugin: 'gitsemver'
version semverVersionTopo()
```

Topological sorting will then find the closest tag to HEAD, and use that tag as the base for the version.  It will strip off the prefix.

## Topological Prefixed Semver

It's possible to combine the prefix and topological methods.  This will work just like topological semver except will choose the closest one with the prefix.

```gradle
apply plugin: 'gitsemver'
version semverVersionTopoPrefix('myprefixed')
```

## Version Object

The plugin's version methods return a ``SemverVersion`` object and not a ``String``.  It can be used as a parameter for Gradle's `version`.  Making this an object allows for pulling out pieces of the version string for other uses (if desired).

```java
class SemverVersion {
  String toString()  // The full version string
  String tagName // The matched tag
  String gitHash // The git commit hash of the HEAD commit
  Integer commitCountFromTag // The number of commits HEAD is from the matched tag
  Integer buildNumber // The value of the BUILD_NUMBER environment variable
  boolean dirty // Is the git repo dirty?
}
```
