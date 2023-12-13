import random

def get_player_choice():
    # This function prompts the player for their choice and validates it
    while True:
        player = input("rock, paper, scissors?: ").lower()
        if player in ["rock", "paper", "scissors"]:
            return player
        else:
            print("Invalid choice! Please choose rock, paper, or scissors.")

def determine_winner(player, computer):
    # This function determines the winner based on the choices made by the player and computer
    if player == computer:
        return "Tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    # This function controls the game loop
    while True:
        choices = ["rock", "paper", "scissors"]
        computer = random.choice(choices)
        player = get_player_choice()

        print("Computer:", computer)
        print("Player:", player)

        result = determine_winner(player, computer)
        print(result)

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing!")

# This conditional ensures that the game is only executed if this script is run directly
if __name__ == "__main__":
    play_game()
