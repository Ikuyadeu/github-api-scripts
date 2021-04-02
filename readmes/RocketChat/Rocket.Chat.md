![](https://github.com/RocketChat/Rocket.Chat.Artwork/raw/master/Logos/2020/png/logo-horizontal-red.png)

<h1 align="center">
  The Ultimate Open Source WebChat Platform
</h1>

[![Rocket.Chat](https://open.rocket.chat/images/join-chat.svg)](https://open.rocket.chat/)
[![Build Status](https://img.shields.io/travis/RocketChat/Rocket.Chat/master.svg)](https://travis-ci.org/RocketChat/Rocket.Chat)
[![Project Dependencies](https://david-dm.org/RocketChat/Rocket.Chat.svg)](https://david-dm.org/RocketChat/Rocket.Chat)
[![devDependencies Status](https://david-dm.org/RocketChat/Rocket.Chat/dev-status.svg)](https://david-dm.org/RocketChat/Rocket.Chat?type=dev)
[![Codacy Badge](https://api.codacy.com/project/badge/grade/8580571ba024426d9649e9ab389bd5dd)](https://www.codacy.com/app/RocketChat/Rocket-chat)
[![Coverage Status](https://coveralls.io/repos/RocketChat/Rocket.Chat/badge.svg)](https://coveralls.io/r/RocketChat/Rocket.Chat)
[![Code Climate](https://codeclimate.com/github/RocketChat/Rocket.Chat/badges/gpa.svg)](https://codeclimate.com/github/RocketChat/Rocket.Chat)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/RocketChat/Rocket.Chat/raw/master/LICENSE)

* [**NEW!** Rocket.Chat Moving to a Single Codebase](#moving-to-a-single-codebase)
* [Community](#community)
* [Mobile Apps](#mobile-apps)
* [Desktop Apps](#desktop-apps)
* [Deployment](#deployment)
   * [Snaps](#instant-server-installation-with-snaps)
   * [DigitalOcean](#digitalocean-droplet)
   * [RocketChatLauncher](#rocketchatlauncher)
   * [Layershift](#layershift)
   * [Yunohost.org](#yunohostorg)
   * [IndieHosters](#indiehosters)
   * [Ubuntu 16.04](#ubuntu-1604)
   * [Cloudron.io](#cloudronio)
   * [Helm Kubernetes](#helm-kubernetes)
  * [Scalingo](#scalingo)
  * [Sloppy.io](#sloppyio)
  * [Docker](#docker)
  * [Ansible](#ansible)
  * [Raspberry Pi 4](#raspberry-pi-4)
  * [Koozali SME](#koozali-sme)
  * [Ubuntu VPS](#ubuntu-vps)
  * [D2C.io](#d2cio)
  * [Syncloud.org](#syncloudorg)
* [About Rocket.Chat](#about-rocketchat)
  * [In the News](#in-the-news)
  * [Features](#features)
  * [Roadmap](#roadmap)
  * [How it all started](#how-it-all-started)
  * [Awards](#awards)
  * [Issues](#issues)
  * [Stack Overflow](#stack-overflow)
  * [Integrations](#integrations)
  * [Documentation](#documentation)
  * [License](#license)
* [Development](#development)
 * [Quick Start](#quick-start-for-code-developers)
  * [Branching Model](#branching-model)
  * [Translations](#translations)
  * [How to Contribute](#how-to-contribute)
* [Credits](#credits)
* [Help Wanted](#help-wanted)
* [Donate](#donate)

# Moving to a Single Codebase

Rocket.Chat is moving to a single codebase. Get to know the reasons and how the community will benefit from it. Read the [details](https://rocket.chat/rocket-chat-is-moving-to-a-single-codebase-get-to-know-the-reasons-and-how-the-community-will-benefit-from-it/).

# Help Wanted

At Rocket.Chat, our community drives *everything* we do. The Rocket.Chat team is expanding, and we know no better place to find qualified new team members than *right here* - in our GitHub  community.

If you are passionate about our project, want to work with a world-leading open source team, and enjoy working remotely at a location of your choice, then we want to talk to you!

Get to know more about us and explore current openings at https://jobs.rocket.chat/"

# Community
Join thousands of members worldwide 24/7 in our [community server](https://open.rocket.chat).

[![Rocket.Chat](https://open.rocket.chat/api/v1/shield.svg?type=channel&name=Rocket.Chat&channel=support)](https://open.rocket.chat/channel/support) for help from our community with general Rocket.Chat questions.

[![Rocket.Chat](https://open.rocket.chat/api/v1/shield.svg?type=channel&name=Rocket.Chat&channel=dev)](https://open.rocket.chat/channel/dev) for developers needing help from the community to developing new features.

You can also join the conversation on [Twitter](https://twitter.com/RocketChat) and [Facebook](https://www.facebook.com/RocketChatApp).

## Share your story
We’d love to hear about [your experience](https://survey.zohopublic.com/zs/e4BUFG) and potentially feature it on our [Blog](https://rocket.chat/case-studies/?utm_source=github&utm_medium=readme&utm_campaign=community).

## Subscribe for Updates
Once a month our marketing team releases an email update with news about product releases, company related topics, events and use cases. [Sign Up!](https://rocket.chat/newsletter/?utm_source=github&utm_medium=readme&utm_campaign=community)

# Desktop Apps
Download the Native Cross-Platform Desktop Application at [Rocket.Chat.Electron](https://github.com/RocketChat/Rocket.Chat.Electron/releases)


# Mobile Apps

[![Rocket.Chat on Apple App Store](https://user-images.githubusercontent.com/551004/29770691-a2082ff4-8bc6-11e7-89a6-964cd405ea8e.png)](https://itunes.apple.com/us/app/rocket-chat/id1148741252?mt=8) [![Rocket.Chat on Google Play](https://user-images.githubusercontent.com/551004/29770692-a20975c6-8bc6-11e7-8ab0-1cde275496e0.png)](https://play.google.com/store/apps/details?id=chat.rocket.android)  [![](https://user-images.githubusercontent.com/551004/48210349-50649480-e35e-11e8-97d9-74a4331faf3a.png)](https://f-droid.org/en/packages/chat.rocket.android/)

# Deployment

## Instant Server Installation with Snaps

Install Rocket.Chat in seconds on Linux (Ubuntu and others) with:

```
sudo snap install rocketchat-server
```

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/rocketchat-server)

Installing snaps is very quick. By running that command you have your full Rocket.Chat server up and running. Snaps are secure. They are isolated with all of their dependencies. Snaps also auto-update when we release new versions.

Our snap features a built-in reverse proxy that can request and maintain free Let's Encrypt SSL certificates. You can go from zero to a public-facing SSL-secured Rocket.Chat server in less than 5 minutes.

Find out more information about our snaps [here](https://rocket.chat/docs/installation/manual-installation/ubuntu/snaps/).

## DigitalOcean droplet

Deploy to a DigitalOcean droplet with our one-click install listing from the DigitalOcean Marketplace.

[![do-btn-blue](https://user-images.githubusercontent.com/51996/58146107-50512580-7c1a-11e9-8ec9-e032ba387c2a.png)](https://marketplace.digitalocean.com/apps/rocket-chat?action=deploy&refcode=1940fe28bd31)


## Layershift

Instantly deploy your Rocket.Chat server for free on next generation auto-scaling PaaS.

[![Layershift Hosting](https://github.com/Sing-Li/bbug/raw/master/images/layershift.png)](http://jps.layershift.com/rocketchat/deploy.html)

Painless SSL. Automatically scale your server cluster based on usage demand.

## Yunohost.org
Host your own Rocket.Chat server in a few seconds.

[![Install RocketChat with YunoHost](https://install-app.yunohost.org/install-with-yunohost.png)](https://install-app.yunohost.org/?app=rocketchat)

## IndieHosters
Get your Rocket.Chat instance hosted in an "as a Service" style. You register and we manage it for you! (updates, backup...).

<!-- [![Rocket.Chat on IndieHosters](https://indiehosters.net/img/generated/logo-indiehosters-horizontal-681-4b587b638.png)](https://indiehosters.net/shop/product/rocket-chat-21) -->
<a href="https://indiehosters.net/shop/product/rocket-chat-21"><img src="https://indiehosters.net/img/generated/logo-indiehosters-horizontal-681-4b587b638.png" alt="Rocket.Chat on IndieHosters" width="200" height="30"></a>

## Cloudron.io

Install Rocket.Chat on [Cloudron](https://cloudron.io) Smartserver:

[![Install](https://cloudron.io/img/button.svg)](https://cloudron.io/button.html?app=chat.rocket.cloudronapp)

## Helm Kubernetes
Deploy on Kubernetes using the official [helm chart](https://github.com/helm/charts/tree/master/stable/rocketchat).

## Scalingo
Deploy your own Rocket.Chat server instantly on [Scalingo](https://scalingo.com).

[![Deploy on Scalingo](https://cdn.scalingo.com/deploy/button.svg)](https://my.scalingo.com/deploy?source=https://github.com/RocketChat/Rocket.Chat#master)


## Sloppy.io
Host your docker container at [sloppy.io](http://sloppy.io). Get an account and use the [quickstarter](https://github.com/sloppyio/quickstarters/tree/master/rocketchat).


## Docker
[Deploy with docker compose](https://rocket.chat/docs/installation/docker-containers/docker-compose/)

[![Rocket.Chat logo](https://d207aa93qlcgug.cloudfront.net/1.95.5.qa/img/nav/docker-logo-loggedout.png)](https://hub.docker.com/r/rocketchat/rocket.chat/)

OR Use the automated build image of our [most recent release](https://hub.docker.com/r/rocketchat/rocket.chat/)

```
docker pull rocketchat/rocket.chat:latest
```

OR select a specific release ([details of releases available](https://github.com/RocketChat/Rocket.Chat/releases)):
```
docker pull rocketchat/rocket.chat:vX.X.X
```

OR our [official docker registry image](https://hub.docker.com/_/rocket.chat/), containing recent stable release build approved by Docker:

```
docker pull rocket.chat
```

## Ansible
Automated production-grade deployment in minutes, for RHEL / CentOS 7 or Ubuntu 14.04 LTS / 15.04.

[![Ansible deployment](https://raw.githubusercontent.com/Sing-Li/bbug/master/images/ansible.png)](https://rocket.chat/docs/installation/automation-tools/ansible/)

## Raspberry Pi 4
Run Rocket.Chat on this world famous $35 quad-core server.

[![Raspberry Pi 4](https://raw.githubusercontent.com/Sing-Li/bbug/master/images/pitiny.png)](https://github.com/RocketChat/Rocket.Chat.RaspberryPi)

## Koozali SME

Add Rocket.Chat to this world famous time tested small enterprise server today.

[![Koozali SME](https://raw.githubusercontent.com/Sing-Li/bbug/master/images/koozali.png)](https://wiki.contribs.org/Rocket_Chat)

## Ubuntu VPS
Follow these [deployment instructions](https://rocket.chat/docs/installation/manual-installation/ubuntu/).

## D2C.io
Deploy Rocket.Chat stack to your server with [D2C](https://d2c.io/). Scale with a single click, check live logs and metrics:

[![Deploy](https://github.com/mastappl/images/blob/master/deployTo.png)](https://panel.d2c.io/?import=https://github.com/d2cio/rocketchat-stack/archive/master.zip/)

## Syncloud.org
Run Rocket.Chat on your easy to use personal device.

[![Deploy](https://syncloud.org/images/logo_min.svg)](https://syncloud.org)

# About Rocket.Chat

Rocket.Chat is a Web Chat Server, developed in JavaScript, using the [Meteor](https://www.meteor.com/install) full stack framework.

It is a great solution for communities and companies wanting to privately host their own chat service or for developers looking forward to build and evolve their own chat platforms.

## In the News

##### [Wired](http://www.wired.com/2016/03/open-source-devs-racing-build-better-versions-slack/)
> Open Sourcers Race to Build Better Versions of Slack

##### [Hacker News](https://news.ycombinator.com/item?id=9624737)
> Yes, we made it to the #1

##### [Product Hunt](https://www.producthunt.com/tech/rocket-chat)
> Your own open source Slack-like chat

##### [JavaScript Weekly](http://javascriptweekly.com/issues/234)
> An open source Web based, channel based chat system (a la Slack) built using Meteor, the full stack JavaScript development platform.

##### [Open Source China](http://www.oschina.net/p/rocket-chat)
> Rocket.Chat 是特性最丰富的 Slack 开源替代品之一。 主要功能：群组聊天，直接通信，私聊群，桌面通知，媒体嵌入，链接预览，文件上传，语音/视频 聊天，截图等等。

##### [wwwhatsnew.com](http://wwwhatsnew.com/2015/05/30/rocket-chat-para-los-programadores-que-quieran-ofrecer-un-chat-en-su-web/)
> Para los programadores que quieran ofrecer un chat en su web

##### [clasesdeperiodismo.com](http://www.clasesdeperiodismo.com/2015/05/30/un-chat-de-codigo-abierto-que-puedes-anadir-a-la-web/)
> Un chat de código abierto que puedes añadir a la web

##### [snowulf.com](https://snowulf.com/2015/09/25/why-slack-when-you-can-rocket-chat/)
> Why Slack when you can Rocket.chat?

##### [liminality.xyz](http://liminality.xyz/self-hosting/)
> Self-hosted alternatives to popular cloud services


## Features

- BYOS (Bring Your Own Server)
- Multiple Rooms
- Direct Messages
- Private Groups
- Public Channels
- Desktop Notifications
- Mentions
- Avatars
- Markdown
- Emojis
- Custom Emojis
- Reactions
- One touch Geolocation
- TeX Math Rendering - inline math typesetting
- Media Embeds
- Link Previews
- Sent Message Edit and Deletion
- Transcripts / History
- File Upload / Sharing
- Scalable file sharing - S3 uploads with CDN downloads
- Full text search
- Global search (from all channels/rooms at once)
- Live chat / Messaging call center
- LDAP Authentication
- CAS 1.0, 2.0 support for educational institutions and hosting providers worldwide
- Support for Okta SSO through SAML v2
- I18n - Supports 22 Languages
- Hubot Friendly
- (Beta) Face to Face Video Conferencing (aka WebRTC )
- (Beta) Multi-users Video Group Chat
- (Beta) Jitsi integration
- Audio calls
- Multi-users Audio Conference
- Screen sharing
- Drupal 7.x and 8.x Plug-in (both stable and development flavours) ([download](https://www.drupal.org/project/rocket_chat)  and [source code](https://git.drupal.org/project/rocket_chat.git) )
- XMPP bridge ([try it](https://open.rocket.chat/channel/general))
- REST APIs
- Remote Video Monitoring
- Native real-time APIs for Microsoft C#, Visual Basic, F# and other .NET supported languages ([Get it!](https://www.nuget.org/packages/Rocket.Chat.Net/0.0.12-pre))
- API access from [Perl](https://metacpan.org/pod/Net::RocketChat) and [Java](https://github.com/baloise/rocket-chat-rest-client)  (community contributions)
- Chat-ops powered by Hubot: scalable horizontal app integration (early access)
- Massively scalable hosting and provisioning (beta testing now)
- Native Cross-Platform Desktop Application [Windows, macOS, or Linux](https://rocket.chat/)
- Mobile app for iPhone, iPad, and iPod touch [Download on App Store](https://geo.itunes.apple.com/us/app/rocket-chat/id1148741252?mt=8)
- Mobile app for Android phone, tablet, and TV stick [Available now on Google Play](https://play.google.com/store/apps/details?id=chat.rocket.android)
- Available on [Cloudron Store](https://cloudron.io/appstore.html#chat.rocket.cloudronapp)

## Roadmap

To see an up to date view of what we have planned, view our [milestones](https://github.com/RocketChat/Rocket.Chat/milestones).


## How it all started

Read about [how it all started](https://www.synopsys.com/blogs/software-security/rocket-chat-privately-hosted-chat-services/).

## Awards
[![InfoWorld Bossie Awards 2016 - Best Open Source Applications](https://raw.githubusercontent.com/Sing-Li/bbug/master/images/bossie.png)](http://www.infoworld.com/article/3122000/open-source-tools/bossie-awards-2016-the-best-open-source-applications.html#slide4)

[![Black Duck Open Source Rookie of the Year for 2015](https://raw.githubusercontent.com/Sing-Li/bbug/master/images/blackducksm.png)](https://info.blackducksoftware.com/OpenSourceRookies2015)

[![Softpedia 100% Free and Clean Award for 2017](https://raw.githubusercontent.com/Sing-Li/bbug/master/images/softpedia.gif)](http://www.softpedia.com/get/Internet/Chat/Other-Chat-Tools/Rocket-Chat.shtml#status)

## Issues

[GitHub Issues](https://github.com/RocketChat/Rocket.Chat/issues) are used to track bugs and tasks on the roadmap.

## Feature Requests

[RocketChat/feature-requests](https://github.com/RocketChat/feature-requests) is used to track Rocket.Chat feature requests and discussions. Click [here](https://github.com/RocketChat/feature-requests/issues/new?template=feature_request.md) to open a new feature request.
[Feature Request Forums](https://forums.rocket.chat/c/feature-requests) stores the historical archives of old feature requests (up to 2018).

### Stack Overflow

Please use the [Stack Overflow TAG](http://stackoverflow.com/questions/tagged/rocket.chat)

## Integrations

#### Hubot

The docker image is ready.
Everyone can start hacking the adapter code or launch his/her own bot within a few minutes now.
Please head over to the [Hubot Integration Project](https://github.com/RocketChat/hubot-rocketchat) for more information.


#### Chat-ops integrations powered by Hubot

Integrate your application with fly-in panels today! Early access is available for developers.

![Sample integration of a Drones Fleet Management System](https://raw.githubusercontent.com/Sing-Li/bbug/master/images/dronechatops.png)

#### Many, many, many more to come!

We are developing the APIs based on the competition, so stay tuned and you will see a lot happening here.

## Documentation

Check out [Rocket.Chat documentation](https://rocket.chat/docs/).

## License

Note that Rocket.Chat is distributed under the [MIT License](http://opensource.org/licenses/MIT).

# Development

## Quick start for code developers
Prerequisites:

* [Git](http://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Meteor](https://www.meteor.com/install)

> Meteor automatically installs a hidden [NodeJS v12](https://nodejs.org/download/release/v12.18.4/) and [MongoDB v4.2](https://docs.mongodb.com/manual/introduction/) to be used when you run your app in development mode using the `meteor` command.

Now just clone and start the app:

```sh
git clone https://github.com/RocketChat/Rocket.Chat.git
cd Rocket.Chat
meteor npm install
meteor npm start
```
For more detailed step-by-step, see our [quick start for developers](https://docs.rocket.chat/guides/developer/quick-start) docs.

To debug the server part, use [meteor debugging](https://docs.meteor.com/commandline.html#meteordebug). You should use Chrome for best debugging experience:

```sh
meteor debug
```
You'll find a nodejs icon in the developer console.

If you are not a developer and just want to run the server - see [deployment methods](https://rocket.chat/docs/installation/paas-deployments/).

## Branching Model

See [Branches and Releases](https://rocket.chat/docs/developer-guides/branches-and-releases/).

It is based on [Gitflow Workflow](http://nvie.com/posts/a-successful-git-branching-model/), reference section below is derived from Vincent Driessen at nvie.

See also this [Git Workflows Comparison](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) for more details.

## Translations
We are experimenting with [Lingohub](https://translate.lingohub.com/rocketchat/dashboard).
If you want to help, send an email to support at rocket.chat to be invited to the translation project.

## How to Contribute

Already a JavaScript developer? Familiar with Meteor? [Pick an issue](https://github.com/RocketChat/Rocket.Chat/labels/contrib%3A%20easy), push a PR and instantly become a member of Rocket.Chat's international contributors' community. For more information, check out our [Contributing Guide](.github/CONTRIBUTING.md) and our [Official Documentation for Contributors](https://rocket.chat/docs/contributing/).

A lot of work has already gone into Rocket.Chat, but we have much bigger plans for it!

### Contributor License Agreement

Please review and sign our CLA at https://cla-assistant.io/RocketChat/Rocket.Chat

# Credits

Thanks to our core team
[Aaron Ogle](https://github.com/geekgonecrazy),
[Bradley Hilton](https://github.com/Graywolf336),
[Diego Sampaio](https://github.com/sampaiodiego),
[Gabriel Engel](https://github.com/engelgabriel),
[Marcelo Schmidt](https://github.com/marceloschmidt),
[Rodrigo Nascimento](https://github.com/rodrigok),
[Sing Li](https://github.com/Sing-Li),
and hundreds of awesome [contributors](https://github.com/RocketChat/Rocket.Chat/graphs/contributors).

![JoyPixels](https://i.imgur.com/OrhYvLe.png)

Emoji provided graciously by [JoyPixels](https://www.joypixels.com/)

![BrowserStack](https://cloud.githubusercontent.com/assets/1986378/24772879/57d57b88-1ae9-11e7-98b4-4af824b47933.png)

Testing with [BrowserStack](https://www.browserstack.com)

![LingoHub](https://user-images.githubusercontent.com/20868078/69438584-0dd0e880-0d24-11ea-9127-de61dcfa6cd6.png)

Translations done with [LingoHub](https://www.lingohub.com)

# Donate

Rocket.Chat will be free forever, but you can help us speed up the development!

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=9MT88JJ9X4A6U&source=url)


[BountySource](https://www.bountysource.com/teams/rocketchat)
