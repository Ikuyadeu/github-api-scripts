omniauth-sso-cookie
=====================

[![Build Status](https://travis-ci.org/cdman/omniauth-sso-cookie.png?branch=master)](https://travis-ci.org/cdman/omniauth-sso-cookie)
[![Code Climate](https://codeclimate.com/github/cdman/omniauth-sso-cookie.png)](https://codeclimate.com/github/cdman/omniauth-sso-cookie)
[![Dependency Status](https://gemnasium.com/cdman/omniauth-sso-cookie.png)](https://gemnasium.com/cdman/omniauth-sso-cookie)

Ruby Omniauth strategy for authenticating using a cookie encrypted with a shared secret.

The secret should be in JSON format and encrypted with AES-256-CBC (with PKCS#7 padding) and authenticated with a SHA-256 HMAC.

See examples/generate-cookie.py for an example as to how such a cookie can be generated.

This code is available under the Apache 2.0 License.

