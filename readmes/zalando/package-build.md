Package Build
=============

Package-build is a toolset for creating native system packages: .deb for Debian-like and .rpm for RedHat-like OSes. It is useable out-of-the-box.

### The Idea
With a few simple scripts, you can use package-build to create isolated, self-contained packages; provide them in your internal repos; and not worry about deployment and dependencies. You can even use these scripts to package tarballs that are randomly dropped into a web folder. Because a simple shell script performs the actual package-building, you can easily use the same commands in a continuous integration context — i.e., to automatically build packages every time a recipe changes or a new one has been added.

#### Details:
- the whole build process is triggered from [Fabric](https://packages.debian.org/unstable/main/fabric) tasks running on the "build host"
- build slaves are Docker containers to maintain a clean, well-defined environment
- actual package building is done with [fpm](https://github.com/jordansissel/fpm) and [fpm-cookery](https://github.com/bernd/fpm-cookery)

### Setup

Clone the repo and install the Python requirements:

    sudo pip install -r requirements.txt

    cp package-build.yaml-example ~/.config/package-build.yaml
    vim ~/.config/package-build.yaml # adapt to your repo server and distributions for which you want to build packages
    fab docker_build # this will setup the required Docker images and could take a while

If pycrypto makes trouble here, install Python's headers before: `sudo apt-get install python-dev` or `sudo yum install python-devel` depending on your OS.

### How-to

Docker containers provide the build environments, so you'll have to create a new subfolder under `docker/` with a Dockerfile for all the distributions for which you want to create a package. Create an entry in the config file `~/.config/package-build.yaml` for each distribution to map it to a package format ("rpm" or "deb", see the example config file).

As stated above, [fpm](https://github.com/jordansissel/fpm) and [fpm-cookery](https://github.com/bernd/fpm-cookery) do the actual package build. (fpm-cookery automatically builds [only a package for the distribution/OS where it's running] (https://github.com/bernd/fpm-cookery/blob/master/spec/facts_spec.rb#L72).) Create a `recipe.rb` under a subfolder in `recipes/`. Optionally, create a script called `prepare.sh`, meant to be run before `fpm-cook package` is executed.

### $ Command Line Examples
To start the packaging process for different distributions and packages, see the examples below.

Build `facter` for Ubuntu 16.04 ("Xenial"):

    fab package_build:facter,ubuntu16.04

Build `facter` for all configured distributions:

    fab package_build:facter

For testing: The created package will not automatically upload and publish to your repositories unless you set the parameter `upload` to `True`:

    fab package_build:debian7,upload=True

Publish a package to the internal repository for ubuntu16.04 (which is the default distribution):

    fab repo_deb_add:~/path/to/package.deb

To publish a package in the repos for other distributions, you have to pass them explicitly:

    fab repo_deb_add:~/path/to/package.deb,dist=ubuntu12.04

To delete a package from the repo for a specified distribution:

    fab repo_deb_del:dist=ubuntu12.04,chimp

### More Recipe Examples

- [https://github.com/bernd/fpm-recipes](https://github.com/bernd/fpm-recipes)
- [https://github.com/piavlo/fpm-recipes-piavlo](https://github.com/piavlo/fpm-recipes-piavlo)
- [https://github.com/Graylog2/fpm-recipes.git](https://github.com/Graylog2/fpm-recipes.git)
- [https://github.com/haf/fpm-recipes.git](https://github.com/haf/fpm-recipes.git)

### Test Coverage

Currently, there are [no tests for this project](https://github.com/zalando/package-build/issues/22) and test contributions are very welcome. Please see also the _Contributing_ section.

### Contributing

Thanks for your interest in contributing! There are many ways to contribute to this project. [Get started here](CONTRIBUTING.md).

### License

The contents of this repository are licensed under the [MIT License](LICENSE).
