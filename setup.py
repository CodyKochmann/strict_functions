# -*- coding: utf-8 -*-
# @Author: Cody Kochmann
# @Date:   2017-11-09 11:50:41
# @Last Modified 2017-11-22
# @Last Modified time: 2017-11-22 21:56:18

from distutils.core import setup

setup(
  name = 'strict_functions',
  packages = ['strict_functions'], # this must be the same as the name above
  version = '2017.2.6',
  description = 'collection of helpful strict_functions that should have been in itertools',
  author = 'Cody Kochmann',
  author_email = 'kochmanncody@gmail.com',
  install_requires = ['cffi'],
  url = 'https://github.com/CodyKochmann/strict_functions',
  download_url = 'https://github.com/CodyKochmann/strict_functions/tarball/2017.2.6',
  keywords = ['strict_functions', 'type', 'enforce', 'strict', 'restrict', 'strict defaults', 'defaults'],
  classifiers = [],
)
