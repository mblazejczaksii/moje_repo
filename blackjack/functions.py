# function to generate deck of cards
def generate_deck():
    list_of_keys = []
    list_of_values = []
    # generate keys - each key is a different card
    for key in range(1, 53):
        key = str(key)
        list_of_keys.append(key)
    # generate values - value for each card in range from '2' to '[1, 11]'
    counter = 4
    while counter > 0:
        for value in range(2, 15):
            value = int(value)
            list_of_values.append(value)
        counter -= 1
    deck = {k: v for k, v in zip(list_of_keys, list_of_values)}
    # for Jack, Queen and King value is 10
    for key, value in deck.items():
        if deck[key] > 10:
            value = 10
            deck.update({key: value})
    # fro aces value is '[1, 11]'
    for key, value in deck.items():
        if key in ('13', '26', '39', '52'):
            value = [1, 11]
            deck.update({key: value})
    return deck
