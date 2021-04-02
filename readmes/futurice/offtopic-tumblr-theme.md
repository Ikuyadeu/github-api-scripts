Offtopic - a Tumblr theme for offtopic.futurice.com blog
=================================================================

Notes about committing
----------------------

As static files of the theme are served directly from GitHub pages, please be sure to compile production version CSS and commit only that to the repository. There should be no needs to have anything else than a branch named _gh-pages_ at GitHub.

Production CSS can be compiled with command

    compass compile -e production --force

while for the development version works

    compass compile --force

or

    compass watch .

To automate this whole thing, add these thing to your git commit hooks.

.git/hooks/pre-commit :

    #!/bin/sh
    compass compile -e production --force
    git add */css/*.css

and .git/hooks/post-commit :

    #!/bin/sh
    compass compile --force