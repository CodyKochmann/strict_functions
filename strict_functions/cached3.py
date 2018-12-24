from strict_functions import overload, lru_cache
from typing import Callable, Any

def cached(fn:Callable, size=32) -> Callable:
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
    
