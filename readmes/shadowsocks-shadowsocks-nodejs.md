shadowsocks-nodejs
==================

[![NPM version]][NPM] [![Build Status]][Travis CI]

shadowsocks-nodejs is a node.js port of [shadowsocks].

**Deprecated; please use [Other versions].**

Many people are asking why. Here's why.

- https://github.com/shadowsocks/shadowsocks-nodejs/issues/35
- https://github.com/nodejs/node-v0.x-archive/issues/5949

The GC of node.js sucks.

Python version [handles 5000 connections with 50MB RAM](https://github.com/shadowsocks/shadowsocks/wiki/Optimizing-Shadowsocks) while node.js version
handles 100 connections with 300MB RAM. Why should we continue to support
node.js?


[Build Status]:    https://img.shields.io/travis/clowwindy/shadowsocks-nodejs/master.svg?style=flat
[NPM]:             https://www.npmjs.com/package/shadowsocks
[NPM version]:     https://img.shields.io/npm/v/shadowsocks.svg?style=flatp
[Travis CI]:       https://travis-ci.org/clowwindy/shadowsocks-nodejs
[shadowsocks]:     https://github.com/shadowsocks/shadowsocks
[Other versions]:  https://github.com/shadowsocks/shadowsocks/wiki/Ports-and-Clients
