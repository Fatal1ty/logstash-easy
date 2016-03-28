#!/usr/bin/env python

from distutils.core import setup

setup(
    name='logstash-easy',
    version='0.1',
    description='Easy to use logstash logging handler wrapper',
    platforms="all",
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python',
    ],
    author='Alexander Tikhonov',
    py_modules=['logstash_easy'],
    install_requires=[
        'python-logstash',
    ]
)
