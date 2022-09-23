# Advanced arguments i.e. argumetns with default values


# Arguments have default valies
def my_function(a=1, b=2, c=3):
    print(f"a: {a} - b: {b} - c: {c}")


# If you dont provide arguments, it will set the arguments to the default
# values
my_function()
my_function(a=3)
my_function(a=5, b=10)
my_function(a=10, b=15, c=1)

# *args: Many positional arguments


# This function can only add two numbers
def add_two(n1, n2):
    return n1 + n2


# *args is a tuple
def add_several(*args):
    return sum(number for number in args)


print(add_two(1, 1))  # 2
print(add_several(1, 1, 1, 1, 1))  # 5


# **kwargs: Many keyword arguments - kwargs is a dict
# -----------------------------------------
def calculate(n, **kwargs):
    # print(kwargs)  # kwargs is a dictionary
    # for key, value in kwargs.items():
    #     print(f"key: {key} - value: {value}")
    #     print(kwargs[key])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(5)


calculate(2, add=3, multiply=5)  # {'add': 3, 'multiply': 5}


class Car:
    def __init__(self, **kw) -> None:
        self.make = kw["make"]
        self.model = kw["model"]


my_car = Car(make=2017, model="bmw")
print(my_car.make)
print(my_car.model)
# my_second_car = Car(make=2017) # Error - Better to create class as:


class CarBetter:
    def __init__(self, **kw) -> None:
        self.make = kw.get("make")  # Will not crash if not exist in kw
        self.model = kw.get("model")  # Will not crash if not exist in kw


my_car = CarBetter(make=2017, model="bmw")
print(my_car.make)
print(my_car.model)

my_second_car = CarBetter(make=2017)
print(my_second_car.make)
print(my_second_car.model)  # Will return None - Better than crashing
