import functools
import time


def slowdown(func):
    @functools.wraps(func)
    def slowdown_wrapper(*args, **kwargs):
        time.sleep(1)
        value = func(*args, **kwargs)
        return value

    return slowdown_wrapper


@slowdown
def countdown(n):
    if n < 1:
        print("Liftoff")
    else:
        print(f"T minus {n}")
        countdown(n - 1)


countdown(10)
