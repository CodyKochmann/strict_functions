# strict_functions

[![Downloads](https://pepy.tech/badge/strict-functions)](https://pepy.tech/project/strict-functions)
[![Downloads](https://pepy.tech/badge/strict-functions/month)](https://pepy.tech/project/strict-functions)
[![Downloads](https://pepy.tech/badge/strict-functions/week)](https://pepy.tech/project/strict-functions)

---

Decorators for function scope control, overloading, type safety, thread safety, cache control, tracing and even self awareness!

## How to install

```python
pip install strict_functions
```

## What's included?

### Scope Control

| Name | Description |
| :--- | :--- |
| `@noglobals` | removes global access outside of the function's local scope |
| `@strict_globals` | locks down function's scope to whitelisted globals |
| `@self_aware` | injects `self` into function's scope referring to the function object itself |

### Execution Control

| Name | Description |
| :--- | :--- |
| `@never_parallel` | protects functions that are not thread safe in threaded environments |
| `@on_fail` | provides clean defining of default function outputs and logging on crash events |
| `@overload` | provides mechanisms to define actual function overloading in python |

### Type Safety

| Name | Description |
| :--- | :--- |
| `@input_types` | type enforcement applied to the function's inputs |
| `@output_type` | type enforcement applied to the function's output |
| `@strict_defaults` | auto-enforced type checking on functions based on the function's defaults |

### Cache Control

| Name | Description |
| :--- | :--- |
| `@cached` | `lru_cache` functionality for functions that might want unhashable arguments |
| `@lru_cache` | `lru_cache` backports for python2 usage |

### Other Goodies

| Name | Description |
| :--- | :--- |
| `@trace` | visually trace steps of a function as it executes to watch the data be processed |
| `attempt` | inline try/except/log blocks for calling functions in comprehensions |
| `force_assertions` | call this method to verify assertions have not been turned off |

