import random
import re
#"R" for rock, "P" for paper, "S" for scissors
option_list = ["R", "P", "S"]

print("Welcome to the ROCK, PAPER AND SCISSORS game")
print("These are the rules of the game: \n" + "Rock vs Scissors -> Rock wins! \n" + "Paper vs Rock -> Paper wins! \n" + "Scissors vs Paper -> Scissors wins!")

def choose_option():
    print("---------Instructions:----------- ")
    print("R for 'ROCK'\n"+ "P for 'PAPER' \n" + "S for 'SCISSORS'")
    player_choice =  input("Choose an option between 'R', 'P' or 'S':  \n")
    player_choice = player_choice.upper()
    if player_choice in ["R", "P", "S"]:
        return player_choice
    else:
        print("Invalid option, please try again")
        print (" ")
        return choose_option()



        

def computer_option():
    computer_choice = random.choice(option_list) 
    return computer_choice
game_over = False
while not game_over:
    player_choice = choose_option()
    computer_choice = computer_option()

    if player_choice == computer_choice:
            print(f"player({player_choice}) : CPU({computer_choice})")
            print("Its a tie!")
            print(" ")
        
    elif player_choice == "R":
        if computer_choice == "S":
            print(f"player({player_choice}) : CPU({computer_choice})")
            print("Rock smashes scissors: You win!")
        else:
            print(f"player({player_choice}) : CPU({computer_choice})")
            print("Paper covers rock: You lose!")
    elif player_choice == "P":
        if computer_choice == "R":
            print(f"player({player_choice}) : CPU({computer_choice})")
            print("Paper covers rock: You win")
        else:
            print(f"player({player_choice}) : CPU({computer_choice})")
            print("Scissors cut paper: You lose!")
    elif player_choice == "S":
        if computer_choice == "P":
            print(f"player({player_choice}) : CPU({computer_choice})")
            print("Scissors cut paper: You win!")
        else:
            
            print(f"player({player_choice}) : CPU({computer_choice})")
            print("Rock smashes scissors: You lose!")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() == "y": 
        pass
    else:
        break
print("Game Over, Goodbye..")
