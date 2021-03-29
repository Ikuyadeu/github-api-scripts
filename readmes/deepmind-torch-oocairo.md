Lua-OOCairo provides Lua with full access to the Cairo vector graphics API.
It can be used for drawing onto bitmap images and saving the resulting files
in PNG format, or for generating files in vector formats like SVG and PDF.
It can also be used for drawing in a Gtk+ GUI application.


## Documentation

Full reference documentation for all the functions and methods supported
by this module are provided in the 'doc' directory in the source code in
POD and Unix manpage format, and on the website as web pages:

    http://www.geoffrichards.co.uk/lua/oocairo/doc/


## Examples

There are example programs in the 'examples' directory of the source code,
which demonstrate many of the features available.  Feel free to copy bits
of code from them to get started.  All example programs should be run from
within the extracted source code directory, but not from in the 'examples'
directory itself, and they will save their output files into the current
directory.  You may need to use the LUA_CPATH environment variable if you
want to the examples to run after you've compiled, but not installed, the
module:

    LUA_CPATH='.libs/liblua-?.so;;' lua examples/arc.lua
    # saves 'arc.png'

If you just want to see what output is produced from the different examples
but aren't in a position to run them yet, the output files are shown here:

    http://www.geoffrichards.co.uk/lua/oocairo/example/


## Using with Gtk+

This module can now (as of version 1.2) be used to draw in a window in a
graphical user interface created with the Lua-Gnome/Gtk package.  See the
programs examples/gtk-drawing.lua and examples/gtk-image.lua for code which
uses most of the new features.  This new stuff has so far only been tested
with lua-gtk-0.9.

## Using with Torch

Surfaces can be exported as tensors using the function rgb2tensor with the
following prototype:

    rgb2tensor(surface, [useAlpha])

This returns either a 3xNxM or 4xNxM ByteTensor with values in the range [0,
255].

The inverse operation can be achieved with the function tensor2rgb24.

## Compiling

The supplied 'Makefile' or 'Makefile.osx' should work on Linux and MacOS X
without changes (just run 'make'), although on some Linux distributions you
might need to change the 'pkg-config' commands if the names used are
different.  On other platforms you might need to provide the compiler options
for finding the Lua and Cairo libraries yourself, rather than relying on
pkg-config.

On a Debian system you should be able to install the precompiled Debian
packages, or build your own if they don't work by running
'dpkg-buildpackage -tc -uc -us -rfakeroot' from in the unpacked tarball.

Let me know if you can provide compilation instructions for other platforms.


## Installing

There is a 'make install' target which will install the compiled library
and manpages, by default under '/usr/local'.  You can install manually
just by copying the compiled library file to the appropriate place.  That
should be enough to use the module.


## Running tests

The module comes with a test suite in the 'test' directory, which at least
on Linux systems can be run with 'make test'.  If there are any problems
with the test programs being able to load your compiled 'oocairo' module,
try adjusting the first few lines of 'test-setup.lua'.

The tests are run with a slightly modified Lunit 0.4, which is included.
They should all pass.  Some tests won't run if they can't load an extra
module they need, but they shouldn't produce failures even then.
