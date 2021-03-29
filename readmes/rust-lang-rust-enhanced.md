# Rust Enhanced

## About

This is a Sublime Text 3 package which supports Rust starting with version 1.0,
it makes no attempt at supporting earlier incompatible versions.

This package used to be called 'Rust', but as of version 3, Sublime now comes with Rust built-in.  The built-in version on Sublime is actually just a snapshot of this package [with some fixes](https://github.com/sublimehq/Packages/issues/178#issuecomment-197050427) from quite some time ago.
This package is still active and will continue to update and release, so if you want up to date features, and extra tools (such as syntax checking or building) we recommend using this package. Installing Rust Enhanced will automatically disable the built-in "Rust" package. If you receive any error, verify that "Rust Enhanced" is enabled, and that the current view's syntax is set to "Rust Enhanced".
There is currently no plan to push upstream changes back into the Sublime Core Packages repo, and extra features will stay here.

For syntax highlighting for Cargo files. Its recommended installing this with the TOML package.

<img src="docs/img/running_tests.gif?raw=true" alt="Running Tests with Rust Enhanced" width=430 style="margin-right:10px"> <img src="docs/img/showing_errors.gif?raw=true" alt="Highlighting errors and warnings with Rust Enhanced" width=430>

## Installation

Install the Package Control package if you haven't got it yet. Package
Control is the best way to install packages for Sublime Text. See
http://wbond.net/sublime_packages/package_control/installation for
instructions.

Open the palette (`control+shift+P` or `command+shift+P`) in Sublime Text
and select `Package Control: Install Package` and then select `Rust Enhanced` from
the list. That's it.
If you can't see `Rust Enhanced` its most likely because you're using Sublime Text 2.

## Features
### Go To Definition
### Cargo Build
Rust Enhanced has a custom build system tailored for running Cargo.  It will display errors and warnings in line using Sublime's phantoms (see [Messages](docs/messages.md) for settings to control how messages are displayed).  It also supports a variety of configuration options to control how Cargo is run.

![testingrust](https://cloud.githubusercontent.com/assets/43198/22944409/7780ab9a-f2a5-11e6-87ea-0e253d6c40f6.png)

See [the build docs](docs/build.md) for more information.

### Cargo tests with highlighting
Thanks to [urschrei](https://github.com/urschrei/)  we have Highlighting for:
- passed test
- failed test
- failed test source line (clickable)
- total number of passed tests
- total number of failed tests > 0
- total number of ignored tests > 0
- total number of measured tests > 0

Example:

![highlight_rust_test](https://cloud.githubusercontent.com/assets/936006/19247437/3cf6e056-8f23-11e6-9bbe-d8c542287db6.png)

### Syntax Checking
Rust Enhanced will automatically perform syntax checking each time you save a file.
Errors and warnings are displayed in line the same way as the [build system](docs/build.md).
This relies on Cargo and Rust (>= 1.8.0) being installed and on your system path. Plus Sublime Text >= 3118.

[Settings](#settings) for controlling the on-save syntax checking:

| Setting | Default | Description |
| :------ | :------ | :---------- |
| `rust_syntax_checking` | `true` | Enable the on-save syntax checking. |
| `rust_syntax_checking_method` | `"check"` | The method used for checking your code (see below). |
| `rust_syntax_checking_include_tests` | `true` | Enable checking of test code within `#[cfg(test)]` sections. |
| `rust_syntax_hide_warnings` | `false` | Don't show warnings when syntax checking |

The available checking methods are:

| Method | Description |
| :----- | :---------- |
| `check` | Uses `cargo check` (requires at least Rust 1.16). |
| `clippy` | Uses `cargo clippy`.  This requires [Clippy](https://github.com/Manishearth/rust-clippy) to be installed.  This also may be a little slower since it must check every target in your package. |

This will use the same configuration options as the "Check" and "Clippy" build variants (for example, extra environment variables, or checking with different features).  See [the build docs](docs/build.md) for more information.

Projects with multiple build targets are supported too (--lib, --bin, --example, etc.). If a cargo project has several build targets, it will attempt to automatically detect the correct target.  In some rare cases, you may need to manually specify which target a file belongs to.  This can be done by adding a "projects" setting in `Rust.sublime-settings` with the following format:

```
    "projects": {
       // One entry per project. Keys are project names.
       "my_cool_stuff": {
           // Path to the project root dir without trailing /src.
           "root": "/path/to/my/cool/stuff/project",

           // Targets will be used to replace {target} part in the command.
           // If no one target matches an, empty string will be used.
           "targets": {
               "bin/foo.rs": "--bin foo",  // format is "source_code_filename -> target_name"
               "bin/bar.rs": "--bin bar",
               "_default": "--lib"         // or "--bin main"
           }
       }
   }
```

## Language Servers

Language servers can provide Rust-specific diagnostics, helpers, and navigation. There are two language server implementations for Rust:

* [RLS (Rust Language Server)](https://github.com/rust-lang/rls)
* [rust-analyzer](https://rust-analyzer.github.io/)

RLS is being replaced by rust-analyzer, but may provide better support at this time depending on your needs.

To use one of the language servers, you need to install the [Sublime LSP](https://github.com/sublimelsp/LSP) plugin. With both the plugin and one of the above servers installed, you should be able to follow the [LSP docs](https://lsp.readthedocs.io/en/latest/) for how to configure the server. Generally this involves running either the `LSP: Enable Language Server Globally` or `LSP: Enable Language Server in Project` and then selecting either `rls` or `rust-analyzer`. Depending on the size of your project, it may take some time for it to process and index.

Note that as well as error checking, code-completion, and renaming, RLS can run [`rustfmt`](https://github.com/rust-lang/rustfmt) on your code: right-click, and select `LSP > Format Document` or `Format Selection` in a Rust source file.

## Context Menu
The Sublime context menu includes a Rust entry with a variety of commands.
See [context menu docs](docs/context.md) for more information.

## Settings
To customize the settings, use the command from the Sublime menu:

    Preferences > Package Settings > Rust Enhanced > Settings - User

Additionally, you can customize settings per-project by adding settings to your `.sublime-project` file under the `"settings"` key.

## Development
Development is quite simple, just check out this project to your Sublime Text 3 packages folder, and switch to using this one.
Syntax definitions are defined in the `RustEnhanced.sublime-syntax` file.

## Credits

Created 2012 by [Daniel Patterson](mailto:dbp@riseup.net), as a near complete from
scratch rewrite of a package by [Felix Martini](https://github.com/fmartini).

This project is currently maintained by [Jason Williams](https://github.com/jayflux)

## License

This package is licensed under the MIT License.
