import random
import os
import logo
import game_database

print(logo.game_logo)
print("\n")

#Here Define the first score is 0.
score = 0

#defining the function for database to fetch the data
def display_accountinfo(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

#defining the function to check the answer
def check_answer(guess, follower_1, follower_2):
    #checking the conditions
    if follower_1 < follower_2:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess == 1:
            return True
        else:
            return False

#This is for getting the account_2 first after 1 round
account_2 = random.choice(game_database.data)

#This Flag is define to run the game repeatedly after completing each round
continue_flag = True
while continue_flag:
    account_1 = account_2
    account_2 = random.choice(game_database.data)

    #This is done to avoid getting a bug of same accounts to compare
    while account_1 == account_2:
        account_2 = random.choice(game_database.data)

    #Now comparing between accounts start from here
    print(f"Compare 1 : {display_accountinfo(account_1)} \n")
    print(logo.vs)
    print("\n")
    print(f"Compare 2 : {display_accountinfo(account_2)} \n")

    guess = int(input("Who has more Followers ? Type '1' or '2' : "))
    #Fetching the follower counts from database
    follower_count_1 = account_1["follower_count"]
    follower_count_2 = account_2["follower_count"]

    is_correct = check_answer(guess, follower_count_1, follower_count_2)

    #To clear the previous Output
    os.system('cls')

    #To increment the score and end the game
    if is_correct:
        score += 1
        print(f" You are Right! Your Score is : {score} \n")
    else:
        print(f" You are Wrong! Your Final Score is: {score} \n")
        continue_flag = False