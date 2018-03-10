# -*- coding: utf-8 -*-
# @Author: Cody Kochmann
# @Date:   2018-03-10 08:25:11
# @Last Modified by:   Cody Kochmann
# @Last Modified time: 2018-03-10 08:26:00

from noglobals import noglobals

@noglobals
def attempt(fn, default_output=None):
    ''' attempt running a function in a try block without raising exceptions '''
    assert callable(fn), 'generators.inline_tools.attempt needs fn to be a callable function'
    try:
        return fn()
    except:
        return default_output

