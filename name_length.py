first_name = input("what is your first name ")
last_name = input("what is your last name ")
name_length = len(first_name) + len(last_name)


if name_length ==12:
    print("*"*100)
    print(f"{first_name} {last_name} is exactly the average length of American names")
    print("*"*100)
   
elif name_length < 12:
    print("*"*100)
    print(f"{first_name} {last_name} is shorter than the average length of American names")
    print("*"*100)
else:
    print(f"{first_name} {last_name} is longer than the average length of American names")

    