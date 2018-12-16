import sys, inspect, operator, os, pprint
from functools import partial, wraps, lru_cache
from typing import Any, Callable

# for type hints
Frame = type(sys._getframe())

# formats nested structure for pretty output
pformat = pprint.PrettyPrinter(
    width=1,
    depth=256,
    indent=2,
    compact=False
).pformat


@lru_cache(1)
def profile_print(s:str):
    ''' prints the profiler's findings and filters
        duplicates and the profiler's traces '''
    if 'wafflestwaffles' not in s:
        print(s)

_get_frame = operator.attrgetter('filename', 'lineno', 'code_context', 'function')

def get_frame_src(f:Frame) -> str:
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

def get_locals(f:Frame) -> str:
    ''' returns a formatted view of the local variables in a frame '''
    return pformat({i:f.f_locals[i] for i in f.f_locals if not i.startswith('__')})

def default_profiler(f:Frame, _type:str, _value:Any):
    ''' inspects an input frame and pretty prints the following:

        <src-path>:<src-line> -> <function-name>
        <source-code>
        <local-variables>
        ----------------------------------------
    '''
    try:
        profile_print(
            '\n'.join([
                get_frame_src(f),
                get_locals(f),
                '----------------------------------------'
            ])
        )
    except:
        pass

def trace(fn=None, profiler=None) -> Callable:
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
