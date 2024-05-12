

# def add_twice(val, lst=[]):
#     lst.append(val)
#     lst.append(val)
#     return lst

# add_twice("hi", [1, 2, 3, 4])
# print(add_twice("hi", [1, 2, 3, 4]))

def add_twice_2(val, lst=None):
    val = val + val
    if lst is None:
        lst = []
    lst.append(val)
    lst.append(val)
    return lst

def add_twice_3(val, lst=None): # The None gives the list a default value of an empty list.
    if lst is None:
        lst = []
    lst.append(val)
    lst.append(val)
    return lst
print(add_twice_3("hi"))

#add_twice expects a value and a list to be passed in.
# It depends on the value to the list twice and returns the list.
def add_thrice(val, lst=[]):
    lst.append(val)
    lst.append(val)
    lst.append(val)
    return lst
print(add_thrice("hi", [1, 2, 3, 4]))

