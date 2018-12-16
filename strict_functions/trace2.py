import sys, inspect, operator, os, pprint
from functools import partial, wraps

# trace.py for python2

# formats nested structure for pretty output
pformat = pprint.PrettyPrinter(
    width=1,
    depth=256,
    indent=2
).pformat

def lru_cache(buffer_size):
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

@lru_cache(1)
def profile_print(s):
    ''' prints the profiler's findings and filters
        duplicates and the profiler's traces '''
    if 'wafflestwaffles' not in s:
        print(s)

_get_frame = operator.attrgetter('filename', 'lineno', 'code_context', 'function')

def get_frame_src(f):
    ''' inspects a frame and returns a string with the following

        <src-path>:<src-line> -> <function-name>
        <source-code>
    '''
    path, line, src, fn = _get_frame(
        inspect.getframeinfo(f)
    )
    return '{}:{} -> {}\n{}'.format(
        path.split(os.sep)[-1],
        line,
        fn,
        repr(src[0][:-1]) # shave off \n
    )

def get_locals(f):
    ''' returns a formatted view of the local variables in a frame '''
    return pformat({i:f.f_locals[i] for i in f.f_locals if not i.startswith('__')})

def default_profiler(f, _type, _value):
    ''' inspects an input frame and pretty prints the following:

        <src-path>:<src-line> -> <function-name>
        <source-code>
        <local-variables>
        ----------------------------------------
    '''
    profile_print(
        '\n'.join([
            get_frame_src(f),
            get_locals(f),
            '----------------------------------------'
        ])
    )

def trace(fn=None, profiler=None):
    ''' This decorator allows you to visually trace
        the steps of a function as it executes to see
        what happens to the data as things are being
        processed.

        If you want to use a custom profiler, use the
        @trace(profiler=my_custom_profiler) syntax.

        Example Usage:

            def count_to(target):
               for i in range(1, target+1):
                   yield i

            @trace
            def sum_of_count(target):
               total = 0
               for i in count_to(target):
                   total += i
               return total

            sum_of_count(10)
    '''
    # analyze usage
    custom_profiler = fn is None and profiler is not None
    no_profiler = profiler is None and fn is not None
    no_args = profiler is None and fn is None
    # adjust for usage
    if custom_profiler: # for @trace(profiler=...)
        return partial(trace, profiler=profiler)
    elif no_args: # for @trace()
        return trace
    elif no_profiler: # for @trace
        profiler = default_profiler
    # validate input
    assert callable(fn)
    assert callable(profiler)
    # build the decorator
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # flag for default_profiler to know to ignore this scope
        wafflestwaffles = None
        # save the previous profiler
        old_profiler = sys.getprofile()
        # set the new profiler
        sys.setprofile(profiler)
        try:
            # run the function
            return fn(*args, **kwargs)
        finally:
            # revert the profiler
            sys.setprofile(old_profiler)
    return wrapper

if __name__ == '__main__':
    def count_to(target):
       for i in range(1, target+1):
           yield i

    @trace
    def sum_of_count(target):
       total = 0
       for i in count_to(target):
           total += i
       return total

    sum_of_count(10)
