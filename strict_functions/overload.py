from functools import wraps
from traceback import format_list, extract_stack

class Overload(object):
    _cache = {}

    @staticmethod
    def validate_function(fn):
        assert callable(fn)
        assert hasattr(fn, '__qualname__') or hasattr(fn, '__name__')
        assert hasattr(fn, '__globals__')
        assert '__name__' in fn.__globals__

    @staticmethod
    def traceback_lines():
        for entry in format_list(extract_stack()):
            yield ''.join(
                i for i in entry.splitlines()
                if not i.strip().startswith('File ')
            )

    @staticmethod
    def has_args():
        ''' returns true if the decorator invocation
            had arguments passed to it before being
            sent a function to decorate '''
        no_args_syntax = '@overload'
        args_syntax = no_args_syntax + '('
        args, no_args = [(-1,-1)], [(-1,-1)]
        for i, line in enumerate(Overload.traceback_lines()):
            if args_syntax in line:
                args.append((i, line.find(args_syntax)))
            if no_args_syntax in line:
                no_args.append((i, line.find(no_args_syntax)))
        args, no_args = max(args), max(no_args)
        if sum(args)+sum(no_args) == -4:
            # couldnt find invocation
            return False
        return args >= no_args

    @staticmethod
    def identify(fn):
        ''' returns a tuple that is used to match
            functions to their neighbors in their
            resident namespaces '''
        return (
            fn.__globals__['__name__'], # module namespace
            getattr(fn, '__qualname__', getattr(fn, '__name__', '')) # class and function namespace
        )
        def __init__(self, fn):
            self.validate_function(fn)
            self.configured = False
            self.has_backup_plan = False
            if self.has_args():
                self.backup_plan = fn
            else:
                self.id = self.identify(fn)
                self.backup_plan = big.overload._cache.get(self.id, None)
                #if self.id in overload._cache:
                #    self.backup_plan =
                self.configure_with(fn)
            #wraps(fn)(self)

        def __call__(self, *args, **kwargs):
            #print(locals())
            try:  # try running like normal
                return self.fn(*args, **kwargs)
            except Exception as ex:
                if self.has_backup_plan:
                    return self.backup_plan(*args, **kwargs) # run backup plan
                elif self.configured:
                    raise ex # no backup plan, abort
                else:
                    # complete unconfigured setup
                    self.configure_with(*args, **kwargs)
                    return self

    @staticmethod
    def default_decorator(firin):
        Overload.validate_function(firin)
        _id = Overload.identify(firin)
        has_backup_plan = _id in Overload._cache
        if has_backup_plan:
            backup_plan = Overload._cache[_id]
        @wraps(firin)
        def imma_firin(*mah, **lazars):
            if has_backup_plan:
                try:
                    return firin(*mah, **lazars)
                except:
                    return backup_plan(*mah, **lazars)
            else:
                return firin(*mah, **lazars)
        Overload._cache[_id] = imma_firin
        return imma_firin

    @staticmethod
    def configured_decorator(custom_backup_plan):
        Overload.validate_function(custom_backup_plan)
        def hotrod(firin):
            @wraps(firin)
            def imma_firin(*mah, **lazars):
                try:
                    return firin(*mah, **lazars)
                except:
                    return custom_backup_plan(*mah, **lazars)
            Overload._cache[Overload.identify(firin)] = imma_firin
            return imma_firin
        return hotrod

    @staticmethod
    def overload(fn, function_to_overload=None):
        '''
This function decorator allows you to overload already defined functions. The
execution of overloaded functions is done by trying the original version first
and if it fails, the variables are handed off to the overloading function.

While this does seem like a sloppy way to go about choosing the execution of
functions, this gives you far more control in terms of how you want each
function to be selected and allows you to program for the "ideal situation"
first.

With this approach, you can simply require very specific conditions that would
apply to a majority of the use cases of the function and allow the code to
mitigate edge case scenarios only when the edge cases show up vs checking for
edge cases on every single usage of the function.

This approach rewards functions that are designed with proper input validation,
which you should be adding anyways.

#------------------------------------------------------------------------------
#   Example Usage Below
#------------------------------------------------------------------------------

def my_print(arg):
    print('running original my_print')
    print(arg)

@overload
def my_print(arg):
    assert type(arg) == list
    print('running list my_print')
    print(', '.join(str(i) for i in arg))

@overload
def my_print(arg):
    assert type(arg) == dict
    print('running dict my_print')
    out = ('='.join((str(k), str(v))) for k,v in arg.items())
    print(' | '.join(out))

my_print(list(range(10)))
# running list my_print
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

my_print(tuple(range(10)))
# running original my_print
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

my_print({i:i*2 for i in range(10)})
# running dict my_print
# 0=0 | 1=2 | 2=4 | 3=6 | 4=8 | 5=10 | 6=12 | 7=14 | 8=16 | 9=18

'''
        if function_to_overload is None:
            if Overload.has_args():
                return Overload.configured_decorator(fn)
            else:
                return Overload.default_decorator(fn)
        else:
            return Overload.configured_decorator(function_to_overload)(fn)

overload = Overload.overload

if __name__ == '__main__':

    @overload
    def my_adder(a):
        return a+1

    @overload
    def my_adder(a, b):
        return a+b

    @overload(lambda *i:i)
    def pa(a):
        return a*3

    print(pa('5'))
    print(pa(5,5))
    print('+')
    print(my_adder(7))
    print(my_adder(8,3))


    class Robot(object):
        def __init__(self):
            self.x = 0
            self.y = 0

        @overload
        def move(self, x, y):
            self.x += x
            self.y += y

        @overload
        def move(self, coords):
            assert len(coords) == 2
            self.move(coords[0], coords[1])

        def run(self):
            return 1

    bimo = Robot()
    print(bimo.x, bimo.y)
    # 0 0
    for i in range(10):
        bimo.move(i, i/2)

    print(bimo.x, bimo.y)
    # 45 22.5

    for i in range(10):
        bimo.move([i, i/2])

    print(bimo.x, bimo.y)
    # 90 45.0
