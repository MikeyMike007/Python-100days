# Advanced Python Decorator Function


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


# We now want to decorate our function so that only users that are logged in
# can create a blogpost
def is_authenticated(func):
    def wrapper(*args, **kwargs):
        # if user.is_logged_in == True: # Doesnt work
        if args[0].is_logged_in is True:
            func(args[0])
        else:
            print(f"User {args[0].name} is not logged in. Cannot make blogpost.")

    return wrapper


@is_authenticated
def creat_blog_post(user):
    print(f"This is {user.name} blog post")


new_user = User("Angela")
creat_blog_post(new_user)

new_user.is_logged_in = True
creat_blog_post(new_user)  # Makes a blogpost
