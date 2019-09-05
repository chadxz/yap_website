# yap_website

[![Build Status][Build Status Image]][Build Status Link]
[![Codecov][Codecov Image]][Codecov Link]

[Build Status Image]: https://travis-ci.org/chadxz/yap_website.svg?branch=master
[Build Status Link]: https://travis-ci.org/chadxz/yap_website
[Codecov Image]: https://codecov.io/gh/chadxz/yap_website/branch/master/graph/badge.svg
[Codecov Link]: https://codecov.io/gh/chadxz/yap_website

Yet another personal website for me to fiddle with different things.

This is a revision of my typical personal website project that displays
data about me from around the web. With this version I combined the frontend
and backend into a single application instead of hosting them separately.

### getting started

The following instructions are for a Mac.

Requires [python 3](https://docs.python-guide.org/starting/install3/osx/):
`brew install python`

Then,

```shell
$ cp config/.secrets.toml.example config/.secrets.toml
```
... and populate the secrets. You'll need a pinboard account, a last.fm api
account, and a pocket account. 

Then,

```shell
$ make dev
```

... which will start the dev server in watch mode. The url will be printed in
the console.

### prior art

See [my-api](https://github.com/chadxz/my-api) and
[personal-site-angular](https://github.com/chadxz/personal-site-angular). 
