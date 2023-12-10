import random
import art


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You lose"
    elif user_score == computer_score:
        return "It's a draw"
    elif computer_score == 0:
        return "Computer got a Blackjack! Computer wins"
    elif user_score == 0:
        return "You got a Blackjack! You won"
    elif user_score > 21:
        return "You went over! You lose"
    elif computer_score > 21:
        return "Computer went over! You won"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(art.logo)
    user_card = []
    computer_card = []
    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    to_continue = True
    while to_continue:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"Your deck: {user_card} Your score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")
        if computer_score == 0 or user_score == 0 or user_score > 21:
            to_continue = False
        else:
            run = input("Do you want to draw another card? 'y' or 'n': ")
            if run == "y":
                user_card.append(deal_card())
            else:

                to_continue = False

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
    print(f"   Your final hand: {user_card}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  
  play_game()