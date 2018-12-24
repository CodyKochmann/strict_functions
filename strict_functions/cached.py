from strict_functions import overload
try:
    from functools import lru_cache 
except ImportError:
    from strict_functions.trace2 import lru_cache

def cached(fn, size=32):
    ''' this decorator creates a type safe lru_cache
    around the decorated function. Unlike
    functools.lru_cache, this will not crash when
    unhashable arguments are passed to the function'''
    assert callable(fn)
    assert isinstance(size, int)
    return overload(fn)(lru_cache(size, typed=True)(fn))

if __name__ == '__main__':
    @cached
    def adder(*args):
        print('running:', locals())
        return sum(args)
        
    print(adder(1,2))
    print(adder(2,3))
    print(adder(1,2))
    print(adder([1,2], [3,4]))
    
