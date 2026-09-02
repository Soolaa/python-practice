from random import randint
import art

EASY_LEVEl_TURNS = 10
HARD_LEVEl_TURNS = 5

def check_answer(user_guess, actual_answer , turns):
    """ Check answer against guess, returns the number of turns remaining. """
    if user_guess > actual_answer:
        print("Too high!")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low!")
        return turns - 1
    else:
        print("You guessed the number! Well done!")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEl_TURNS
    if level == "hard":
        return HARD_LEVEl_TURNS
    return None

def game():
    print(art.logo)
    print("wellcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    # Choosing a random number
    answer = randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess , answer , turns)
        if turns == 0:
            print("You run out of guesses! you lose.")
            return

game()

