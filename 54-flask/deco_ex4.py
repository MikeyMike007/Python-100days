import functools


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):

        # Do something before function
        value = func(*args, **kwargs)
        # Do something after function

        return value

    return wrapper_decorator
