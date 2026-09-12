import random
from random import randint
from random import choice
from instagram_top_accounts import data
current_score = 0
gam_should_continue = True

# Get the number of accounts
#number_of_accounts = len(data)
def account_information(account):
    """ get account information in separate variables """
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description},from {account_country}"

def check_answer(user_guess, a_followers , b_followers):
    """Check user guess"""
    if a_followers > b_followers:
        return user_guess == 'A'
    else:
        return user_guess == 'B'


account_b = random.choice(data)

while gam_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f" Compare A: {account_information(account_a)}")
    print("VS")
    print(f" Against B: {account_information(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B':").upper()
    print("\n" * 20)

    followers_a = account_a["follower_count"]
    followers_b = account_b["follower_count"]

    is_correct = check_answer(guess, followers_a, followers_b)
    if is_correct:
        current_score += 1
        print (f"You are right! current score: {current_score}")
    else:
        print (f"Sorry, that's wrong! Final score: {current_score}")
        gam_should_continue = False