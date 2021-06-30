# Create an app that does the following:

# 1. Asks for player name
# 2. Greets and show playing options
# 3. Player is asked to make a choice (read from the console)
# 4. Computer makes a random choice
# 5. If the computer makes the same choice, play again
# 6. If not, show the result
# 7. Asks the player if he/she wants to play again
# 8. Game stops when the player decides not to play again

# Game rules:
# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporises Rock
# Rock crushes Scissors

import random


# Options

opts = ["Scissors", "Paper", "Rock", "Lizard", "Spock"]

# Game start
name = input("What's your name?: ")
print(f"You are not prepared, {name}")

# Game reactions
tie = f"{name}, this round's a tie."
win = f"{name}, you have won!"
loss = f"{name}, you have lost!"


while True:
    user_option = input(
        f"{name}, you can play as: {opts[0]}, {opts[1]}, {opts[2]}, {opts[3]}, {opts[4]}. Type your choice here: ").capitalize()
    computer_option = random.choice(opts)
    print(
        f"You have selected {user_option}. The computer's chosen {computer_option}.")
    # Results:
    if user_option == computer_option:
        print(tie)

    elif user_option == "Scissors":
        if computer_option == "Rock" or computer_option == "Spock":
            print(loss)
        else:
            print(win)

    elif user_option == "Paper":
        if computer_option == "Scissors" or computer_option == "Lizard":
            print(loss)
        else:
            print(win)

    elif user_option == "Rock":
        if computer_option == "Paper" or computer_option == "Spock":
            print(loss)
        else:
            print(win)

    elif user_option == "Lizard":
        if computer_option == "Scissors" or computer_option == "Rock":
            print(loss)
        else:
            print(win)

    elif user_option == "Spock":
        if computer_option == "Paper" or computer_option == "Lizard":
            print(loss)
        else:
            print(win)

    again = input("Do you wish to try again? Yes or No: ").capitalize()
    if again != "Yes":
        break
        print(f"Thank you for the games, {name}")
