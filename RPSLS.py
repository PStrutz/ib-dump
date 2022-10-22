import random

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return

def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return 


def rpsls(player_choice):
    print(" ")
    print("Player chooses ", player_choice)
    player_number = name_to_number(player_choice)
    random.seed()
    comp_number = random.randint(0, 4)
    print("Computer chooses ", number_to_name(comp_number))
    try:
        dif = player_number - comp_number % 5
    except:
        print("Player input is not valid")
    if dif == 0:
        print("It's a tie")
    elif dif > 2:
        print("Computer wins!")
    else:
        print("Player wins!")
    print(" ")
    again = input("Again? y/n: ")
    if again == "y":
        print(" ")
        run()
    

def run():
    player_choice = input("Choose rock, Spock, paper, lizard, or scissors: ")
    rpsls(player_choice)

run()
    
    
