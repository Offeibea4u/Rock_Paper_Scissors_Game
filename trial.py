import random

def game():
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors) or 'quit' to exit: ").lower()
        
        if user_choice == 'quit':
            break
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please try again.")
            continue
        
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
        else:
            print("Computer wins!")




