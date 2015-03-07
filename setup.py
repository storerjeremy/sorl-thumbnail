# -*- encoding: utf8 -*-
from __future__ import unicode_literals

from setuptools import setup, find_packages
from setuptools.command.test import test


def get_module_meta(module_path):
    import re
 
    with open(module_path) as cakebet_meta:
        meta = cakebet_meta.read()
    return dict(re.findall('(?P<key>__.+__)\s=\s["\' ](?P<value>.+)["\' ]', meta))


class TestCommand(test):
    def run(self):
        from tests.runtests import runtests

        runtests()


meta = get_module_meta('thumbnail/__init__.py')

setup(
    name='python-thumbnail',
    version=meta['__version__'],
    description='Thumbnails for Python',
    long_description=open('README.rst').read(),
    author=meta['__author__'],
    author_email='mariocesar.c50@gmail.com',
    license=meta['__license__'],
    url='https://github.com/mariocesar/python-thumbnail',
    packages=find_packages(exclude=['tests', 'tests.*']),
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Multimedia :: Graphics',
        'Framework :: Django',
        'Framework :: Flask',
    ],
    cmdclass={"test": TestCommand},
)
