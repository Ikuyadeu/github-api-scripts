## BISC: Borrowed Instructions Synthetic Computation

[![Code Climate](https://codeclimate.com/github/trailofbits/bisc.png)](https://codeclimate.com/github/trailofbits/bisc)

BISC is a Ruby library for demonstrating how to build [borrowed-instruction](http://users.suse.com/~krahmer/no-nx.pdf) programs. BISC aims to be simple, analogous to a traditional assembler, minimize behind-the-scenes magic, and let users write simple macros. BISC was developed by Dino Dai Zovi for [Practical Return-oriented Programming](http://blog.trailofbits.com/2010/04/26/practical-return-oriented-programming/) at Blackhat USA 2010 and was used for the [Assured Exploitation](http://www.trailofbits.com/training/#assured-exploitation) training course.

## Technical Overview
BISC utilizes the Ruby librex `peparsey` and `pescan` libraries to scan PE (or `elfparsey` and `elfscan` for ELF) modules for instruction sequences and unused data space that may be borrowed to construct return-oriented programs.  Traditional ROP-Programming relies on composing reused instructions into gadgets, however, BISC makes use of borrowed instruction mnemonics and, as such, is more opportunistic based off of the instructions available in provided executables. BISC does this by scanning through the provided executable files searching for a single instruction followed by a 'ret' which is added to BISC's available vocabulary. This vocabulary can then be pulled from to write and ultimately assemble a borrowed-instruction program to be used for exploitation.

## Installation

### Windows
The most tested and support installation of BISC is on Windows utilizing the Cygwin shell. Note that BISC utilizes the librex gem that Windows Defender will flag as malware and remove. You should run BISC inside of a VM with Windows Defender disabled.

#### BISC on Windows with Cygwin
*NOTE:* If you have Ruby and RubyGems installed on your local Windows computer this method will not work. See the tutorial
'BISC on Windows with Powershell'.

##### Install Ruby and git from cygwin installer.
For Ruby, simply select 'Ruby' from the main package selection window.  This will automatically install Ruby 1.9.3 as 
well as all of the dependencies needed. For git, expand out the Devel tab and look for the package simply named 'git',
and mark this package for installation.

##### Install Ruby's 'bundle' gem
```bash
User@vm ~/bisc
$ gem install bundle
Successfully installed bundle-0.0.1
1 gem installed
Installing ri documentation for bundle-0.0.1...
Installing RDoc documentation for bundle-0.0.1...
```

##### Install BISC
```bash
User@vm ~/bisc
$ bundle install
fatal: Not a git repository (or any of the parent directories): .git
Fetching gem metadata from https://rubygems.org/..
Resolving dependencies...
Installing librex (0.0.68)
Installing metasm (1.0.1)
Using bisc (0.1.0) from source at .
Using bundler (1.5.3)
Your bundle is complete!
Use `bundle show [gemname]` to see where a bundled gem is installed.
```

#### BISC on Windows with Powershell

##### Install Ruby 1.9.3+
Ensure that the ruby bin directory is in your path

##### Install bundle
```cmd
PS C:\Users\User> gem install bundle
Successfully installed bundle-0.0.1
1 gem installed
Installing ri documentation for bundle-0.0.1...
file 'lib' not found
Installing RDoc documentation for bundle-0.0.1...
file 'lib' not found
```

##### Install bisc
```cmd
PS C:\Users\User\Desktop\bisc> bundle install
fatal: Not a git repository (or any of the parent directories): .git
Resolving dependencies...
Using librex (0.0.68)
Using metasm (1.0.1)
Using bisc (0.1.0) from source at .
Using bundler (1.5.3)
Your bundle is complete!
Use `bundle show [gemname]` to see where a bundled gem is installed.
```

## Examples
For an example of how to use BISC, see [examples/CreateThreadStage.rb](https://github.com/trailofbits/bisc/blob/master/examples/CreateThreadStage.rb). This BISC program creates a new thread to run an embedded machine code payload and then runs a "parent" payload in the current thread.

BISC programs are built from a cygwin shell:

    ./examples/CreateThreadStage.rb ./Shockwave-11.5.6r606/*.dll > CreateThreadStage.rop

Testing must be done from a Windows CMD.exe shell:

    ./data/test-rop.exe CreateThreadStage.rop ./Shockwave-11.5.6r606/*.dll

# Contributors
* [@ddz](https://github.com/ddz) (original author)
* [@dgalling](https://github.com/dgalling)
* [@postmodern](https://github.com/postmodern)
* [@PoppySeedPlehzr](https://github.com/PoppySeedPlehzr)
* [@NitinJami](https://github.com/NitinJami)
