import random


def play():
    print("Welcome to the Medical Rock, Paper, Scissors Game!")
    print("Rules: Pill crushes Scalpel, Scalpel cuts Prescription, Prescription covers Pill.")

    choices = ['pill', 'scalpel', 'prescription']
    player = input(f"Make your choice [0: pill, 1: scalpel, 2: prescription]: ")

    if player in choices or player == '0' or player == '1' or player == '2':
        computer_choice_number = random.randint(0, 2)
        com_choice = choices[computer_choice_number]
        player_choice = player.lower()
        if player.isnumeric():
            player_choice = choices[int(player)]
        print(f"The computer chose {com_choice}")
        if player_choice == 'pill':
            if com_choice == 'pill':
                print("Draw!")
            elif com_choice == 'scalpel':
                print("You win!")
            elif com_choice == 'prescription':
                print("You lose!")
        elif player_choice == 'scalpel':
            if com_choice == 'pill':
                print("You lose!")
            elif com_choice == 'scalpel':
                print("Draw!")
            elif com_choice == 'prescription':
                print("You win!")
        elif player_choice == 'prescription':
            if com_choice == 'pill':
                print("You win!")
            elif com_choice == 'scalpel':
                print("You lose!")
            elif com_choice == 'prescription':
                print("Draw!")
