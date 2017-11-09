# -*- coding: utf-8 -*-
# @Author: cody kochmann
# @Date:   2016-10-14 13:23:20
# @Last Modified 2016-10-14
# @Last Modified time: 2016-10-14 13:28:02

class input_types(object):
    # control how functions take data in
    # by: Cody Kochmann
    def __init__(self, *listed_types, **named_types):
        if(len(listed_types)):
            assert all(type(list) is type(i) for i in listed_types), "input_types needs types as arguments"
            self.listed_types = listed_types
        if(len(named_types)):
            self.named_types = named_types

    def __call__(self,f):
        def wrapper(*args, **kwargs):
            if('listed_types' in self.__dict__):
                for i in range(len(self.listed_types)):
                    assert isinstance(args[i], self.listed_types[i]), "{} needs arg {} to be a {} not a {}".format(
                        f.__name__,
                        i+1,
                        self.listed_types[i].__name__,
                        type(args[i]).__name__
                        )
            if('named_types' in self.__dict__):
                for n in self.named_types:
                    assert n in kwargs, "{} missing specified argument '{}'".format(f.__name__,n)
                    assert self.named_types[n] == type(kwargs[n]), "{} needs '{}' arg to be a {} not a {}".format(
                        f.__name__,
                        n,
                        self.named_types[n].__name__,
                        type(kwargs[n]).__name__
                        )
            return f(*args, **kwargs)
        return wrapper
