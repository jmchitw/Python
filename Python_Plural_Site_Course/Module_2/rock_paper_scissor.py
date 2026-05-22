import random

user_choice = ''

while user_choice != 'quit':
    choice = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choice)
    user_choice = input("\nEnter your choice (rock, paper, scissors, quit): ")
    if user_choice == computer_choice:
        print(f"\nComputer chose {computer_choice}. It's a tie!\n")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print(f"\nComputer chose {computer_choice}. You win!\n")
    elif (user_choice == 'quit'):
        print("\nThanks for playing! Goodbye!\n")
        break
    else:
        print(f"\nComputer chose {computer_choice}. Computer wins!\n")