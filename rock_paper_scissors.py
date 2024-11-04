#Defining game choices "rock","paper" and "scissors"
#print(choices)
import random

# Define the prompt message
prompt = 'Welcome to Rock, Paper, Scissors!\nType "quit" to exit the game\nType "rock", "paper", or "scissors" to play:'

# Initialize scores
user_wins = 0
computer_wins = 0
ties = 0

# Function to display final scores
def scores():
    print(f'\nFinal Score - You: {user_wins}, Computer: {computer_wins}, Ties: {ties}')

# Game loop to get users input
while True:
    
    users_choice = input(prompt)
    if users_choice.lower() == 'quit':
        scores()
        break

    
    if users_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please try again.")
        continue

    
    choices = ["rock", "paper", "scissors"]
    computers_choice = random.choice(choices)
    
    print(f"\nYou chose: {users_choice}")
    print(f"Computer chose: {computers_choice}\n")

    # Determine the winner
    if users_choice == computers_choice:
        print("It's a tie!")
        ties += 1
    elif (users_choice == 'rock' and computers_choice == 'scissors') or \
         (users_choice == 'scissors' and computers_choice == 'paper') or \
         (users_choice == 'paper' and computers_choice == 'rock'):
        print("You win!")
        user_wins += 1
    else:
        print("Computer wins!")
        computer_wins += 1





