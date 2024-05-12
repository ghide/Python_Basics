

raise ValueError("This is an error message")
# We can raise our own exceptions(force them to happen) whenever we want, using the raise keyword.

def get_user_name():
    inp= input("please enter your name:")
    if  not inp.isalpha():
        raise ValueError("Please enter a valid name")
    else:
        return inp


def register_user():
    user = get_user_name()
    DataBase.save(user)
    