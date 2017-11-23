# -*- coding: utf-8 -*-
# @Author: Cody Kochmann
# @Date:   2017-11-22 13:53:53
# @Last Modified 2017-11-22
# @Last Modified time: 2017-11-22 14:25:56

import builtins

def noglobals(f):
    """ decorator for functions that dont get access to globals """
    return type(f)(
        f.func_code,
        {'__builtins__': builtins},
        f.func_name,
        f.func_defaults,
        f.func_closure
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
