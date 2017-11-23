# -*- coding: utf-8 -*-
# @Author: Cody Kochmann
# @Date:   2017-11-22 21:05:34
# @Last Modified 2017-11-22
# @Last Modified time: 2017-11-22 21:45:39

from functools import wraps

class on_fail(object):
    def __init__(self, output_on_fail, logger=None):
        assert logger is None or callable(logger), 'on_fail-logger needs to be a callable function, not {}'.format(logger)
        self.output_on_fail = output_on_fail
        self.logger = logger

    def __call__(self, fn):
        @wraps(fn)
        def wrapper(*a, **k):
            try:
                return fn(*a, **k)
            except Exception as ex:
                if self.logger is not None:
                    self.logger(ex)
                return self.output_on_fail
        return wrapper


if __name__ == '__main__':
    from logging import warning

    @on_fail(None)
    def test1(a,b):
        return a/b

    print(test1(3.0, 5))
    print(test1(3.0, 0))

    @on_fail(None, warning)
    def test2(a,b):
        return a/b

    print(test2(3.0, 5))
    print(test2(3.0, 0))

