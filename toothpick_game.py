
#ask for player name

print("Welcome to the toothpick game!")
print("********************************")


num_left = 13
player1_name = input("Enter player 1's name: ")
player2_name = input("Enter player 2's name: ")
current_player = player1_name


while True:
    print ("| " * num_left)
    print(f"There are {num_left} toothpicks left")
    choice = int(input(f"{current_player}, how many toothpick do yo take? "))
    
    while choice != 1 and choice !=2 and choice !=3:
        choice = int(input("You can only choice 1, 2, or 3 toothpicks."))
    num_left -= choice
    if num_left <= 0:
        print(f"{current_player} wins! the game!")
        break   
    if current_player == player1_name:
        current_player = player2_name
    else:
        current_player = player1_name
    
print("Game over!")































































#game loop, until someone wins:

#ask player1 to enter nymber

# check to see if they win


# ask player2 to enter nymber

# check to see if they win
