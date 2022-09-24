import random  # will be used for the computer to select a random number
from colorama import Fore, Back, Style  # to color the printed text
computer_choice = random.randint(1, 100)  # between 1-100 inclusive
player_input = input("Guess a number between 1-100 or type [e] to exit: ")
while player_input != "e":
    if player_input.isdigit():
        player_input = int(player_input)  # converting the input into int
        if player_input == computer_choice:
            print(Fore.GREEN + "Right Guess!")
            break  # break the loop
        elif player_input > computer_choice:
            print(Fore.YELLOW + "Try a lower number!")
        elif player_input < computer_choice:
            print(Fore.YELLOW + "Try a higher number!")
    elif player_input == "e":
        break
    else:  # if the input is not int or "e"
        print(Fore.RED + "Invalid Input!")

    print(Style.RESET_ALL) # to reset the color for the next iteration
    player_input = input("Guess a number between 1-100 or type [e] to exit: ")
print(Back.GREEN + Fore.BLACK + "Game Ended!")