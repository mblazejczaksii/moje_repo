from cc_functions import caesar_cipher
from letters import name

print(name)
decision = str(input("Do you want encode or decode the message?"))
word = str(input(f"What message you want to {decision}?"))
shift = int(input("Please provide a shift (number)"))
if (decision.lower()).startswith("e"):
    caesar_cipher(encode=True, word=word, shift=shift)
elif (decision.lower()).startswith("d"):
    caesar_cipher(encode=False, word=word, shift=shift)
else:
    print(f"It looks like You have problem with reading, I said 'encode' or 'decode', not '{decision}'")
    exit()


