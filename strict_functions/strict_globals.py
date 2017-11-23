# -*- coding: utf-8 -*-
# @Author: Cody Kochmann
# @Date:   2017-11-22 14:00:48
# @Last Modified 2017-11-22
# @Last Modified time: 2017-11-22 21:54:34

import builtins
from types import FunctionType

class strict_globals(object):
    ''' this is a decorator that allows you to define exactly what global variables it is allowed to access '''
    def __init__(self, __no_builtins=False, **_globals):
        assert type(__no_builtins) == bool, '__no_builtins needs to be a boolean, received: {}'.format(type(__no_builtins))
        if __no_builtins == False: # and '__builtins__' not in _globals: # i know, double negative, but __no_builtins is a good external option
            _globals['__builtins__'] = builtins
        self.globals = _globals

    def __call__(self, fn):
        assert callable(fn), 'strict_globals needs to be used on a callable function'
        assert hasattr(fn, '__code__') or hasattr(fn, 'func_code'), 'strict_globals only works on functions with a __code__ or func_code attribute'
        return FunctionType(
            getattr(fn, 'func_code', getattr(fn, '__code__')),
            self.globals,
            getattr(fn, 'func_name', getattr(fn, '__name__')),
            getattr(fn, 'func_defaults', getattr(fn, '__defaults__')),
            getattr(fn, 'func_closure', getattr(fn, '__closure__'))
        )

if __name__ == '__main__':
    from logging import warning

    a = 6
    b = 7

    def not_strict_globals(i):
        return sum((i,a,b))

    print(not_strict_globals(9))

    @strict_globals(a=a, b=b)
    def with_all_strict_globals(i):
        return sum((i,a,b))

    print(with_all_strict_globals(9))

    @strict_globals(a=a)
    def with_one_missing_strict_global(i):
        return sum((i,a,b))

    try:
        print(with_one_missing_strict_global(9))
    except Exception as e:
        warning(e)
