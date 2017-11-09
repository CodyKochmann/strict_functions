# -*- coding: utf-8 -*-
# @Author: cody kochmann
# @Date:   2016-10-14 13:22:24
# @Last Modified 2016-10-14
# @Last Modified time: 2016-10-14 13:27:57

class output_type(object):
    # control how functions output data
    # by: Cody Kochmann
    def __init__(self, *specified_type):
        assert all(type(list) is type(i) for i in specified_type), "output type must be a <type 'type'>"
        self.specified_type = specified_type[0]
    def __call__(self,f):
        def wrapper(*args, **kwargs):
            out = f(*args, **kwargs)
            assert isinstance(out, self.specified_type),\
                "{} has to return a {} instead of a {}".format(
                    f.__name__,
                    self.specified_type.__name__,
                    type(out).__name__)
            return out
        return wrapper
