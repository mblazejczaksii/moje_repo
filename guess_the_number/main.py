# Guess the number
# Maciej Błażejczak MBQA
# inspired by 100 days of code challenge

import random
from title import title

NUMBER = random.randint(0, 100)


def play_game():
    print(title)
    print("Welcome to the Number Guessing Game!\n"
          "I'm thinking of a number between 1 and 100.")
#   print(f"Pssst, the correct answer is {NUMBER}")
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard':")
    if difficulty_level == 'easy':
        attempts = 10
        print(f"You have {attempts} attempts remaining to guess the number. ")
    else:
        attempts = 5
        print(f"You have {attempts} attempts remaining to guess the number. ")

    def check_attmepts():
        if attempts == 0:
            return True

    guess = input("Make a guess:")
    if int(guess) == NUMBER:
        print("YOU WIN")
    else:
        while int(guess) != NUMBER:
            if int(guess) < NUMBER:
                print("Too low...")
                attempts -= 1
                if check_attmepts():
                    print("No more lives, You loose...")
                    break
                else:
                    print(f"Guess again.\n"
                          f"You have {attempts} attempts remaining to guess the number. ")
                guess = input("Make a guess: ")

            elif int(guess) > NUMBER:
                print("Too high...")
                attempts -= 1
                if check_attmepts():
                    print("No more lives, You loose...")
                    break
                else:
                    print(f"Guess again.\n"
                          f"You have {attempts} attempts remaining to guess the number. ")
                guess = input("Make a guess:")
        else:
            print("YOU WIN!!!")
    play_again = input("Do you want to play again? type 'yes' or 'no'...")
    if play_again == 'yes':
        play_game()


play = input("Do you want to play a game? type 'yes' or 'no'...")
if play == 'yes':
    play_game()
else:
    print("Bye...")
