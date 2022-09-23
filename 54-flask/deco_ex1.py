from datetime import datetime


def not_after_office_hours(func):
    def wrapper():
        hour = datetime.now().hour
        if hour <= 17 and hour > 9:
            func()
        else:
            pass

    return wrapper


@not_after_office_hours
def work():
    print("Work Work Work")


work()
