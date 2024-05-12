
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# number = is_even(5)

# print(number)

# def is_odd(num):
#     if num % 2 == 0:
#         return False
#     else:
#         return True
    
# number = is_odd(30)

# print(number)


# def slugify(title):
# #     words = title.split(" ")
# #     slug = "-".join(words)
# #     return slug

# # print(slugify(title)
#  return title.lower().strip().replace(" ", "-")


# title = "This is a title"

# print(title.lower().strip().replace(" ", "-"))

# def count_vowels(word):
#     count = 0
#     for letter in word:
#         if letter in "aeiou":
#             count += 1
#     return count
# word = "banana"
# print(count_vowels(word))

# def laugh(level =10):  # this is a default value, so that if no value is passed in, it will default to 10. Therefore the cocde will not show an error.
#     print("HA!" * level)
    
    
# def slugify(title, sep="-",seperator=" "):
#     return title.lower().strip().replace(" ", "-")
# #print(slugify("Every day is a chance to be better person"))

# word = "Make the world a better"
# print(slugify(word))


# def greet(person="stranger", msg="Hi"): # if no value is passed in, it will default to "stranger" and "Hello". 
#     #But the argument with default value should be at the end.
#     print(f"{msg}, {person}!")
    
# greet()

def get_total(price, qty=1, tax=0.02, discount=0):
   subtotal = price * qty * (1 - discount)
   print(subtotal*(1 + tax))
   
#get_total(4.99,5,0.015,0.2)
 

get_total(9.75, 5, 0.01, 0.5)  # in this case the arguments are in this order - which means order matters. This means this is called positional arguments.

get_total(price=9.75,qty=5,tax=0.01,discount=0.5) # in this case the arguments are in this order - which means order doesn't matters. And this is called keyword arguments.

get_total(price=9.75, tax=0.01,qty=5,discount=0.5)
get_total(8.99) # In this case it take the default values for qty, tax and discount.