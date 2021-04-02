# Swift Package Manager Project

The Swift Package Manager is a tool for managing distribution of source code, aimed at making it easy to share your code and reuse others’ code. The tool directly addresses the challenges of compiling and linking Swift packages, managing dependencies, versioning, and supporting flexible distribution and collaboration models.

We’ve designed the system to make it easy to share packages on services like GitHub, but packages are also great for private personal development, sharing code within a team, or at any other granularity.

Swift Package Manager includes a build system that can build for macOS and Linux. Starting with Xcode 11, Xcode integrates with libSwiftPM to provide support for iOS, watchOS, and tvOS platforms.

The [SourceKit-LSP](https://github.com/apple/sourcekit-lsp) project leverages libSwiftPM and provides [Language Server Protocol](https://langserver.org/) implementation for editors that support LSP.

---

## Table of Contents
* [Getting Started](#getting-started)
* [Documentation](#documentation)
* [System Requirements](#system-requirements)
* [Installation](#installation)
  * [Managing Swift Environments](#managing-swift-environments)
  * [Choosing a Swift Version](#choosing-a-swift-version)
* [Support](#support)
* [Contributions](#contributions)
* [License](#license)

---

## Getting Started

Please use [this guide](https://swift.org/getting-started/#using-the-package-manager) for learning package manager basics.

---

## Documentation

For Quick Help use the ```swift package --help ``` command.

For extensive documentation on using Swift Package Manager, creating packages, and more, see [Documentation](Documentation).

For additional documentation on developing the Swift Package Manager itself, see [Documentation/Contributing](Documentation/Contributing.md).

For detailed documentation on the package manifest API, see [PackageDescription API](https://docs.swift.org/package-manager/PackageDescription/index.html).

For release notes with information about changes between versions, see [Release Notes](Documentation/ReleaseNotes).

---

## System Requirements

The package manager’s system requirements are the same as [those for Swift](https://github.com/apple/swift#system-requirements) with the caveat that the package manager requires Git at runtime as well as build-time.

---

## Installation

The Swift Package Manager is included in Xcode 8.0 and all subsequent releases.

The package manager is also available for other platforms as part of all [Snapshots available at swift.org](https://swift.org/download/), including snapshots for the latest versions built from `master`. For installation instructions for downloaded snapshots, please see the [Getting Started](https://swift.org/getting-started/#installing-swift) section of [swift.org](https://swift.org).

You can verify your installation by typing `swift package --version` in a terminal:

```sh
$ swift package --version
Apple Swift Package Manager - ...
```

### Managing Swift Environments

On macOS `/usr/bin/swift` is just a stub that forwards invocations to the active
toolchain. Thus when you call `swift build` it will use the swift defined by
your `TOOLCHAINS` environment variable. This can be used to easily switch
between the default tools, and a development snapshot:

```sh
$ xcrun --find swift
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/swift
$ swift --version
Apple Swift version 3.0
$ export TOOLCHAINS=swift
$ xcrun --find swift
/Library/Developer/Toolchains/swift-latest.xctoolchain/usr/bin/swift
$ swift --version
Swift version 3.0-dev
```

To use a specific toolchain you can set `TOOLCHAINS` to the `CFBundleIdentifier` in an `.xctoolchain`’s Info.plist.

### Choosing a Swift Version

The `SWIFT_EXEC` environment variable specifies the `swiftc` executable path used by `swift package`. If it is not set, the package manager will try to locate it:

1. In `swift-package`'s parent directory.
2. On macOS, by calling `xcrun --find swiftc`.
3. By searching the PATH.


---

## Support

If you have any trouble with the package manager, help is available. We recommend:

* The [Swift Forums](https://forums.swift.org/c/swift-users)
* Our [bug tracker](http://bugs.swift.org)

When adding a bug to the tracker you should follow the bug reporting guidelines, they can be found in [Resources.md](./Documentation/Resources.md#reporting-a-good-swiftpm-bug).

If you’re not comfortable sharing your question with the list, contact details for the code owners can be found in [CODEOWNERS](CODEOWNERS); however, the mailing list is usually the best place to go for help.

---

## Contributions

There are several ways to contribute to Swift Package Manager. To learn about the policies, best practices that govern contributions to the Swift project and instructions for setting up the development environment please read the [Contributor Guide](Documentation/Contributing.md).  

The Swift package manager uses [llbuild](https://github.com/apple/swift-llbuild) as the underlying build system for compiling source files. It is also open source and part of the Swift project.

---

## License

Copyright 2015 - 2020 Apple Inc. and the Swift project authors. Licensed under Apache License v2.0 with Runtime Library Exception.

See [https://swift.org/LICENSE.txt](https://swift.org/LICENSE.txt) for license information.

See [https://swift.org/CONTRIBUTORS.txt](https://swift.org/CONTRIBUTORS.txt) for Swift project authors.
