import functools

# def do_twice(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#
#     return wrapper


def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper


@do_twice
def greet(name):
    print(f"Hello {name}")


@do_twice
def say_whee():
    print("Whee")


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hello {name} from return_greeting"


print(say_whee)  # <function do_twice.<locals>.wrapper_do_twice at 0x7f43700e52f0>
print(say_whee.__name__)  # wrapper
print(help(say_whee))
# Help on function wrapper in module decorators:
#
# wrapper()
