from caesar_cipher.letters import letters


def caesar_cipher(word, shift, encode):
    new_word = ''
    for letter in word:
        number = letters.index(letter)
        if encode:
            if number + shift > len(letters):
                result = (number + shift) % len(letters)
                letter = letters[result]
            else:
                letter = letters[number + shift]
        else:
            if number - shift < len(letters):
                result = (number - shift) % len(letters)
                letter = letters[result]
            else:
                letter = letters[number - shift]
        new_word = new_word + letter
    return print(f"Your word is {new_word}")
