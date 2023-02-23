# Hangman game
# Maciej Błażejczak MBQA
import random
from words import word_list
from hangman_art import stages, logo

print(logo)

chosen_word = random.choice(word_list)
lives = 6
word_to_guess = list(len(chosen_word) * '_')
print("word_to_guess", word_to_guess)
while lives > 0:
    guessed_letter = input("Guess a letter").lower()
    if guessed_letter in word_to_guess:
        print("You already guessed that letter, try again...")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            word_to_guess[position] = letter
    print(word_to_guess)
    if '_' not in word_to_guess:
        print("You won")
        exit()
    if guessed_letter not in chosen_word:
        lives = lives - 1
        print(f"You guessed '{guessed_letter}', there is no '{guessed_letter}' in the word.\n "
              f"You lose a life, {lives} lives left.")
        print('---------')
        print(stages[lives])
print(f"You lose...\n"
      f"Secret word is {chosen_word}")
