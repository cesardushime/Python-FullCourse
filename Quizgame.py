def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print(key)
        for option in options[question_num - 1]:
            print(option)
        question_num += 1
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        guesses.append(user_answer)
        correct_guesses += check_answer(questions[key], user_answer)
        question_num += 1
    display_score(correct_guesses, len(questions))

def check_answer(question_answer, user_answer):
    if question_answer == user_answer:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

def display_score(correct_guesses, total_questions):
    score = (correct_guesses / total_questions) * 100
    print(f"You got {correct_guesses} correct out of {total_questions} questions.")
    print(f"Your score: {score}%")

def play_again():
    play = input("Do you want to play again? (yes/no): ").lower()
    return play == "yes"

questions = {
    "Who created Python?": "A",
    "What year was Python created?: ": "B",
    "Python is attributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [
    ["A. Guido Van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]
]

def start_game():
    while True:
        new_game()
        if not play_again():
            print("Thanks for playing!")
            break

start_game()
