# pups

Simple YAML--based bootstrapper

## Installation

Add this line to your application's Gemfile:

    gem 'pups'

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install pups

## Usage

pups is a small library that allows you to automate the process of creating Unix images.

Example:

```
# somefile.yaml
params:
  hello: hello world

run:
  - exec: /bin/bash -c 'echo $hello >> hello'
```

Running: `pups somefile.yaml` will execute the shell script resulting in a file called "hello" with the contents "hello world".

### Features

#### Environment Variables

By default, pups automatically imports your environment variables and includes them as params.

```
# In bash
export SECRET_KEY="secret value"

# In somefile.yaml
run:
  - exec: echo "$SECRET_KEY"
```

Running the above code with pups will produce `secret value`.

#### Execution

Run multiple commands in one path:

```
run:
  - exec:
      cd: some/path
      cmd:
        - echo 1
        - echo 2
```

Run commands in the background (for services etc)

```
run:
  - exec:
      cmd: /usr/bin/sshd
      background: true
```

Suppress exceptions on certain commands

```
run:
  - exec:
      cmd: /test
      raise_on_fail: false
```

#### Replacements:

```
run:
  - replace:
      filename: "/etc/redis/redis.conf"
      from: /^pidfile.*$/
      to: ""
```

Will substitute the regex with blank, removing the pidfile line

```
run:
  - replace:
      filename: "/etc/nginx/conf.d/discourse.conf"
      from: /upstream[^\}]+\}/m
      to: "upstream discourse {
        server 127.0.0.1:3000;
      }"
```

Additional params:

Global replace (as opposed to first match)
```
global: true
```

#### Hooks

Execute commands before and after a specific command by defining a hook.

```
run
  - exec:
      hook: hello
      cmd: echo 'Hello'

hooks:
  before_hello:
    - exec:
        cmd: echo 'Starting...'

  after_hello:
    - exec:
        cmd: echo 'World'
```

#### Merge yaml files

```
home: /var/www/my_app
params:
  database_yml:
    production:
      username: discourse
      password: foo

run:
  - merge: $home/config/database.yml $database_yml

```

Will merge the yaml file with the inline contents.

#### A common environment

This is implemented in discourse_docker's launcher, not in pups - therefore it does not work in standalone pups.

```
env:
   MY_ENV: 1
```

All executions will get this environment set up


## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
