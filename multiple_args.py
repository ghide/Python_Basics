

# The order of parameters is very important here.
#Note : after the return function, the code will not execute. Even the print function will not execute

def divide(a, b):
    if b == 0:
        print("You cannot divide by 0")
        return "You cannot divide by 0"
    return a / b

num = divide(10,2)

print(num)
