from all_decorators import debug, do_twice


@debug
@do_twice
def greet1(name):
    print(f"Hello {name}")


@do_twice
@debug
def greet2(name):
    print(f"Hello {name}")


greet1("Angela")
print("------------------")
greet2("Angela")
