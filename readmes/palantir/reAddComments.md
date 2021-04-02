# reAddComments

> Re-add comments to generated files from their CoffeeScript source files via sourcemap.

## Getting Started

**reAddComments** takes a sourcemap (.map) file, looks at the generated JavaScript file and the CoffeeScript source file(s) it's associated with, and adds comments from the sources to the generated file.

If multiple .map are passed in one invocation, **reAddComments** will process each one individually.  Common usage may be `reAddComments lib/*.map`.

**reAddComments** is only as accurate as the sourcemaps it's given, so it occassionally misplaces comments.  If you are using it to migrate a code base away from CoffeeScript, you should manually review the altered files.


## As A Library

**reAddComments** exports a single function,

###reAddComments(generatedCode: string, sourceCode: string, mapdict: {})
The mapdict parameter should be a json object equivalent to a .map file between the
generatedCode and the sourceCode.  The actual filenames/sourceRoot defined in the mapdict
is ignored, as the map is assumed to be between the generatedCode and sourceCode arguments.


## Release History
_(Nothing yet)_

## Authors #

[Jared Pochtar](https://github.com/jaredp)

---

Copyright 2014 Palantir Technologies

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
