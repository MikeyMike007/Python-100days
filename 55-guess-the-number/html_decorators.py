def make_bold(function):
    def bold_wrapper(*args, **kwargs):
        return f"<b>{function(*args)}</b>"

    return bold_wrapper


@make_bold
def greet(firstname, surname):
    return f"Hello {firstname} {surname}"


@make_bold
def greet_again(firstname):
    return f"Hello {firstname} again"


print(greet("Firstname", "Surname"))
print(greet_again("Firstname"))
