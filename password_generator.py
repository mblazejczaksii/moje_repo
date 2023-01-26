# simple password generator
# Maciej Błażejczak MBQA

import string
import random

# General questions asked by computer
amount_of_letters = int(input('How many letters password should contain?'))
amount_of_digits = int(input('How many digits password should contain?'))
amount_of_punctuation = int(input('How many special marks password should contain?'))

# Variables contain data necessary to build a password
letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
len_letters = len(letters)
len_digits = len(digits)
len_punctuation = len(punctuation)

# Counters to help count during loop
counter_letters = counter_digits = counter_punctuation = 0

# Final variable
password = ''
# While loops

while counter_letters < amount_of_letters:
    password += letters[random.randint(0, len_letters - 1)]
    counter_letters += 1

while counter_digits < amount_of_digits:
    password += digits[random.randint(0, len_digits - 1)]
    counter_digits += 1

while counter_punctuation < amount_of_punctuation:
    password += punctuation[random.randint(0, len_punctuation - 1)]
    counter_punctuation += 1

# Password is ready, but it should be shuffled
# Shuffling password - creating an ascending list then shuffle it, then transform it into a string
password = sorted(password)
random.shuffle(password)
password = ''.join(password)
if len(password) == 0:
    print(f'Password with 0 marks is not a password, but your wish is my order :)')
else:
    print('Your password: ', password)
