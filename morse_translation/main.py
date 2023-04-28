# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A':  '.-', 'B':  '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ', ': '--..--', '.': '.-.-.-',
                    '?': '..--..', '/': '-..-.', '-': '-....-',
                    '(': '-.--.', ')': '-.--.-'}


# Function to encrypt
def encrypt(word_in_english):
    result = []
    for letter in word_in_english.upper():
        if letter in MORSE_CODE_DICT.keys():
            result.append(MORSE_CODE_DICT[letter])
        else:
            result.append(None) # if symbol isn't in MORSE_CODE_DICT, append None
    return result


# Function to decrypt
def decrypt(word_in_morse):
    result = []
    # Extract all the pairs in different lists based on their type, so that they can be easily matched via index()
    letters = list(MORSE_CODE_DICT.keys())
    combinations = list(MORSE_CODE_DICT.values())
    for combination in word_in_morse.split():
        if combination in MORSE_CODE_DICT.values():
            # key = list(filter(lambda i: MORSE_CODE_DICT[i] == combination, MORSE_CODE_DICT))[0] # neat way
            i = combinations.index(combination)
            result.append(letters[i])
        else:
            result.append(None)
    return result


print("Welcome to the Morse code translator.\n")
while True:
    word = input("Give me a word to decrypt/encrypt: ")
    command = input("Press one of the following to continue(e->encrypt, d->decrypt, q-quit)\n")
    if command == 'q':
        break

    # A neat way of checking if the word contains characters that are in MORSE_CODE_DICT (works only with encryption)
    # elif not set(word).issubset(set(MORSE_CODE_DICT)):
    #     print("There are symbols in the word that cannot be translated. \n")
    #     continue

    elif command == 'e':
        translated_word = encrypt(word)
        if all(translated_word):  # check the integrity of translated_word(list)
            print(f"Returned word: {' '.join(translated_word)}")
        else:
            print("There are symbols in the word that cannot be translated.\n")

    elif command == 'd':
        translated_word = decrypt(word)
        if all(translated_word):
            print(f"Returned word: {''.join(translated_word)}")
        else:
            print("There are symbols in the word that cannot be translated. \n")

    else:
        print("Command not found.Try again.\n")
