# 从零开始构建 JavaScript 技术栈

这里是[从零开始构建 JavaScript 技术栈](https://github.com/verekia/js-stack-from-scratch)的中文翻译版本。本教程内容比较浅，适合刚入门的初学者。

作者正在写[第二版](https://github.com/verekia/js-stack-from-scratch)，可以关注。

[![Build Status](https://travis-ci.org/pd4d10/js-stack-from-scratch.svg?branch=master)](https://travis-ci.org/pd4d10/js-stack-from-scratch) [![Join the chat at https://gitter.im/js-stack-from-scratch/Lobby](https://badges.gitter.im/js-stack-from-scratch/Lobby.svg)](https://gitter.im/js-stack-from-scratch/Lobby)

[![Yarn](/img/yarn.png)](https://yarnpkg.com/)
[![React](/img/react.png)](https://facebook.github.io/react/)
[![Gulp](/img/gulp.png)](http://gulpjs.com/)
[![Redux](/img/redux.png)](http://redux.js.org/)
[![ESLint](/img/eslint.png)](http://eslint.org/)
[![Webpack](/img/webpack.png)](https://webpack.github.io/)
[![Mocha](/img/mocha.png)](https://mochajs.org/)
[![Chai](/img/chai.png)](http://chaijs.com/)
[![Flow](/img/flow.png)](https://flowtype.org/)

欢迎阅读我的 JavaScript 教程：**从零开始构建 JavaScript 技术栈**

这是一个简单直接的 JavaScript 技术栈构建指南。在此之前，你需要掌握基本的编程知识和一些 JavaScript 基础。**本教程旨在将所有这些工具结合起来使用**，并为每个工具提供**最简单的示例**。 你可以把它当作*从零开始编写代码样板*的示范。

如果你只是想做一个简单的网页，有一些简单的 JS 交互，那么 Browserify/Webpack + Babel + jQuery 就足够了。如果你希望做的是有一定的规模的 web app，那么本教程非常适合你阅读。

本教程不会涉及这些技术的具体细节，因为目的只是让你学会使用它们。如果你想深入了解，可以查阅它们的文档，或者找其他的教程。

教程中提到的大部分技术栈都会用到 React。如果你是一个初学者，想学习 React，[create-react-app](https://github.com/facebookincubator/create-react-app) 是一个很好的选择，它可以帮你快速搭建起开发环境，所有的环境都配置好了。例如你刚加入一个使用 React 的团队，希望快速上手，我非常推荐你使用它。不过在本教程中，不会有任何预先配置好的东西，因为我希望你理解每一行配置背后真实发生了什么。

每个章节都有代码示例，可以使用命令 `yarn && yarn start` 或 `npm install && npm start` 来运行。建议按照每章的说明，**一步一步**从零开始写所有的代码。

**每一章都包含前一章的代码**，所以如果你只是想找一个代码样板或脚手架，直接看最后一章的示例代码即可。

注意：章节的顺序不一定是最有利于学习的顺序。 例如，测试和类型检查可以在引入 React 之前完成。 移动章节或编辑过去的章节比较困难，因为我同时需要将这些更改应用到后续加入的章节。 如果所有的内容都定下来了，我相信可以有更好的方式重新组织他们。

本教程的代码可以运行在 Linux，macOS 和 Windows 下。

## 目录

[1 - Node, NPM, Yarn 和 package.json](/tutorial/1-node-npm-yarn-package-json)

[2 - 包的安装与使用](/tutorial/2-packages)

[3 - 使用 Babel 和 Gulp 配置 ES6 开发环境](/tutorial/3-es6-babel-gulp)

[4 - 使用 ES6 中的 class](/tutorial/4-es6-syntax-class)

[5 - ES6 模块系统](/tutorial/5-es6-modules-syntax)

[6 - 代码检查工具 ESLint](/tutorial/6-eslint)

[7 - 前端打包工具 Webpack](/tutorial/7-client-webpack)

[8 - React](/tutorial/8-react)

[9 - Redux](/tutorial/9-redux)

[10 - Immutable JS 和 Redux 的改进方法](/tutorial/10-immutable-redux-improvements)

[11 - 使用 Mocha, Chai 和 Sinon 进行测试](/tutorial/11-testing-mocha-chai-sinon)

[12 - 使用 Flow 进行类型检查](/tutorial/12-flow)

## 即将加入以下内容

部署/开发环境，Express，React 路由管理，服务端渲染，样式，React 测试工具 Enzyme，Git Hooks。

## 翻译

- [中文](https://github.com/pd4d10/js-stack-from-scratch) by [@pd4d10](http://github.com/pd4d10)
- [Italiano](https://github.com/fbertone/js-stack-from-scratch) by [Fabrizio Bertone](https://github.com/fbertone)
- [日本語](https://github.com/takahashim/js-stack-from-scratch) by [@takahashim](https://github.com/takahashim)
- [Русский](https://github.com/UsulPro/js-stack-from-scratch) by [React Theming](https://github.com/sm-react/react-theming)
- [ไทย](https://github.com/MicroBenz/js-stack-from-scratch) by [MicroBenz](https://github.com/MicroBenz)

## Credits

Created by [@verekia](https://twitter.com/verekia) – [verekia.com](http://verekia.com/).

License: MIT
