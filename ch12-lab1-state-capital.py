# Tim Lucas
# Lab 12-1 
# 2025-07-03

STATES_CAPITALS = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
}

def main():
    print("State Capital Game")
    print()

    correct = 0
    incorrect = 0

    for key in STATES_CAPITALS:
        guess = input(f"What is the capital of {key}?\nType your answer: ")
        if guess == STATES_CAPITALS[key]:
            print()
            print("Good Job!")
            print()
            correct += 1
        else:
            print()
            print(f"Sorry the answer is {STATES_CAPITALS[key]}")
            print()
            incorrect += 1
    print(f"You answered {correct} correctly, and {incorrect} incorrectly.")            


# after all states have been presented, display number of correct and incorrect answers


main()