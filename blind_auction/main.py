# Blind auction
# Maciej Błażejczak MBQA
# inspired by 100 days of code challenge
from title import title
print(title)
print("Welcome to the secret auction program.")
gamers = dict()
name = input("What is your name?")
bid = input("What is your bid?")
gamers.update({name: bid})
decision = input("Are they any other bidders? Type 'yes' or 'no'.")

while decision == 'yes':
    name = input("What is your name?")
    bid = input("What is your bid?")
    gamers.update({name: bid})
    decision = input("Are they any other bidders? Type 'yes' or 'no'.")

for key, value in gamers.items():
    value_max = max(gamers.values())
    if gamers[key] == value_max:
        print(f"{key} WON with bid {value_max}")









