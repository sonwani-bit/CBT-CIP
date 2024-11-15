import random

# List of choices
choices = ["rock", "paper", "scissors"]

# Function to get the user's choice
def get_user_choice():
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_input in choices:
        return user_input
    else:
        print("Invalid choice. Please choose either rock, paper, or scissors.")
        return get_user_choice()

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to play the game
def play_game():
    wins = 0
    losses = 0
    ties = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            wins += 1
        elif result == "You lose!":
            losses += 1
        else:
            ties += 1

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    # Print the final scores
    print(f"\nFinal Scores:\nWins: {wins}\nLosses: {losses}\nTies: {ties}")

if __name__ == "__main__":
    play_game()
