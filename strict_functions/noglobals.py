# -*- coding: utf-8 -*-
# @Author: Cody Kochmann
# @Date:   2017-11-22 13:53:53
# @Last Modified 2017-11-22
# @Last Modified time: 2017-11-22 21:55:39

import builtins

def noglobals(fn):
    """ decorator for functions that dont get access to globals """
    return type(fn)(
        getattr(fn, 'func_code', getattr(fn, '__code__')),
        {'__builtins__': builtins},
        getattr(fn, 'func_name', getattr(fn, '__name__')),
        getattr(fn, 'func_defaults', getattr(fn, '__defaults__')),
        getattr(fn, 'func_closure', getattr(fn, '__closure__'))
    )


if __name__ == '__main__':
    from logging import warning

    i = 5

    def with_globals(a):
        return a*i

    print(with_globals(9))

    @noglobals
    def without_globals(a):
        return a*i

    try:
        print(without_globals(9))
    except Exception as e:
        warning(e)
