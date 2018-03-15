# -*- coding: utf-8 -*-
# @Author: Cody Kochmann
# @Date:   2017-11-09 11:50:41
# @Last Modified 2018-03-15
# @Last Modified time: 2018-03-15 11:51:55

from distutils.core import setup

version = '2018.3.15'

setup(
  name = 'strict_functions',
  packages = ['strict_functions'], # this must be the same as the name above
  version = version,
  description = 'collection of helpful strict_functions that should have been in itertools',
  author = 'Cody Kochmann',
  author_email = 'kochmanncody@gmail.com',
  url = 'https://github.com/CodyKochmann/strict_functions',
  download_url = 'https://github.com/CodyKochmann/strict_functions/tarball/{}'.format(version),
  keywords = ['strict_functions', 'type', 'enforce', 'strict', 'restrict', 'strict defaults', 'defaults'],
  classifiers = [],
)
