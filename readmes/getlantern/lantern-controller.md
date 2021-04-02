# Lantern Controller

This is the software for globally controlling the Lantern network.


## Development

To run the development server from the command-line, you will need Maven 3.1.0
or higher.  Then, just run `mvn appengine:devserver`.

To bring this project and its submodules into Eclipse, just do the following:

1. git clone --recursive git@github.com:getlantern/lantern-controller.git
   
   If you have already checked out lantern-controller but did not pass
   '--recursive', you can clone its submodules with
   `git submodule update --init`.
   
1. Open Eclipse
1. File->Import...->Existing Projects into Workspace
1. Choose the lantern-controller directory 


## Deployment

To deploy a new version,
 - clone the too-many-secrets repo alongside this one, and
 - run `./deploy.py [<controller-id> [<bump-version? (y/n)> [<set-version-as-default? (y/n)>]]]`.

You'll be prompted for any arguments you don't provide in the command line.

## Admin Pages

Lantern Controller makes the following admin pages available for various
management tasks:

- `https://<appid>.appspot.com/admin/index.jsp` - misc. global state
- `https://<appid>.appspot.com/admin/invites.html` - approve
  pending invites
- `https://<appid>.appspot.com/admin/latest.html` - set latest lantern version

### CSRF Protection

If you do not yet have a CSRF protection cookie for the domain the admin pages
are served on, visit the /admin/invites.html page, which should trigger an ajax
GET and result in your getting a CSRF cookie (inspect document.cookies to
verify). Once you have the CSRF cookie, you will be able to use other admin
pages like /admin/latest.html from that point forward.

## Setting up a Test Lantern Controller

 1. Set up a appengine instance
 2. Add an entry with your controller id to [versions](versions)
 3. In `Dao.java`, flip the boolean guard in `createInitialUser`.
 4. Open `org.lantern.RemoteApi.java` and edit it to call
    dao.createInitialUser() - this will set up a seed user with which you can
    run Lantern
 5. Open `org.lantern.MaintenanceTask.java` and edit the doPost to call `new Dao().createInitialUser()` 
 6. Launch up a cloudmaster using launch_cloudmaster.py per the instructions [here](https://github.com/getlantern/lantern_aws)
 7. Deploy your app using `deploy.py` (make sure to specify the right instance
    name).
 8. Go to /admin/index.jsp of your app in a browser and run your maintenance task, specifying the email address for your initial user
 9. Revert `Dao.java`
 10. Revert `RemoteApi.java`
 11. Visit `https://<your app id>.appspot.com/admin/invites.html` (this is just to get a CSRF cookie, as in the section **CSRF Protection** above.)
 12. Visit `https://<your app id>.appspot.com/admin/latest.html` and enter details for the latest version that this controller knows about.

## i18n

Translated strings are fetched from json files in the "locale" directory. To
add or change a translated string, update the corresponding mapping in the
source file "locale/en_US.json", and add or update any references to it as
needed.

### Transifex

All translatable content for Lantern has been uploaded to [the Lantern
Transifex project](https://www.transifex.com/projects/p/lantern/) to help
manage translations. Translatable strings from this code have been uploaded to
the [controller resource](https://www.transifex.com/projects/p/lantern/resource/email/)
therein. Transifex has been set up to automatically pull updates to that
resource from [its GitHub
url](https://raw.github.com/getlantern/lantern-controller/master/locale/en_US.json)
(see
http://support.transifex.com/customer/portal/articles/1166968-updating-your-source-files-automatically
for more information).

After translators add translations of these strings to the Transifex project,
the [Transifex
client](http://support.transifex.com/customer/portal/articles/960804-overview)
can be used to pull them. See
http://support.transifex.com/customer/portal/articles/996157-getting-translations
for more.


## Generating email templates

The emails the controller sends out are assembled from a template containing
the html (e.g.
[src/main/resources/org/lantern/email/invite-notification.tmpl](https://github.com/getlantern/lantern-controller/tree/master/src/main/resources/org/lantern/email/invite-notification.tmpl)),
a sass stylesheet containing the styles (
[src/main/resources/org/lantern/email/style.sass](https://github.com/getlantern/lantern-controller/tree/master/src/main/resources/org/lantern/email/style.sass)),
and the json files containing the translated strings (e.g.
[locale/en_US.json](https://github.com/getlantern/lantern-controller/tree/master/locale/en_US.json)).
These sources are combined into a final html file suitable to be emailed, i.e. with
all translations and css rules inlined so that they will be displayed properly
by email clients (e.g.
[src/main/resources/org/lantern/email/invite-notification.html](https://github.com/getlantern/lantern-controller/tree/master/src/main/resources/org/lantern/email/invite-notification.html)). This final html is then passed to
[Mandrill](https://mandrillapp.com) for delivery, along with any
[merge variables](http://help.mandrill.com/entries/21678522-How-do-I-use-merge-tags-to-add-dynamic-content-)
to interpolate into it.

Any time the source content of these emails changes (e.g. a language tweak
to a string in the json, a style tweak to the sass, etc.), run `./generate_emails.py`
to regenerate the final html. Run the script from a Python 2.7 environment with
the following packages installed:

  - [Jinja2 2.7.1](https://pypi.python.org/pypi/Jinja2/2.7.1)
  - [premailer 1.2.3](https://pypi.python.org/pypi/premailer/1.2.3)

The recommended way of doing this is to create a
[virtualenv](https://pypi.python.org/pypi/virtualenv), cd into it and source
its activate script, and then run `pip install` commands for the required
packages.

Also make sure you have [compass](http://compass-style.org/) 0.12.2 installed,
which is required to compile the sass. You can run
`gem install compass --version '= 0.12.2'` to install it (sudo as necessary).
If the sass hasn't changed since the last time it was compiled, you can run
`./generate_emails.py nosass` to skip the compass compilation step.

Any time a **new** translation file is pulled from Transifex (see the
[Transifex](#transifex) section above), a corresponding `Lang` instance should
be added to the `LANGS` list in generate_emails.py. For instance, if "tx pull"
pulls a new file "locale/es_ES.json", add an entry to `LANGS` like
`Lang('es_ES', 'Español', 'ltr')`. The next time you run
`./generate_emails.py`, a new section will be added to the generated emails for
the Spanish translation.
