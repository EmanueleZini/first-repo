#import
import random

# Write code below 💖
repeat = 1

while repeat != 0:
    print("===================\nRock Paper Scissors\n===================\n")
    print("1) ✊\n2) ✋\n3) ✌️")
    player = int(input("Pick a number: "))
    computer = random.randint(1,3)

    if player == 1 and computer == 2:
        print("You chose: ✊\nCPU chose: ✋\nThe CPU won!")
    elif player == 2 and computer == 1:
        print("You chose: ✋\nCPU chose: ✊\nThe player won!")
    elif player == 3 and computer == 2:
        print("You chose: ✌️\nCPU chose: ✋\nThe player won!")
    elif player == 2 and computer == 3:
        print("You chose: ✋\nCPU chose: ✌️\nThe CPU won!")
    elif player == 1 and computer == 3:
        print("You chose: ✊\nCPU chose: ✌️\nThe player won!")
    elif player == 3 and computer == 1:
        print("You chose: ✌️\nCPU chose: ✊\nThe CPU won!")
    else:
        print("Same choice, draw")

    print("You want to play again? (yes = 1 / no = 0)")
    repeat = int(input())





