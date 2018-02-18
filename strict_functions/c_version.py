# -*- coding: utf-8 -*-
# @Author: Cody Kochmann
# @Date:   2018-02-06 13:07:06
# @Last Modified 2018-02-06
# @Last Modified time: 2018-02-17 21:25:36

from functools import wraps
from os import listdir, remove
from sys import version_info
from cffi import FFI
import logging
if version_info>=(3,4):
    from importlib import reload
elif version_info>=(3,0):
    from imp import reload
from strict_globals import strict_globals

class c_version(object):
    tmp_module_name = '_tmp_c_module'

    @property
    def type(self):
        return self.c_src.split(' ')[0]

    @property
    def name(self):
        return [i for i in self.c_src.replace('(',' ').split(' ') if len(i)][1]

    @property
    def cdef(self):
        return '{};'.format(self.c_src.split('{')[0])

    @property
    def args(self):
        return [i.strip() for i in self.c_src.split('(')[1].split(')')[0].split(',')]

    @property
    def arg_types(self):
        return [i.split(' ')[0] for i in self.args]

    @staticmethod
    def cleanup_files():
        for i in listdir('.'):
            if i.startswith(c_version.tmp_module_name):
                remove(i)

    def compile(self):
        try:
            ffi = FFI()
            ffi.cdef(self.cdef)
            ffi.set_source(self.tmp_module_name, self.c_src)
            ffi.compile(verbose=self.verbose)
            from _tmp_c_module import lib
            try:
                reload(_tmp_c_module)
            except: # fuck you marcin!!!
                pass
            @strict_globals(
                fn=getattr(lib, self.name),
                cast=ffi.cast,
                types=self.arg_types
            )
            def output(*args):
                return fn(*(cast(_type, arg) for _type, arg in zip(types, args)))
        except Exception as ex:
            logging.exception(ex)
            return None
        else:
            return output
        finally:
            self.cleanup_files()


    def __init__(self, c_src, verbose=False):
        self.c_src = c_src.strip()
        self.verbose = verbose
        self.compiled = self.compile()

    def __call__(self, fn):
        @wraps(fn)
        @strict_globals(compiled_version=self.compiled)
        def wrapper(*args):
            return compiled_version(*args)
        return fn if self.compiled is None else wrapper


if __name__ == '__main__':
    @c_version("""
    int add_numbers(int a, int b)
    {
      int result;
      result = a+b;
      return result;
    }
    """)
    def add_numbers(a, b):
        return a+b

    for i in range(4294967295-10, 4294967295+10):
        print(add_numbers(i,3))
