logstash-easy
=============

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
