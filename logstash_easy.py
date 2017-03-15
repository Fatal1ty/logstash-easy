import logging
from os import environ as env

import logstash


class TCPLogstashHandler(logstash.TCPLogstashHandler):
    def __init__(self, app_name, *args, **kwargs):
        self.app_name = app_name
        super(TCPLogstashHandler, self).__init__(*args, **kwargs)

    def makePickle(self, record):
        if self.app_name:
            record.app_name = self.app_name
        return super(TCPLogstashHandler, self).makePickle(record)


class UDPLogstashHandler(logstash.UDPLogstashHandler):
    def __init__(self, app_name, *args, **kwargs):
        self.app_name = app_name
        super(UDPLogstashHandler, self).__init__(*args, **kwargs)

    def makePickle(self, record):
        if self.app_name:
            record.app_name = self.app_name
        return super(UDPLogstashHandler, self).makePickle(record)


def init_logstash():
    proto_classes = dict(UDP=UDPLogstashHandler, TCP=TCPLogstashHandler)
    handler_class = proto_classes.get(env.get('LOGSTASH_PROTO', 'UDP'))
    if handler_class:
        root_logger = logging.getLogger()
        app_name = env.get('LOGSTASH_APP_NAME')
        tag = env.get('LOGSTASH_TAG')
        handler = handler_class(
            app_name=app_name,
            host=env.get('LOGSTASH_HOST', 'localhost'),
            port=int(env.get('LOGSTASH_PORT', 5000)),
            tags=[tag] if tag else None,
            version=1
        )
        root_logger.addHandler(handler)


def patch():
    original_basicConfig = logging.basicConfig

    def basicConfig(**kwargs):
        original_basicConfig(**kwargs)
        init_logstash()

    logging.basicConfig = basicConfig


patch()
