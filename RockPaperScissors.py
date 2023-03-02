from random import randint
import time
vaild_responses =["yes", "no", "y", "n", "Yes", "YES", "No", "NO"]
yes_responses = ["yes", "y","Yes", "YES"]
no_responses = ["no", "n","No", "NO"]

# Vaild Inputs
computer_options = ["Rock", "Paper", "Scissors", "Gun"]
options = ["1","r", "R", "Rock", "rock", "2", "p", "P", "Paper", "paper", "3","s", "S", "Scissors", "scissors", "4", "g", "G", "Gun", "gun"]
rock_options = ["r", "R", "Rock", "rock", "1"]
paper_options = ["p", "P", "Paper", "paper", "2"]
scissor_options = ["s", "S", "Scissors", "scissors", "3"]
gun_options = ["4", "g", "G", "Gun", "gun"]

player_choice = 0 # 0 - unset, 1 - rock, 2 - paper, 3 - scissors, 4 - gun 
player_choice_set = False
computer_choice = 0
play_again = True

def vaild():
    global player_choice_set
    player_choice_set = True
    print("\nYou threw " +str(player_choice))
    time.sleep(1)

def lost():
    global player_choice_set
    print("You Lost!")
    player_choice_set = False

def won():
    global player_choice_set
    print("You Win!")
    player_choice_set = False

while play_again == True:
    play_again = False
    computer_choice = computer_options[randint(0,3)] # computer chooses
    while player_choice_set == False:
        player_choice = input("------------------------------------------\nRock Paper Scissors                  v0.1\nWhat do you throw?\nRock, Paper or Scissors?\n-->> ")
        if player_choice in options: # checking for vaild input
            while player_choice_set == False:
                if player_choice in rock_options:
                    player_choice = "Rock"
                    vaild()     
                elif player_choice in paper_options:
                    player_choice = "Paper"
                    vaild()                    
                elif player_choice in scissor_options:
                    player_choice = "Scissors" 
                    vaild()
                elif player_choice in gun_options:
                    player_choice = "Gun"
                    vaild()
        else:print("Invaild Option\n")
    while player_choice_set == True: # the player has chosen
        print("Computer threw " +str(computer_choice))
        if player_choice == computer_choice:
            print("It's a tie, No one wins!")
            player_choice_set = False
        else: # finds who won
            if player_choice == "Rock": # Rock
                if computer_choice == "Paper": # Rock (p) v Paper 
                    lost()
                elif computer_choice == "Scissors": # Rock (p) v Scissors
                    won()
                elif computer_choice == "Gun": # Rock (p) v Gun
                    lost()
            elif player_choice == "Paper": # Paper
                if computer_choice == "Rock": # Paper (p) v Rock
                    won()
                elif computer_choice == "Scissors": # Paper (p) v Scissors
                    lost()
                elif computer_choice == "Gun": # Paper (p) v Gun
                    lost()
            elif player_choice == "Scissors": # Scissors
                if computer_choice == "Rock": # Scissors (p) v Rock
                    lost()
                elif computer_choice == "Paper": # Scissors (p) v Paper
                    won()
                elif computer_choice == "Gun": # Scissors (p) v Gun
                    lost()
            elif player_choice == "Gun": # Gun
                if computer_choice == "Rock": # Gun (p) v Rock
                    won()
                elif computer_choice == "Paper": # Gun (p) v Paper
                    won()
                elif computer_choice == "Scissors": # Gun (p) v Scissors
                    won()
    while play_again == False:
        play_again = input("Play again? (y/n)\n-->> ")
        if play_again in vaild_responses:
            if play_again in yes_responses:
                print("")
                play_again = True
            elif play_again in no_responses:
                print("...\n-------------------------------------")
                break
        else:print("Invaild Option")            