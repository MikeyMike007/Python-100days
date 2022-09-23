import time

# Functions
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Functions are first class objects
def calcluate(calc_func, n1, n2):
    return calc_func(n1, n2)


result = calcluate(multiply, 2, 2)
print(result)


print("--------------\n\n")


result = calcluate(add, 2, 2)
print(result)


print("--------------\n\n")


# Nested functions
def outer_function():
    print("Im am outer")

    def nested_function():
        print("I am inner")

    nested_function()


outer_function()

print("--------------\n\n")


# Functions can be returned from other functions
def outer_function_1():
    print("Im am outer")

    def nested_function():
        print("I am inner")

    return nested_function


inner_function = outer_function_1()
inner_function()


print("--------------\n\n")


# Python Decorators - Adds extra functionality to functions
def delay_decorator(function):
    def wrapper_function():
        print("Adding some functionality before function is run")
        time.sleep(1)
        function()
        time.sleep(1)
        print("Adding some functionality before function is run")

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_goodbye():
    print("Goodbye")


@delay_decorator
def say_greeting():
    print("How are you?")


# Syntatic sugar for delay_decorator(say_hello)()
say_hello()

print("--------------\n\n")

say_goodbye()

print("--------------\n\n")
say_greeting()


# Now we want to create more greeting function such as say_goodbye
