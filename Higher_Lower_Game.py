data = [
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 600,
        "description": "Footballer",
        "country": "Portugal"
    },
    {
        "name": "NASA",
        "follower_count": 94,
        "description": "Space Agency",
        "country": "United States"
    },
    {
        "name": "Narendra Modi",
        "follower_count": 90,
        "description": "Prime Minister",
        "country": "India"
    },
    {
        "name": "Selena Gomez",
        "follower_count": 420,
        "description": "Musician and Actress",
        "country": "United States"
    },
    {
        "name": "Pankaj Tripathi",
        "follower_count": 5,
        "description": "Actor",
        "country": "India"
    },
    {
        "name": "Lionel Messi",
        "follower_count": 480,
        "description": "Footballer",
        "country": "Argentina"
    },
    {
        "name": "Beyoncé",
        "follower_count": 315,
        "description": "Musician",
        "country": "United States"
    },
    {
        "name": "T-Series",
        "follower_count": 245,
        "description": "Music Label & Movie Studio",
        "country": "India"
    },
    {
        "name": "Neeraj Chopra",
        "follower_count": 6,
        "description": "Athlete",
        "country": "India"
    },
    {
        "name": "Justin Bieber",
        "follower_count": 293,
        "description": "Musician",
        "country": "Canada"
    },
    {
        "name": "Fit Tuber",
        "follower_count": 7,
        "description": "YouTuber",
        "country": "India"
    },
    {
        "name": "Taylor Swift",
        "follower_count": 267,
        "description": "Musician",
        "country": "United States"
    },
    {
        "name": "Jennifer Lopez",
        "follower_count": 249,
        "description": "Musician and Actress",
        "country": "United States"
    },
    {
        "name": "Shakira",
        "follower_count": 87,
        "description": "Musician",
        "country": "Colombia"
    },
    {
        "name": "ISRO",
        "follower_count": 1,
        "description": "Space Agency",
        "country": "India"
    },
    {
        "name": "Virat Kohli",
        "follower_count": 254,
        "description": "Cricketer",
        "country": "India"
    },
]

print("""
╦ ╦┬┌─┐┬ ┬┌─┐┬─┐  ╦  ┌─┐┬ ┬┌─┐┬─┐  ╔═╗┌─┐┌┬┐┌─┐  
╠═╣││ ┬├─┤├┤ ├┬┘  ║  │ ││││├┤ ├┬┘  ║ ╦├─┤│││├┤   
╩ ╩┴└─┘┴ ┴└─┘┴└─  ╩═╝└─┘└┴┘└─┘┴└─  ╚═╝┴ ┴┴ ┴└─┘  """)

import random
import os

score = 0

def display_account_info(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"

def check_answer(guess, followers_1, followers_2):
    if followers_1 < followers_2:
        return guess == '2'
    else:
        return guess == '1'

account2 = random.choice(data)
game_active = True

while game_active:
    account1 = account2
    account2 = random.choice(data)

    while account1 == account2:
        account2 = random.choice(data)

    print(f"Compare 1: {display_account_info(account1)}")
    print("\n")
    print(r"""
         __    
 /\   /\/ _\  
 \ \ / /\ \    
  \ V / _\ \   
   \_/  \__/   """)
    print("\n")

    print(f"Compare 2: {display_account_info(account2)}")

    guess = input("Who has more followers? Type 1 or 2: ")
    followers_count_1 = account1["follower_count"]
    followers_count_2 = account2["follower_count"]

    is_correct = check_answer(guess, followers_count_1, followers_count_2)
    os.system("cls")
    print("""
╦ ╦┬┌─┐┬ ┬┌─┐┬─┐  ╦  ┌─┐┬ ┬┌─┐┬─┐  ╔═╗┌─┐┌┬┐┌─┐  
╠═╣││ ┬├─┤├┤ ├┬┘  ║  │ ││││├┤ ├┬┘  ║ ╦├─┤│││├┤   
╩ ╩┴└─┘┴ ┴└─┘┴└─  ╩═╝└─┘└┴┘└─┘┴└─  ╚═╝┴ ┴┴ ┴└─┘  """)

    if is_correct:
        score += 1
        print(f"You are right! Your score is {score}.")
    else:
        print(f"You are wrong. Final score is {score}.")
        game_active = False
