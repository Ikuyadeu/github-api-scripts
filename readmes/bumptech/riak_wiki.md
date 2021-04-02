# The Riak Wiki

This repo holds all the content (and other bits) for the most-excellent Riak wiki, located at [wiki.basho.com][basho-wiki].

We are using [Gollum][gollum] and [Gollum-Site][gol-site] to generate the wiki. Gollum is a great piece of open source software released by the GitHub team that lets you maintain and build wikis from the contents of a Git repo.

`gollum-site` generates html from pages written in any format supported by Gollum (ASCIIDoc, Creole, Markdown, Textile, etc.).

<A name="contrib">
## How to Contribute

Part of the reason we switched to Gollum and GitHub for the Riak Wiki was to make it easier for people to contribute. So, treat this repo much like you would a code repo: If you have a change (be a minor edit or an entirely new page full of Python client code snippets), simply:

1. [Fork this repo][forking]

2. [Build a local copy][build]

3. Create a new Branch:

        git checkout -b <branch-name>

4. Add your changes

5. Run the specs and fix any formatting issues

        rake spec

6. Commit changes to your branch

7. [Send us a pull request][pull-req]

If it's a small or obvious change, we're likely to merge it right away.  If we have questions, we'll communicate with you using the pull request's issue page.

The [Gollum README][gol-read] provides a great introduction to using the wiki system.

**Anyone can contribute to the Riak Wiki via the process outlined above. That said, there is a group of non-Basho developers who have commit access to this repo and can edit it directly. We call them _Community Wiki Committers_. [See this page][day-labor] if you're interested in becoming one.**

<A name="build">
## Building the Wiki Locally

If you want to build and view the Riak Wiki locally, here is what you need to do:

1. Clone this repo:

        git clone git://github.com/basho/riak_wiki.git

2. Ensure that you have [Bundler][bundler] installed:

        gem install bundler

3. Install all pre-requisite gems:

        bundle install

4. Generate the site and start a local server (This will take a minute. Don't fret.)

        gollum-site generate        # Will generate the files
        gollum-site serve           # Will start the gollum-site server
        gollum-site serve --watch   # Will start the gollum-site server and will regenerate the site
                                    # when changes are made

5. Navigate to <http://localhost:8000/> (Default) to access a fully-functional copy of the Riak Wiki.

## Updating wiki.basho.com

After adding new content or updating existing content in the wiki repo, it then needs to be pushed live to wiki.basho.com. We do this using a post-receive hook [(written by Basho's Dan Reverri)](https://github.com/dreverri/repo-sync-webhook) and the "publish" branch. Here's the process to update the live site. **(Only people who have commit access to this repo will be able to do this.)** 

1. Make sure lastest changes are merged or committed to master branch

2. Checkout "publish" branch
   
	`git checkout publish`

3. Merge changes from master into publish

   	`git merge master`

4. Push changes back to publish branch 

   	`git push origin publish`

After you merge your changes into publish and push them back to the repo, the post-receive hook will fire and wiki.basho.com should be updated 
within several minutes.


<A name="feedback">
## Issues, Questions, Comments, Etc.

* Send Email to [mark@basho.com][phark]

* Use the [Riak Mailing List][mail-list]

* Create a new [Issue][issues]

## Credits

Includes [icons from famfamfam][silk].

## License

The Riak Wiki is licensed under a [Creative Commons Attribution 3.0 Unported License][license].

[phark]:      mailto:mark@basho.com "Mark"
[mail-list]:  http://lists.basho.com/mailman/listinfo/riak-users_lists.basho.com "Riak-Users"
[issues]:     https://github.com/basho/riak_wiki/issues "Riak-Wiki Issues Page"
[forking]:    http://help.github.com/forking/ "Github Forking Guide"
[pull-req]:   http://help.github.com/pull-requests/ "Github Pull-Requests Guide"
[build]:      #build "Building the Wiki"
[bundler]:    https://github.com/carlhuda/bundler/ "Bundler"
[gol-read]:   https://github.com/github/gollum/blob/master/README.md "Gollum README"
[day-labor]:  http://wiki.basho.com/Contributing-to-the-Riak-Wiki.html "Riak Contributors"
[gollum]:     https://github.com/github/gollum "Gollum Repo"
[gol-site]:   https://github.com/dreverri/gollum-site "Gollum-Site Repo"
[basho-wiki]: http://wiki.basho.com "Basho Wiki"
[silk]: http://www.famfamfam.com/lab/icons/silk/ "FamFamFam Silk Icons"
[license]: http://creativecommons.org/licenses/by/3.0/

