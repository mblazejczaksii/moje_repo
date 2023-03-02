import random
from title import title


def deal_card():
    """
    :return: returns a random card from the deck
    """
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """
    :param cards: take a cards list
    :return: score returned from cards
    """
    score = sum(cards)
    if score == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        return score
    else:
        return score


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, computer has a BLACKJACK"
    elif user_score == 0:
        return "Win with a BLACKJACK"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Computer went over. You win"
    elif user_score > computer_score:
        return "You won"
    else:
        return "You lose"


def play_game():
    print(title)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(cards=user_cards)
        computer_score = calculate_score(cards=computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Do you want to pick another card? type 'y' or 'n' to decide")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score=user_score, computer_score=computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n'...") == 'y':
    play_game()
