# Removing unnecessary spaces from words provided by user and then concatenate those words
# Maciej Błażejczak MBQA

# General questions asked by computer
words_number = input("How many words would you like to concatenate?")
words_number = int(words_number)
words_list = list()
result = str()

# For loop iterates through
for n in range(int(words_number)):
    print(f"Provide wrod number {n + 1}")
    word = input()
    words_list.append(word)

# Presenting words provided by user or exit
if len(words_list) == 0:
    print("You don't want to play with me so our game is over...")
    exit()
else:
    print('Your words list: ', words_list)

# For loop iterates through provided words list
for n in words_list:
    n = (n.rstrip()).lstrip()
    result = result + n + ' '

print('Your result is: ', result)
