from inspect import isgeneratorfunction
from functools import wraps
from strict_globals import strict_globals

def self_aware(fn):
    ''' decorating a function with this allows it to 
        refer to itself as 'self' inside the function
        body.
    '''
    if isgeneratorfunction(fn):
        @wraps(fn)
        def wrapper(*a,**k):
            generator = fn(*a,**k)
            if hasattr(
                generator, 
                'gi_frame'
            ) and hasattr(
                generator.gi_frame, 
                'f_builtins'
            ) and hasattr(
                generator.gi_frame.f_builtins, 
                '__setitem__'
            ):
                generator.gi_frame.f_builtins[
                    'self'
                ] = generator
        return wrapper
    else:
        fn=strict_globals(**fn.__globals__)(fn)
        fn.__globals__['self']=fn
        return fn

if __name__ == '__main__':
    @self_aware
    def who_am_i():
        return 'hello my name is {}'.format(self.__name__)
    
    
    @self_aware
    def call_counter():
        if hasattr(self,'runs'):
            self.runs += 1
        else:
            self.runs = 1
        print('I have ran {} times'.format(self.runs))
    
    
    print(who_am_i())
    # hello my name is who_am_i
    
    for i in range(10):
        call_counter()
    # I have ran 1 times
    # I have ran 2 times
    # I have ran 3 times
    # I have ran 4 times
    # I have ran 5 times
    # I have ran 6 times
    # I have ran 7 times
    # I have ran 8 times
    # I have ran 9 times
    # I have ran 10 times
    
