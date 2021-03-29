# Localization

This project contains translation files for the Netdata HTML documentation. 
All contributions will be made via GitHub Pull Requests.

## Add translations for a new language

Under the root directory, you will need to add a subdirectory with the language abbreviation as shown at https://squidfunk.github.io/mkdocs-material/getting-started/#localization. If your language does not appear in the `mkdocs-material` translations table, you will see a link that lets you provide a new translation in 5 minutes. Once your language is included in a release of `mkdocs-material`, let us know, so we can ensure our build mechanism uses the version that contains your language.

Underneath your directory you will add markdown files, using the precise structure of the `netdata/netdata`project directory tree. You can translate as many files as you like. The files you provide will be is used to override the existing English markdown file in the localized version. Of course the names of the files need to match precisely. 

For example, to provide a Chinese translation on how to update Netdata, the file should be `zh/packaging/installer/UPDATE.md`.

When you do a pull request with your PR, you will see that a Netlify check is automatically executed for your language as well.  If you click on deploy preview, the HTML documentation at https://docs.netdata.cloud will also be available under `https://docs.netdata.cloud/[abbreviation]`, with only the files you provided translated. For the previous example, the translated page would be available at `https://docs.netdata.cloud/zh/packaging/installer/UPDATE.md`. 

The generated documentation has a language switcher tool, which we will extend with your language, once your PR is successfully merged. 
You may submit a PR yourself, by adding [an option for your language](https://github.com/netdata/netdata/blob/master/docs/generator/custom/themes/material/partials/header.html#L95).   
You can see an example in [PR 7004 of project netdata/netdata](https://github.com/netdata/netdata/pull/7004).

## Translate more documents

If you already see your language in https://docs.netdata.cloud, you will notice that many files are still shown in English. Pressing the 'edit' file will lead you to an invalid location, because no one had added a translation for that file. To provide one yourself:
- Find the relevant .md document in the `netdata/netdata` repo.
- Copy it to the exact same location under `netdata/localization/[abbreviation]`.
- Translate it and create a PR.

## Caution regarding header translations

Headers in markdown documents have a dual use as a section description and a link to a specific part of the document. 
When you translate a header, you will need to find where else in the documentation that header is referenced and change 
that reference as well. 
An alternative workaround to modifying all links to a section is to keep the original, English headers as well. 
This will result in duplicate headings, one in English and one in your language, so it's not a proper solution. 

As soon as [the issue with the build process](https://github.com/netdata/localization/issues/17) is resolved, the check 
for broken links will be done for you by the build process (`checklinks.sh`). 
So you'll be able to easily find the additional files that need to be modified, in order to get a successful build.
