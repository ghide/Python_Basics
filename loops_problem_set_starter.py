
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
for char in word:
    print(char)


# Write a while loop that does the same thing!

index = 0  # In this case we need an index variable to keep track of our position in the word.
while index < len(word):
    print(word[index])
    index += 1
#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)

number =100

# while number <= 140:
#     if number % 2 == 0:
#         print(number)
#     number += 1

# OR we can also do it differently.

while number <= 140:
   print(number)
   number += 2



# Write a for loop that does the same thing (with range())

for number in range(100, 142, 2):
    print(number)


#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
reply = input("Please enter the passphrase: ")
while reply != "sillygoose":
    reply = input("Please enter the passphrase: ") # in this case we are updating the value of reply
    #print("I'm sorry, that is not the correct passphrase. Please try again.")


