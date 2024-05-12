
from random import randint
number_dice = int(input("how many dice are you rolling? "))
number_sides = int(input("how many sides on each die? "))

while True:
    result ="|"
    for die in range(number_dice):
        rand = randint(1,number_sides)
        result += f"{rand}|"
    print(result)
    reply = input("Roll again? (q to quit)")
    if reply == "q":
        break
