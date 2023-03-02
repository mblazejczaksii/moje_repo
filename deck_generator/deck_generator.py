# functions to generate deck of cards
# function 'how_many_decks' returns aces positions
# function 'generate_decks' returns card decks
def how_many_decks(number):
    """
    :param number: how many decks generate
    :return: aces positions
    """
    aces = 4 * number
    aces_position = []
    while aces > 0:
        ace = str(aces * 13)
        aces_position.append(ace)
        aces -= 1
    return aces_position


def generate_decks(number=1):
    """
    :param number: how many decks generate
    :return: dictionary where 'key' is a card number and 'value' is a card value
    """
    list_of_keys = []
    list_of_values = []
    # generate keys - each key is a different card
    for key in range(1, number * 53):
        key = str(key)
        list_of_keys.append(key)
    # generate values - value for each card in range from '2' to '[1, 11]'
    counter = number * 4
    while counter > 0:
        for value in range(2, 15):
            value = int(value)
            list_of_values.append(value)
        counter -= 1
    deck = {k: v for k, v in zip(list_of_keys, list_of_values)}
    print("deck: ", deck)
    # for Jack, Queen and King value is 10
    for key, value in deck.items():
        if deck[key] > 10:
            value = 10
            deck.update({key: value})
    print("deck: ", deck)
    # for aces value is '[1, 11]'
    for key, value in deck.items():
        if key in how_many_decks(number=number):
            value = [1, 11]
            deck.update({key: value})
    return deck


def bet():
    bet_container = 0
    # Starting with 1000$
    your_cash = opponent_cash = 1000
    bet = input(f"You have {your_cash}$. How much you want to bet?")
    while not bet.isdigit() or float(bet) > your_cash:
        bet = input(f"You have only {your_cash}$ and 'bet' should be a number")
    print(f"You bet {bet}$")
    # Decrease your and your opponent cash by a bet
    your_cash -= int(bet)
    opponent_cash -= int(bet)
    # Store your and your opponent cash into bet_container
    bet_container += bet * 2
    return bet_container
