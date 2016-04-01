logstash-easy
=============
[![PyPI](https://img.shields.io/pypi/dm/logstash-easy.svg)](https://pypi.python.org/pypi/logstash-easy)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/Fatal1ty/logstash_easy/master/LICENSE)

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

By default logging messages will be sent to `localhost:5000` but you can set environment variables `LOGSTASH_HOST`, `LOGSTASH_PORT` and `LOGSTASH_TAG` for tagging your application.
