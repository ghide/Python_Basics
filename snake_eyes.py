
import random
roll1 = random.randint(1,6)
roll2 = random.randint(1,6)
roll_count =1

while roll1 != 1 or roll2 != 1:
    print(roll1, roll2)
    roll1 = random.randint(1,6) # this updating the value of roll1
    roll2 = random.randint(1,6) # this updating the value of roll2
    roll_count += 1
    
print(roll1, roll2)
print("YAY, you got snake eyes!")
print(f" it took you {roll_count} rolls to get snake eyes")