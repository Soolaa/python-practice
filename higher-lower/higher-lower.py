from random import randint
from instagram_top_accounts import data

# Get the number of accounts
number_of_accounts = len(data)


# Choose two random accounts
random_account1 = randint(1,number_of_accounts)
random_account2 = randint(1,number_of_accounts)
if random_account1 == random_account2:
    random_account2 = randint(1,number_of_accounts)

current_score = 0

followers_a = data[random_account1]["follower_count"]
followers_b = data[random_account2]["follower_count"]


# compare and return
def compare(account1, account2, current_score=0):
    print(f"Compare A: {data[account1]['name']}, a {data [account1]['description']}, from {data[account1]['country']}")
    print(f"Against B: {data[account2]['name']}, a {data [account2]['description']}, from {data[account2]['country']}")

    while True:
        guess = input("Who has more followers? Type 'A' or 'B':").upper()
        if guess in ("A", "B"):
            break
        else:
            print("Please type 'A' or 'B'")

    if (guess == "A" and followers_a > followers_b) or \
            (guess == "B" and followers_b > followers_a):
        current_score += 1
        print (f"You are right! current score: {current_score}")
        account1 = account2
        account2 = randint(1,number_of_accounts)
        return(compare(account1, account2, current_score))

    else:
        print(f"Sorry, that's wrong! Final score: {current_score}")
        return current_score



compare(random_account1,random_account2)