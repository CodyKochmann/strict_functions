# -*- coding: utf-8 -*-
# @Author: Cody Kochmann
# @Date:   2018-03-05 10:29:26
# @Last Modified 2018-03-05e>
# @Last Modified time: 2018-03-05 10:31:13

def force_assertions():
    ''' running this function will ensure the code is running with assertions
        enabled since python has a flag that disables all assertions
    '''
    try:
        assert False, 'this is suppose to fail'
        exit("Error: enable assertions to use {}".format(__file__))
    except AssertionError:
        pass
