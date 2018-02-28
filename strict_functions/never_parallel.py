# -*- coding: utf-8 -*-
# @Author: Cody Kochmann
# @Date:   2018-02-28 14:14:33
# @Last Modified 2018-02-28e>
# @Last Modified time: 2018-02-28 14:17:04

from threading import RLock, Lock

class never_parallel(object):
    ''' this function decorator locks a function until it finishes to protect
        functions that are not thread safe. '''
    def __init__(self, fn, use_rlock=False):
        self.fn = fn
        self.lock = (RLock if use_rlock else Lock)()

    def __call__(self, *args, **kwargs):
        with self.lock:
            return self.fn(*args, **kwargs)
