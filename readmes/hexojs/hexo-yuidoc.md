# hexo-yuidoc

Generate [YUIDoc] with Hexo.

## Deprecated

It's not compatible with Hexo 3.

## Install

``` bash
$ npm install hexo-yuidoc --save
```

## Usage

### Requirements

You have to install [YUIDoc] first.

``` bash
$ npm install yuidocjs -g
```

### Generating

Generate raw data with YUIDoc first. Then, move `data.json` to `source/_yuidoc` folder. You can rename `data.json` to whatever you like. For example:

```
index.json => /api/classes/Class.html
foo.json => /api/foo/classes/Foo.html
```

### Templates

You have to at least add two templates to the `layout` folder of the theme:

- `api/class`
- `api/module`

You can get the model from `site.yuidoc` and get the name of current yuidoc from `page.yuidoc_name` in templates.

### Helpers

#### yuidoc_type

Gets the link of specified data types. You can use a string or an array. Multiple types will be separated by `|`. Besides classes in the database, you can also use [native types](https://github.com/hexojs/hexo-yuidoc/blob/master/lib/helpers.js#L11).

```
<%- yuidoc_type('String') %>
<%- yuidoc_type(['String', 'Array']) %>
```

#### yuidoc_params

Generates a parameter list.

```
<%- yuidoc_params(params) %>
```

#### get_current_yuidoc

```
<% get_current_yuidoc() %>
```

### Tags

You can use all tags and filters in your documentation.

#### crosslink

You can use `crosslink` to cross-reference other classes.

```
{% crosslink class/item:[type] [link text] %}
```

## Options

You can configure this plugin in `_config.yml`.

``` yaml
yuidoc_dir: api
```

- **yuidoc_dir** - Where generated files will be saved (Default: api)

[YUIDoc]: http://yui.github.io/yuidoc/
