import higher_lower_data
import os, random

def clear(): 
    os.system('cls') 

def format_data(account):
    """Takes an account and returns a formatted set of data"""
    return "{}, a {}, from {}".format(account["name"], account["description"], account["country"])

# def check_answer(guess, a_followers, b_followers):
#     """Takes the user guess and follower counts and returns True if correct"""
#     if a_followers > b_followers:
#         return guess == 'a'
#     else:
#         return guess == 'b'

def play_game():

    print(higher_lower_data.logo)
    score = 0
    person1 = random.choice(higher_lower_data.data)
    person2 = random.choice(higher_lower_data.data)

    while (True):
        if (person1 == person2):
            person2 = random.choice(higher_lower_data.data)

        print("Compare A : {}.".format(format_data(person1)))

        print(higher_lower_data.vs)

        print("Against B: {}".format(format_data(person2)))

        answ = input("Who has more followers? Type 'A' or 'B': ").title()

        if (answ == 'A' and person1["follower_count"] > person2["follower_count"])\
            or (answ == 'B' and person1["follower_count"] < person2["follower_count"]):

        #ALTERNATIVE
        #if check_answer(answ, person1["followers_count"], person2["followers_count"]):
            score += 1

            if (answ == 'A'):
                person2 = random.choice(higher_lower_data.data)
            else :
                person1 = person2
                person2 = random.choice(higher_lower_data.data)

            clear()
            print(higher_lower_data.logo)
            print("You're right! Current score: {}".format(score))

        else:
            clear()
            print(higher_lower_data.logo)
            print("Sorry, that's wrong. Final score: {}".format(score))
            break

play_game()