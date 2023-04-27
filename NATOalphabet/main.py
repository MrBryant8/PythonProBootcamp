import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv") #Smarter using pandas

nato_alphabet = {letter.letter: letter.code for (index, letter) in data.iterrows()}
print(nato_alphabet)

while(True):

    user_input = input("Give me a word:\n").upper()
    if user_input == "QUIT":
        break
    else:
        try:
            word = [nato_alphabet[letter] for letter in user_input]
        except KeyError:
            print("Sorry,only letters in the alphabet allowed.")
            continue
        else:
            print(word)

#Another way of creating the nato_alphabet
# with open("nato_phonetic_alphabet.csv") as f:
#     content = f.readlines()
#
# dict1={}
# for n in content:
#     word = n.split(',')
#     print(word)
#     dict1[word[0]] = word[1].strip()
#
# dict1.pop("letter")
# print(dict1)