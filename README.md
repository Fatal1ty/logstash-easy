logstash-easy
=============
[![PyPI](https://img.shields.io/pypi/dm/logstash-easy.svg?maxAge=2592000)](https://pypi.python.org/pypi/logstash-easy)
[![PyPI](https://img.shields.io/pypi/v/logstash-easy.svg?maxAge=2592000)](https://pypi.python.org/pypi/logstash-easy)
[![PyPI](https://img.shields.io/pypi/pyversions/logstash-easy.svg?maxAge=2592000)](https://pypi.python.org/pypi/logstash-easy)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?maxAge=2592000)](https://raw.githubusercontent.com/Fatal1ty/logstash_easy/master/LICENSE)

Very easy to use Logstash logging handler.

Installation
============

Install via pip:

```
    pip install logstash-easy
```

Usage
=====

Just write one line of code and enjoy:

```python
    import logstash_easy
```

By default logging messages will be sent to `localhost:5000` but you can set environment variables `LOGSTASH_HOST`, `LOGSTASH_PORT` and `LOGSTASH_TAG` for tagging your application. If you define `LOGSTASH_APP_NAME` variable then `app_name` field will be added to all logging messages (it can be used for creating Elasticsearch indices per application).
