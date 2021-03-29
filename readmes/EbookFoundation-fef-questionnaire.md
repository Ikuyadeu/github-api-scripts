# FEF Questionnaire

## Introduction

FEF Questionnaire is a Django questionnaire app which is easily customizable
and includes advanced dependency support using boolean expressions.

It allows an administrator to create and edit questionnaires in the Django
admin interface, with support for multiple languages.

It can be run either as a survey where subjects are solicited by email, or as a web-based poll.

In either mode, an instance can be linked to an arbitrary object via the django content-types module.

Try out the questionaire on the Unglue.it page for "Open Access Ebooks" https://unglue.it/work/82028/

## History

The questionnaire app was originally developed by [Seantis](https://github.com/seantis), itself derived from [rmt](https://github.com/rmt). Eldest Daughter picked up the project and named it [ED-questionnaire](git://github.com/eldest-daughter/ed-questionnaire)  because they had been using it and the Seantis version had entered a steady state of development. There are several feature changes they wanted and decided to head up the maintenance themselves.

The old versions are tagged as follows:

 * tag 1.0 - state of last commit by the original developer (rmt)
 * tag 1.1 - contains merged changes by other forks improving the original
 * tag 2.0 - original updated trunk from Seantis version
 * tag 2.5 - contains the original Seantis version and all PRs merged in as of 12/09/15. It's considered to be the backwards compatible version of the repository.

The "ED-questionnaire" version was dubbed v3.0. It is not compatible with the v2.x branches.

The "FEF-questionnaire" version was created to add the ability to link the questionnaire to individual books in a book database. We'll call this v4.0. The app was extensively renovated and updated. This work was funded by the Mellon Foundation as part of the [Mapping the Free Ebook Supply Chain Project](https://www.publishing.umich.edu/projects/mapping-the-free-ebook/).

## About this Manual

Questionnaire was not a very well documented app so far to say the least. This manual should give you a general idea of the layout and concepts of it, but please help us improve it.

What it does cover is the following:

 * **Integration** lays out the steps needed to create a new Django app together with the questionnaire. The same steps can be used to integrate the questionnaire into an existing site (though you would be entering unpaved ways).
 * **Concepts** talks about the data model and the design of the application.
 * **Migration** explains how a questionnaire defined with 1.0 can be used in 2.0.
 * **2.0 Postmortem** talks about some experiences made during the development of 2.0.

    
    
## Integration

### Install

If you just want to install, start with 

    pip install fef-Questionnaire
    
### Example Setup

This part of the docs will take you through the steps needed to create a questionnaire app from scratch. It should also be quite handy for the task of integrating the questionnaire into an existing site.

First, create a folder for your new site:

    mkdir site
    cd site

Create a virtual environment so your python packages don't influence your system
    
    virtualenv --no-site-packages -p python2.7 .

Activate your virtual environment

    source bin/activate

Install Django

    pip install django==1.8.18

Create your Django site

    django-admin.py startproject example

Create a place for the questionnare

    cd example
    mkdir apps
    cd apps

Clone the questionnaire source

    git clone git://github.com/EbookFoundation/fef-questionnaire.git

You should now have a fef-questionnaire folder in your apps folder

    cd fef-questionnaire

The next step is to install the questionnaire.

    python setup.py install

If you are working with ed-questionnaire from your own fork you may want to use `python setup.py develop` instead, which will save you from running `python setup.py install` every time the questionnaire changes.

Now let's configure your basic questionnaire OR copy the settings.py, urls.py, and models.py files from the "example" folder into `example/example`, then skip down to [initialize your database](#initialize-the-database).


Also add the locale and request cache middleware to MIDDLEWARE_CLASSES:

    'questionnaire.request_cache.RequestCacheMiddleware'

Add the questionnaire template directory as well as your own to TEMPLATES:

    'DIRS': [os.path.join(BASE_DIR, 'example/templates/')],

If you want to use multiple languages, add the i18n context processor to TEMPLATES
    'context_processors': ['django.template.context_processors.i18n',]

Now add `transmeta`, `questionnaire` to your INSTALLED_APPS:

    'transmeta',
    'questionnaire',
    'questionnaire.page',

To finish the settings, add the fef-questionaire specific parameters. For our example, we'll use:
    
    QUESTIONNAIRE_PROGRESS = 'async'
    QUESTIONNAIRE_USE_SESSION = False
    QUESTIONNAIRE_ITEM_MODEL = 'example.Book'
    QUESTIONNAIRE_SHOW_ITEM_RESULTS = True

Next up we want to edit the `urls.py` file of your project to link the questionnaire views to your site's url configuration. The example app shows you how.

Finally, we want to add a model to the example app for us to link our questionnaires to. It needs to have a back-relation named "items"

    class Book(models.Model):
        title = models.CharField(max_length=1000, default="")
        landings = GenericRelation(Landing, related_query_name='items')
        def __unicode__(self):
            return self.title


### Initialize the database

Having done that we can initialize our database. (For this to work you must have set up your DATABASES in `settings.py`.). First, in your CLI navigate back to the `example` folder:

    cd ../..

The check that you are in the proper folder, type `ls`: if you can see `manage.py` in your list of files, you are good. Otherwise, find your way to the folder that contains that file. Then type:

    python manage.py migrate

You will be asked to create a superuser.

The questionnaire expects a `base-questionnaire.html` template to be there, with certain stylesheets and blocks inside. Have a look at `./apps/fef-questionnaire/example/templates/base-questionnaire.html`. if you're adding the app to an existing project.

Congratulations, you have setup the basics of the questionnaire! At this point this site doesn't really do anything, as there are no questionnaires defined.

### Internationalizating the database

First, you want to setup the languages used in your questionnaire. Open up your `example` folder in your favorite text editor.

Open `example/example/settings.py` and add following lines, representing your languages of choice:

    LANGUAGES = (
        ('en', 'English'),
        ('de', 'Deutsch')
    )

Now, you'll need to 

    python manage.py makemigrations
    python manage.py migrate

If you want to use multiple languages, add the i18n context processor to TEMPLATES
    'context_processors': ['django.template.context_processors.i18n',]
    
and set up middleware as described in the [Django translation docs](https://docs.djangoproject.com/en/1.8/topics/i18n/translation/)

To see example questionnaires you can do the following (Note: this will only work if you have both English and German defined as Languages in `settings.py`):

    python manage.py loaddata ./apps/fef-questionnaire/example/fixtures/example.yaml
    python manage.py loaddata ./apps/fef-questionnaire/example/fixtures/books.yaml


### Start the server!

Start your development server:

    python manage.py runserver

And navigate to [localhost:8000](http://localhost:8000/).

First, go to the admin console and log yourself in. Otherwise, there won't be items for you to link  questionnaires to.

Take a questionnaire. the "Example" has English and German translations. the "MappingSurvey" is English only.



## Concepts

The ED Questionnaire has the following tables, described in detail below.

 * Subject
 * RunInfo
 * RunInfoHistory
 * Question
 * Choice
 * QuestionSet
 * Questionnaire
 * Answer
 * Landing

### Subject

A subject is someone filling out a questionnaire. 

Subjects are primarily useful in a study where the participants answer a questionnaire repeatedly. In this case a subject may be entered. Whoever is conducting the study (i.e. the person running the questionnaire app), may then periodically send emails inviting the subjects to fill out the questionnaire.

Sending Emails is covered in detail later.

Of course, not every questionnaire is part of a study. Sometimes you just want to find out what people regard as more awesome: pirates or ninjas*? 

*(it's pirates!)

Though a poll would be a better choice for this example, one can find the answer to that question with ED Questionnaire by using an anonymous subject. The next chapter *Questionnaire* will talk about that in more detail.

### RunInfo

A runinfo refers to the currently active run of a subject.

A subject who is presently taking a questionnaire is considered to be on a run. The runinfo refers to that run and carries information about it.

The most important information associated with a runinfo is the subject, a random value that is used to generate the unique url to the questionnaire, the result of already answered questions and the progress.

Once a run is over it is deleted with some information being carried over to the RunInfoHistory.

Runs can be tagged by any number of comma separated tags. If tags are used, questions can be made to only show up if the given tag is part of the RunInfo.

### RunInfoHistory

The runinfo history is used to refer to a set of answers.

### Question

A question is anything you want to ask a subject. There are a number of different types you can use:

 * **choice-yesno** - Yes or No
 * **choice-yesnocomment** - Yes or No with a chance to comment on the answer
 * **choice-yesnodontknow** - Yes or No or Whaaa?
 * **open** - A simple one line input box
 * **open-textfield** - A box for lengthy answers
 * **choice** - A list of choices to choose from
 * **choice-freeform** - A list of choices with a chance to enter something else
 * **choice-multiple** - A list of choices with multiple answers
 * **choice-multiple-freeform** - Multiple Answers with multiple user defined answers
 * **range** - A range of number from which one number can be chosen
 * **number** - A number
 * **timeperiod** - A timeperiod
 * **custom** - Custom question using a custom template
 * **comment** - Not a question, but only a comment displayed to the user
 * **sameas** - Same type as another question

*Some of these types, depend on checks or choices. The number question for instance can be controlled by setting the checks to something like `range=1-100 step=1`. The range question may also use the before-mentioned checks and also `unit=%`. Other questions like the choice-multiple-freeform need a `extracount=10` if ten extra options should be given to the user.

I would love to go into all the details here but time I have not so I my only choice is to kindly refer you to the qprocessor submodule which handles all the question types.*

Next up is the question number. The question number defines the order of questions alphanumerically as long as a number of questions are shown on the same page. The number is also used to refer to the question.

The text of the question is what the user will be asked. There can be one text for each language defined in the `settings.py` file.

The extra is an additional piece of information shown to the user. As of yet not all questions support this, but most do.

An important aspect of questions (and their parents, QuestionSets) is the checks field. The checks field does a lot of things (possibly too many), the most important of which is to define if a certain question or questionset should be shown to the current subject.

The most important checks on the question are the following:

 * **required** A required question must be answered by the user
 * **requiredif="number,answer"**  Means that the question is required if the question with *number* is equal to *answer*.
 * **shownif** Same as requiredif, but defining if the question is shown at all.
 * **maleonly** Only shown to male subjects
 * **femaleonly** Only shown to female subjects
 * **iftag="tag"** Question is only shown if the given tag is in the RunInfo

Checks allow for simple boolean expressions like this:
`iftag="foo or bar"` or `requiredif="1,yes and 2,no"`

### Choice

A choice is a possible value for a multiple choice question.

### QuestionSet

A number of questions together form a questionset. A questionset is ultimately single page of questions. Questions in the same questionset are shown on the same page.

QuestionSets also have checks, with the same options as Questions. There's only one difference, **required** and **requiredif** don't do anything.

A questionset which contains no visible questions (as defined by **shownif**) is skipped.

### Answer

Contains the answer to a question. The value of the answer is stored as JSON.

### Questionnaire 

A questionnaire is a group of questionsets together.

### Landing 

In Poll mode, the landing url links a Questionnaire to an Object and a User to a Subject. This is useful if you have a database of things you want to ask questions about.

Migration of 1.x to 2.0
-----------------------

Version 4.0 does not support migration of 1.X data files.

2.0 Postmortem
--------------

2.0 was the result of the work we put into Seantis questionnaire for our second project with it. We did this project without the help of the questionnaire's creator and were pretty much on our own during that time.

Here's what we think we learned:

### Questionnaire is a Framework

More than anything else ed.questionnaire should be thought of as a framework. Your site has to provide and do certain things for the questionnaire to work. If your site is a customized questionnaire for a company with other needs on the same site you will end up integrating code which will call questionnaire to setup runs and you will probably work through the answer records to provide some sort of summary.

If it was a library you could just work with a nice API, which does not exist.

### Don't Go Crazy with Your Checks

We used a fair amount of checks in both questionset and questions to control a complex questionnaire. We offloaded the complexity of the questionnaire into an Excel file defined by the customer and generated checks to copy that complexity into our application.

Though this approach certainly works fine it does not give you a good performance. The problem is, if you have hundreds of questions controlled by runinfo tags, that you end up with most CPU cycles spent on calculating the progress bar on each request. It is precisely for that reason that we implemented the QUESTIONNAIRE_PROGRESS setting (you can learn more about that by looking at the example settings.py).

We managed to keep our rendering time low by doing the progress bar using AJAX after a page was rendered. It is only a workaround though. Calculating the progress of a run in a huge questionnaire remains a heavy operation, so for really huge questionnaires one might consider removing the progress bar altogether. There is still some optimization to be made, but it essentially will remain the slowest part of the questionnaire, because at the end of the day interpreting loads of checks is not something you can do in a fast way, unless your name is PyPy and your programmers are insanely talented.

### There are not Enough Tests

There are a few that do some simple testing, but more are needed. More tests would also mean that more refactoring could be done which would be nice, because there certainly is a need for some refactoring.

### The Admin Interface is not Good Enough

Django admin is a nice feature to have, but we either don't leverage it well enough, or it is not the right tool for the questionnaire. In any case, if you are expecting your customer to work with the questionnaire's structure you might have to write your own admin interface. The current one is not good enough.

4.0 Changes
--------------
Version 4.0 has not been tested for compatibility with previous versions.

* Broken back links have been fixed. The application works in session mode and non-session mode.
* We've updated to Bootstrap 3.3.6 and implemented label tags for accessibility
* "landings" have been added so that survey responses can be linked to arbitrary models in an application. template tags have been added that allow questions and answers to refer to those models.
* question types have been added so that choices can be offered without making the question required.
* styling of required questions has been spiffed up.
* export of response data has been fixed.
* compatibility with Django 1.8. Compatibility with other versions of Django has not been tested.
* refactoring of views
* documentation has been updated to reflect Django 1.8.
* email and subject functionality has not been tested

4.0.1
---------------
Updated for Django 1.11

5.0
---------------
Updated for Python 3.6



