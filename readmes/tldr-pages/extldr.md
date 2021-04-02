# ExTldr

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/83d63c07f9ca45af9fac591a2c51e8e6)](https://www.codacy.com/gh/tldr-pages/extldr)
[![Coverage Status](https://coveralls.io/repos/github/tldr-pages/extldr/badge.svg?branch=master)](https://coveralls.io/github/tldr-pages/extldr?branch=master)
[![Build Status](https://img.shields.io/github/workflow/status/tldr-pages/extldr/CI.svg)](https://github.com/tldr-pages/extldr/actions)
[![Inline docs](http://inch-ci.org/github/tldr-pages/extldr.svg?branch=HEAD&style=shields)](http://inch-ci.org/github/tldr-pages/extldr)

ExTldr is an Elixir client for [tldr-pages](https://github.com/tldr-pages/tldr).

## Requirement

  - Erlang/OTP installed (it does not require Elixir, because Elixir is embedded in the script).
    - Read [*Erlang package from official repositories (Linux)*](https://github.com/tldr-pages/extldr/wiki/Erlang-package-from-official-repositories-(Linux)) to know about tested versions of Erlang available on some Linux distributions.
  - Download ExTldr. You can:
    - [Download the latest release](https://github.com/tldr-pages/extldr/releases).
    - Clone this repository.

## Usage

Once you have downloaded ExTldr, and unzipped in the case you downloaded a release, you can execute the script: `./extldr`

The first argument of the script is the operating system, the second argument is the command/term you want search. Below there are some examples:

  - Search command `feh` in the pages of your current operating system:

    `extldr feh`

  - Search Linux command `adduser`:

    `extldr linux adduser`

  - Search a common command, `chroot`, in different operating system:

    `extldr common chroot`

  - Search Linux command `cat`, available in common pages due it is available in different operating systems:

    `extldr linux cat`

Then, if you like, you can make it globally available with a symbolic link or adding it to your `PATH`.

## Planned for next versions

Although I prefer to track possible enhancements and ideas in the issues, below there are some essentials:

  - [ ] Multilingual support ([#1](https://github.com/tldr-pages/extldr/issues/1)).
  - [x] Check by default the operating system in which ExTldr is being executed ([#2](https://github.com/tldr-pages/extldr/issues/2)).

## Inspiration

ExTldr is heavily inspired by the great and awesome work of the tldr-pages community and the actually archived [TLDR Elixir Client](https://github.com/edgurgel/tldr_elixir_client) developed by [Eduardo Gurgel](https://github.com/edgurgel).

## License

ExTldr is licensed under the [GNU General Public License v3.0](https://github.com/tldr-pages/extldr/blob/master/COPYING).
