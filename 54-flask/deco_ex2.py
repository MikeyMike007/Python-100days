# def do_twice(func):
#     def wrapper():
#         func()
#         func()
#
#     return wrapper

#
# def do_twice(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#
#     return wrapper
#


def do_twice(func):
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


# # greet("Angela")  # Error
#
#
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# # TypeError: wrapper_do_twice() takes 0 positional arguments but 1 was given
#

greet("Angela")
say_whee()
greeting = return_greeting("Angela")
print(greeting)
