import random

PLUGINS = dict()


def register(func):
    """Register a function as plugin"""
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name):
    return f"Hello {name}"


@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def randomly_greet(name):
    greeter, greet_function = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter}")
    return greet_function(name)


greeting = randomly_greet("Alice")
print(greeting)

print(PLUGINS)

print(globals())
