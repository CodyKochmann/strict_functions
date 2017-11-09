# -*- coding: utf-8 -*-
# @Author: Cody Kochmann
# @Date:   2017-11-09 11:29:48
# @Last Modified 2017-11-09
# @Last Modified time: 2017-11-09 11:48:38

from functools import wraps
import inspect

def _get_default_args(func):
    """
    returns a dictionary of arg_name:default_values for the input function
    """
    args, varargs, keywords, defaults = inspect.getargspec(func)
    print(args)
    return dict(zip(reversed(args), reversed(defaults)))

def _get_arg_names(func):
    ''' this returns the arg names since dictionaries dont guarantee order '''
    args, varargs, keywords, defaults = inspect.getargspec(func)
    return(tuple(args))

def strict_defaults(fn):
    ''' use this decorator to enforce type checking on functions based on the function's defaults '''
    @wraps(fn)
    def wrapper(*args, **kwargs):
        defaults = _get_default_args(fn)
        # dictionary that holds each default type
        needed_types={
            key:type(defaults[key]) for key in defaults
        }
        # ordered tuple of the function's argument names
        arg_names=_get_arg_names(fn)
        assert not len(arg_names) - len(fn.__defaults__), '{} needs default variables on all arguments'.format(fn.__name__)
        # merge args to kwargs for easy parsing
        for i in range(len(args)):
            if args[i] not in kwargs.keys():
                kwargs[arg_names[i]]=args[i]
        # assert that theyre all the correct type
        for name in needed_types:
            # do them all seperately so you can show what went wrong
            assert  isinstance(kwargs[name],needed_types[name]), 'got {} and expected a {}'.format(kwargs[name],needed_types[name])
        # return the refined results
        return fn(**kwargs)
    return wrapper

if __name__ == '__main__':
    @strict_defaults
    def test(a='',b=0):
        pass

    test('hello', 9)
    test('hello', '9')
