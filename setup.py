#!/usr/bin/env python

from distutils.core import setup

setup(
    name='logstash-easy',
    version='0.2',
    description='Very easy to use Logstash logging handler',
    platforms="all",
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python',
    ],
    license='MIT',
    author='Alexander Tikhonov',
    author_email='random.gauss@gmail.com',
    url='https://github.com/Fatal1ty/logstash_easy',
    py_modules=['logstash_easy'],
    install_requires=[
        'python-logstash',
    ]
)
