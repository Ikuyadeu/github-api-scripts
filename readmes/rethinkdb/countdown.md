Countdown
=========

*Note*: This code is ancient.  It's probably non-working.  Its usage of the
Github API seems to be outdated.  Its code mentions that
`table_create` is not available yet.  You should view this repo as
historically (un)interesting.

Installation
============

If you don't already have RethinkDB, [go download](http://rethinkdb.com/docs/install) and install it.

Install the required libraries:
```
npm install -g less
npm install -g coffee-script
pip install -r requirements.txt
```

Deploying
=========

Countdown uses the CherryPy WSGI server, as it's lightweight and easy to deploy. Start an instance of RethinkDB, and then launch Countdown with:

```
python countdown.py
```

If you want to deploy this on port 80, you can use nginx (or other web server) as a proxy. Here's an example nginx config:
```
server {
        listen          80;
        server_name     $hostname;

        location / {
            proxy_pass http://127.0.0.1:8888/;
        }
}

```

License
=======
Countdown is licensed under the MIT license: http://opensource.org/licenses/mit-license.php
