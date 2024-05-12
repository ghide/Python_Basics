
#*args means  many arguments
def average(**args):
    total = 0
    for arg in args:
        total += arg
    return total / len(args)