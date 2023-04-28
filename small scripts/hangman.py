import random

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
''')
word_list = ["banana","apple", "orange", "red"]

chosen_word = random.choice(word_list)

prototype_of_chosen_word = []
marker = []
for _ in range (len(chosen_word)):
    prototype_of_chosen_word.append("_")
    marker.append(False)

print(*prototype_of_chosen_word, sep=" ")

guesses = set()
letter_by_position = {}
lives = 5

for idx,letter in enumerate(chosen_word):
    if letter not in letter_by_position:
        letter_by_position[letter] = []
    letter_by_position[letter].append(idx) 


while True:
    
    if all(marker):
        print("You won.")
        break
    
    if lives == 0:
        print()
        print("You lose.")
        print('''


      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___

        ''')
        break

    print()
    guess = input("Try to guess a letter\n").lower()
    
    if guess in guesses:
        print("Letter already used.Try again")
        continue
    
    if guess in chosen_word:

        for value in letter_by_position[guess]:
            prototype_of_chosen_word[value] = guess
            marker[value] = True

        print(*prototype_of_chosen_word, sep = ' ')
        
    else :
        print("Wrong.")
        lives -= 1

    guesses.add(guess)