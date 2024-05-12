

# The default arguments must come first.
#The order is (parameter, *args, default parameters, **kwargs)
#When defining a function, the order of the parameters is very important or matters.

def display_info(person, *args, status="single", **kwargs):
   print (f" person is:{person}")
   print (f" status is:{status}")
   print(f" args is:{args}")
   print(f" kwargs is:{kwargs}")
   
display_info("John", 1, 2, 3, 4, 5, name="John", age=27, status="married", city="New York")

# In the above case the order is (person, status, args, kwargs)
#person is a positional parameter.
#status is a default parameter.
#args is a tuple.
#kwargs is a dictionary.