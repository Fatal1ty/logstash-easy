#!/usr/bin/env python

from distutils.core import setup

setup(
    name='logstash-easy',
    version='0.3',
    description='Very easy to use Logstash logging handler',
    long_description=open('README.rst').read(),
    platforms='all',
    license='MIT',
    author='Alexander Tikhonov',
    author_email='random.gauss@gmail.com',
    url='https://github.com/Fatal1ty/logstash_easy',
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: Implementation :: CPython',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System',
          'Topic :: System :: Software Distribution',
          ],
    py_modules=['logstash_easy'],
    install_requires=[
        'python-logstash',
    ]
)
