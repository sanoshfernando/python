from tkinter.font import names

import art
import game_data
import random

winner_follow_count=0
game_state=True

def game_charactor():
    global name,follower_count,country,description
    game_len=len(game_data.data)
    figure =game_data.data[random.randint(0,game_len-1)]
    name=figure["name"]
    follower_count = figure["follower_count"]
    description = figure["description"]
    country=figure["country"]
    print(f": {name}, {description}, from {country}")
    winner_data()

def winner_data():
    global winner_follow_count, winner_name, winner_description,winner_country
    if winner_follow_count<follower_count:
        winner_follow_count=follower_count
        winner_name = name
        winner_description = description
        winner_country = country
    winner_option.append(follower_count)

def game_logic():
    choice=input("Who has more followers? Type 'A' or 'B':").upper()

    if winner_option[0]>=winner_option[1] and choice=="A":
        print(f"You're right! Current score: {game_count-1}","\n"*20)
    elif winner_option[0]<=winner_option[1] and choice=="B":
        print(f"You're right! Current score: {game_count-1}","\n"*20)
    else:
        print("\n"*20,art.logo,f"Sorry, that's wrong. Final score: {game_count-1}")
        global game_state
        game_state=False
print(art.logo)

game_count=0

while game_state==True:
    game_count+=1

    print("Compare A",end="")
    if game_count>1:
        print(f": {winner_name}, {winner_description}, from {winner_country}")
        winner_option.remove(min(winner_option))
    else:
        winner_option = []
        game_charactor()
    print(art.vs)
    print("Compare B", end="")
    game_charactor()
    game_logic()


