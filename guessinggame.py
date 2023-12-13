while True:
    secret_number = 9
    guess_count = 0
    guess_limit = 5
    while guess_count < guess_limit:
        guess = int(input('Guess '))
        guess_count += 1
        print((f"remaining {guess_limit - guess_count} guesses"))
        if guess == secret_number:
            print('You won!')
            print(str.upper("You are a master of the Game"))
            break
    else:
        print('Sorry, you failed!')

        play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!!")
        break






