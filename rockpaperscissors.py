# rock paper scissors game

import random

#import random module
options = ("rock","paper","scissor")
running = True

while running:
    player=None
    #take input from computer
    computer=random.choice(options) 

    while player not in options:
        #take input from user
        player = input("Enter a choice(rock,paper,scissor): ")

    print(f"player : {player}")
    print(f"computer : {computer}")

    if player==computer:
        print("it's a tie!")

    elif player == "rock" and computer == "scissor":
        print("you win!")

    elif player=="paper" and computer == "rock":
        print("you win!")

    elif player == "scissor" and computer=="paper":
        print("you win!")
    else:
        print("you lose!")

    play_again = input("play again (yes/no): ").lower()
    if not play_again == "yes":
        running = False

print("Thank you for playing!")