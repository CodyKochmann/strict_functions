# -*- coding: utf-8 -*-
# @Author: Cody Kochmann
# @Date:   2017-11-09 11:50:41
# @Last Modified 2018-03-15
# @Last Modified time: 2019-09-02 12:41:32

from distutils.core import setup

version = '2019.9.2.1'

setup(
  name = 'strict_functions',
  packages = ['strict_functions'], # this must be the same as the name above
  version = version,
  description = 'Decorators for function scope control, overloading, type safety, thread safety, cache control, tracing and even self awareness!',
  author = 'Cody Kochmann',
  author_email = 'kochmanncody@gmail.com',
  url = 'https://github.com/CodyKochmann/strict_functions',
  download_url = 'https://github.com/CodyKochmann/strict_functions/tarball/{}'.format(version),
  keywords = ['strict_functions', 'scope', 'overload', 'overloading', 'type', 'enforce', 'strict', 'restrict', 'strict defaults', 'defaults'],
  classifiers = [],
)
