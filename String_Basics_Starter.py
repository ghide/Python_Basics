
first = "Nico"
last = "Hulkenberg"

# - Create a variable called "full_name" that combines first and last with a space between them.  
# - Print it out
full_name = first + " " + last
print(full_name)



# - Create an "initials" variable that holds the first character of first followed by the first character of last. 
# - Print it out

intials = first[0] + last[0]
print(intials)

# - Create an "initials_2" variable that holds the first character of first followed by the first character of last, with periods after each letter!
# - Print it out
intials_2 = first[0]+"." + last[0]+"."
print(intials_2)


# Create a "nickname" variable that holds the first 4 characters of "last" (use a slice)
# Print it out 

nickname = first[0:4] + last[0:4]
print(nickname)


