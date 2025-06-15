import art
import random

def pick_num():
    global number
    number = random.randint(1,100)

def game():
    if guess >number:
        print("Too high.\nGuess again.")
    elif guess<number:
        print("Too Low")
    else:
        print(f"You got it! The answer was {number}")
        global Game_state
        Game_state = False

current_attempt = 0
Game_state = True

print(art.logo, "\nWelcome to the Number Guessing Game!", "\nI'm thinking of a number between 1 and 100.")
mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if mode == "easy":
    attempts = 10
else:
    attempts = 5
pick_num()
while current_attempt < attempts and Game_state==True:
    print(f"You have {attempts-current_attempt} attempts remaining to guess the number.")
    current_attempt+=1
    guess = int(input("Make a guess: "))
    game()
if Game_state:
    print("You've run out of guesses, you lose.")


