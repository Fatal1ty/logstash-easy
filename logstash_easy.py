import logging
from os import environ as env

import logstash


def init_logstash():
    proto_classes = dict(UDP=logstash.UDPLogstashHandler,
                         TCP=logstash.TCPLogstashHandler)
    handler_class = proto_classes.get(env.get('LOGSTASH_PROTO', 'UDP'))
    if handler_class:
        root_logger = logging.getLogger()
        app_name = env.get('LOGSTASH_TAG')
        handler = handler_class(env.get('LOGSTASH_HOST', 'localhost'),
                                int(env.get('LOGSTASH_PORT', 5000)),
                                tags=[app_name] if app_name else None,
                                version=1)
        root_logger.addHandler(handler)


def patch():
    original_basicConfig = logging.basicConfig

    def basicConfig(**kwargs):
        original_basicConfig(**kwargs)
        init_logstash()

    logging.basicConfig = basicConfig


patch()
