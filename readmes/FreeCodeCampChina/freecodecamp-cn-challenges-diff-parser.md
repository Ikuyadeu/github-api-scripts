![Node.js](https://jaywcjlove.github.io/sb/ico/nodejs.svg)
![NodeVersion](https://img.shields.io/badge/node-%3E=8.11.3-brightgreen.svg)
-----
# freecodecamp-cn-challenges-diff-parser
[![English](https://jaywcjlove.github.io/sb/lang/english.svg)](https://github.com/FreeCodeCampChina/freecodecamp-cn-challenges-diff-parser) [![Chinese](https://jaywcjlove.github.io/sb/lang/chinese.svg)](./README-CN.md)
-----
## Intro
`freecodecamp-cn-challenges-diff-parser` is a simple tool, primarily targeted for freeCodeCamp China developers, contributors and maintainers. 
## How it works
1. It takes in two commits hash for comparison. By default, one is from local history, while the other one is from the latest `freecodecamp/curriculum` `dev` branch.
    - **Note that the earlier commit (i.e. the one from local history) is currently static. Will use the commit off which the latest translation is based from tag tree**
2. After retrieving the diff of two commits, iterate through the related `.json` challenge files, looking for id/title corresponding to the diffs. Then, generate output.
3. The output includes the following information:
    - File path (`new`, `old` or both) of modified challenges 
    - `id` or `title` of modified challenges
    - Line changes (old code and new cold) of modified challenges, resembles that of `git diff` (alternative)

# Install
## Global
// TODO: Publish via npm
## Local (dev)
### Clone repositories
1. `git clone https://github.com/FreeCodeCampChina/curriculum-cn`
2. `git clone https://github.com/FreeCodeCampChina/freecodecamp-cn-challenges-diff-parser`
### Install dependencies of diff-parser
1. `cd freecodecamp-cn-challenges-diff-parser`
2. `npm i` or `yarn install`
### Create local dev-track-en branch of curriculum-cn repo
**!important**
1. `cd ../curriculum-cn`
2. `git checkout -b dev-track-en origin/dev-track-en`
### Note that either folder structure below **should** work
- Diff parser is within the same level of curriculum-cn
```text
.
├── curriculum-cn
|   ├── challenges/
|   └── index.js
├── freecodecamp-cn-challenges-diff-parser
|   ├── lib/
|   └── index.js
|
...
```

- Diff parser is within the same level of curriculum-cn parent folder `cn` (has to be `cn`)
```text
.
├── cn
|   ├── curriculum-cn/
|       ├── challenges/
|       └── index.js
|   ...
├── freecodecamp-cn-challenges-diff-parser
|   ├── lib/
|   └── index.js
|
...
```

# Usage
## As global package
// TODO: Publish via npm
## Under freecodecamp-cn-challenges-diff-parser directory
```bash
node index.js
```
## Under curriculum-cn directory
```bash
node ${path_to_freecodecamp-cn-challenges-diff-parser}/index.js
```
## Flags/Options
```bash
node index.js [--type] [--path] [--debug]
```
### --type
- Determine output type, possible values are `title` and `id`
- Defaults to `title` when not passed in
- **Note: when type is given, detailed line changes are suppressed (consider `--type` as `--type-only`)**
### --path
- Determine output path type, possible values are `new` and `old`
- Defaults to 'both' when not passed in
### --debug
- Determine whether to show line number for each hunk of code change

## Example
- `node index.js` will output:
    - Detailed line changes
    - Title corresponding to the line changes
    - Both new and old file path corresponding to the line changes
- `node index.js --type=id` will output:
    - ID corresponding to the line changes
    - Both new and old file path corresponding to the line changes
- `node index.js --type=title --path=new` will output:
    - Title corresponding to the line changes
    - New file path corresponding to the line changes
- `node index.js --type=title --debug` will output:
    - Title corresponding to the line changes
    - Both new and old file path corresponding to the line changes
    - Line number corresponding to the line changes of both old file path and new file path

# Data Structure
- `DiffObject` object for output
```yaml
newPath: String<Path>
oldPath: String<Path>
oldFile: Array<String>    # The old JSON file split with \n
newFile: Array<String>    # The new JSON file split with \n
diffs: Array<ParsedHunk>  # Array that contains all parsed diff content
```

- `ParsedHunk`
```yaml
oldStart: Number         # The line number (of old json file) where change happens
newStart: Number         # The line number (of old json file) where change happens
data: Array<DiffContent>
```

- `DiffContent`
```yaml
sign: String     # Possible values are ' ', '+' or '-', where ' ' denotes unchanged line of code, '+' denotes code addition and '-' denotes code subtraction
content: String  # Line diff
```

# TODO
- [ ] Add eslint
- [ ] Verify Node.js version 6.3.0
- [ ] Verify corresponding NPM version
- [ ] Generate HTML output, pug?
- [ ] Add babel
- [ ] Set up build process
