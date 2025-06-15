import art
import random
state = "y"
def blackjack():
    print("\n"*100)
    print(art.logo)
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]

    user_choice="y"
    user_cards = [random.choice(cards), random.choice(cards)]
    computer_cards =[random.choice(cards),random.choice(cards)]
    user_tol = sum(user_cards)
    computer_tol = sum(computer_cards)
    print(f"your cards: [{user_cards[0]},{user_cards[1]}] , current score: {user_tol}")
    print(f"Computer's first card: {computer_cards[0]}")


    while user_tol <= 21 and user_choice=="y":
        user_choice = input("Type 'y' to get another card, type 'n' to pass:").lower()
        if user_choice == "y":
            user_cards.append(random.choice(cards))
            user_tol = sum(user_cards)
            print(f"your cards: {user_cards} , current score: {user_tol}")
        else:
            print(f"Your final hand: {user_cards}, final score: {user_tol}")

    while computer_tol <17 and user_tol>computer_tol:
        computer_cards.append(random.choice(cards))
        computer_tol = sum(computer_cards)

    print(f"Computer's final hand: {computer_cards}, final score: {computer_tol}")
    if user_tol>21:
        print("You went over. You Loose 😭")
    elif computer_tol>21:
        print("Opponent went over. You win 😁")
    elif computer_tol>user_tol:
        print("You lose 😤")
    elif computer_tol==user_tol:
        print("DRAW")
    else:
        print("You win 😁")
while state == "y":
    state = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    if state=="y":
        blackjack()
