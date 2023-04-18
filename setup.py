#!/usr/bin/env python
from setuptools import setup, find_packages

from internationalize import __version__

setup(keywords=['i18n', 'internationalize'],
      version=__version__,
      packages=find_packages(include=['internationalize']),
      tests_require=["nose2", "coverage", "nose2[coverage_plugin]"],
      test_suite='nose2.collector.collector',
      python_requires='!=2.*,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*',
      )