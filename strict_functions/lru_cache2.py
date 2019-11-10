from functools import wraps

'''cheap backports for python2 lru cache'''

def lru_cache(buffer_size, typed=False):
    def decorator(fn):
        cache = {}
        keys = []
        @wraps(fn)
        def wrapper(*args):
            try:
                return cache[args]
            except TypeError:
                return fn(*args)
            except KeyError:
                keys.append(args)
                cache[args] = fn(*args)
                try:
                    return cache[args]
                finally:
                    if len(keys) > buffer_size:
                        cache.pop(keys.pop(0))
        return wrapper
    return decorator

