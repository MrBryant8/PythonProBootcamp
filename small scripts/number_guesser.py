import random,os

logo = """
 _______               ___.                    ________                                          
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ ______ ___________ 
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___// __ \_  __ \\
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \\  ___/|  | \/
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >\___  >__|   
        \/            \/    \/     \/                \/            \/     \/     \/     \/       
"""

def clear(): 
    os.system('cls') 

def set_difficulty():
    difficulty = input("Choose a difficulty(Type in easy/hard):")
    lives = 0 
    if difficulty == 'easy':
        lives = 10
    elif difficulty == 'hard':
        lives = 5

    return lives

def play_game():
    print(logo)
    print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100")
    number = random.randint(1,100)
    lives = set_difficulty()
    
    while lives != 0:
        print("You have {} remaining attempts to guess the number.".format(lives))
        guess = int(input("Make a guess:"))
        if guess == number:
            print("Woohoo.U guessed right.")
            break
        elif guess < number:
            print("Too low.\nTry again.")
            lives -= 1
        elif guess > number:
            print("Too high.\nTry again.")
            lives -= 1

        if lives == 0:
            print("You lose, you ran out of guesses.The answer was {}".format(number))
        
while input("Do u wanna guess a number?(y/n)\n") == 'y':
    clear()
    play_game()    
