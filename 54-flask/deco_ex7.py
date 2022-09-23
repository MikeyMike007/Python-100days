import functools
import math


def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__} returned {value}")
        return value

    return wrapper_debug


factorial = debug(math.factorial)


def approximate_e(terms=18):
    return sum(1 / factorial(n) for n in range(terms))


result = approximate_e(10)
print(result)
