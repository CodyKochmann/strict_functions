# strict_functions.py

---

Strict data type enforcement for Python 2 and Python 3 functions.

This project was basically created in order to bring strict variable handling for functions to Python. Python 3 brought methods for us to be able to imply what functions were taking in.

Yes, with more flexibility it makes things easier to get up and running. Swift and a few other modern languages have proven that if you're willing to lock down what comes in and out of functions, it makes programming in general much more predictable.

Being that Python has a wonderful wrapper interface, I made an interface that allows you to restrict your code without the need to add asserts to your function definition.

```
@input_types( l=list, index=int )
@output_type( int )
def pick( l, index ):
    return l[index]
```

The strictness of the defining of the input types was designed to be flexible as well. However the variables for `@input_types` are defined, is a template for the minimum required variables for the function to run properly. For example:

```
@input_types(list,str)
@output_type(list)
def find_strings_with_phrase( list_of_strings, search_phrase, sort_result=False ):
    result = []
    for s in list_of_strings:
        if search_phrase in s:
            result.append(s)
    if sort_result:
        result = sorted(result)
    return result

l="hi joe how are you doing today?".split(" ")
for s in find_strings_with_phrase( l, "o", sort_result=True ):
    print(s)
```

Outputs

```
doing
how
joe
today?
you
```

Now say we decide to throw a tuple in there instead of a list with this below:

```
l = "hi joe how are you doing today?".split(" ")
l = tuple(l)
for s in find_strings_with_phrase( l, "o", sort_result=True ):
    print(s)
```

You would then get this message from the debugger and know exactly what variable in the function call made the error occur.

```
Traceback (most recent call last):
  File "/tmp/test.py", line 110, in <module>
    for s in find_strings_with_phrase( l, "o", sort_result=True ):
  File "/tmp/test.py", line 47, in wrapper
    type(args[i]).__name__
AssertionError: wrapper needs arg 1 to be a list not a tuple
```
