
#Argument unpacking in Python turns a sequence of values into individual arguments or separated args .
def average(*args):
    total = 0
    for arg in args:
        total += arg
    return total / len(args)
print(average(1, 2)) # each of these is a separate argument
print(average(1, 2, 3))
nums = [10,45,60,43,40,100]
print(average(*nums)) 
# We can't pass a list of values. The function expects individual arguments, 
# not a single collection of numbers. Therefore in order to make it to work we need to use the asterisk , 
# or unpack the list int to invidiual arguments using an asterisk.

# This function accepts any number of arguments and returns their average.
