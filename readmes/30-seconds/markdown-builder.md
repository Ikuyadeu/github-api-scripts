# Markdown builder for Node 
[![Build Status](https://api.travis-ci.org/30-seconds/markdown-builder.svg?branch=master)](https://travis-ci.org/30-seconds/markdown-builder)
![npm bundle size (minified + gzip)](https://img.shields.io/bundlephobia/minzip/markdown-builder.svg)
![npm](https://img.shields.io/npm/v/markdown-builder.svg)

> Official README builder for the 30-seconds projects.

## Usage
```bash
npm install --save markdown-builder
```

Using `markdown-builder` is quite easy:
```js
const markdown = require('markdown-builder');
const { headers } = markdown;

headers.hX(3, '3rd Header') // ### 3rd Header
```

## Example
**Check out [30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code)'s READMEs, they are automatically generated using `markdown-builder`**

## API

### Headers
Use the `h1`,`h2`,`h3`,`h4`,`h5`,`h6` or `hX` to generate a markdown header. Calling `hX` with a level above `6` returns a `h6` Header.

```js
const markdown = require('markdown-builder')
const { headers } = markdown

headers.h1('1st Header') // # 1st Header
headers.h2('2nd Header') // ## 2nd Header
headers.h3('3rd Header') // ### 3rd Header
headers.hX(5, '5th Header using hX') // ##### 5th Header using hX
```

### Emphasis
```js
const markdown = require('markdown-builder')
const { emphasis } = markdown

emphasis.b('bold text')
emphasis.i('italic text')
emphasis.s('strikethrough text')
```

### Lists
```js
const markdown = require('markdown-builder')
const { lists } = markdown

let a = ['Item 1', 'Item 2']
// ordered list
lists.ol(a)
// 1. Item 1
// 2. Item 2
lists.ol(a, (item) => item.toUpperCase()) // use callbacks to alter each item
// 1. ITEM 1
// 2. ITEM 2

// unordered List
lists.ul(a)
lists.ul(a, (item) => item.toUpperCase())
```

### Miscellaneous

```js
const markdown = require('markdown-builder')
const { misc } = markdown

// Images
let alt = 'image of lights', url = 'https://www.w3schools.com/w3css/img_lights.jpg', title = 'lights'
misc.image(alt, url)
misc.image(alt, url, title)

// Collapsible summary/details block
misc.collapsible('Summary', 'content');

// Github Anchor
misc.anchor('A header with /*() special-characters!'); // #a-header-with--special-characters

// Link
misc.link('Github', 'https://github.com/flxwu')

// horizontal rule
misc.hr()

```

**Collapsible**:

<details>
	<summary>Summary</summary>
	Content
</details>



#### A header with /*() special-characters!
