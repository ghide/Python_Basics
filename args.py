

# def count_stuff(*args): # *args is the name of the arguments. It can accept any number of arguments.
#      for arg in args:
#         print(args)
        
        
# def sum(*nums):
#     total = 0 # Here we set the total variable intitially to 0
#     for num in nums:
#         total += num # This is the same as total = total + num
#     return total

# def silly(first, second, *others):
#     print(f"first is:,{first}")
#     print (f"second is:,{second}")
#     print (f"others is:,{others}")
    
    
    #**kwargs - we can use the  ** notation to write functions that accept any number of keyword arguments.
    # The two ** stars tells python to create a dictionary of the keyword arguments.
def print_ages(**kwargs):
    for name, age in kwargs.items(): 
        print(f"{name} is {age} years old")
print_ages(Smith =67, Bob = 32, Alice = 27)
        