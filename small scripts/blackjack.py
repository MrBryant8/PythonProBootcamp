import random, os

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def clear(): 
    os.system('cls') 

def deal_cards(n, cards):
      global deck
      [cards.append(random.choice(deck)) for _ in range(n)]

def calculate_score(cards):
      score = sum(cards)
      if score == 21 and len(cards) == 2:
            return 0
      if 11 in cards and score > 21:
            score -= 10
            cards.append(1)
            cards.remove(11)

      return score
      
def compare(user_score, computer_score):

  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
      user_cards = []
      pc_cards = []
      game_ended = False
      print(logo)
      deal_cards(2, user_cards)
      deal_cards(2, pc_cards)
      user_score = calculate_score(user_cards)
      pc_score = calculate_score(pc_cards)

      while game_ended == False:
            if user_score > 21  or user_score == 0 or pc_score == 0:
                  game_ended = True
            else:
                  print("Your cards: {}, current score: {}".format(user_cards,user_score))
                  print("Computer's first card: {}".format(pc_cards[0]))      
                  another_card = input("Type 'y' to draw another card, 'n' to pass:\n")
                  if another_card == 'y':
                        deal_cards(1, user_cards)
                        user_score = calculate_score(user_cards)
                  elif another_card == 'n':                         
                        game_ended = True

            while pc_score != 0 and pc_score < 17:
                  deal_cards(1, pc_cards)
                  pc_score = calculate_score(pc_cards)

      print("Your final hand: {}, final score: {}".format(user_cards, user_score))
      print("Computer's final hand: {}, final score: {}".format(pc_cards, pc_score))
      print(compare(user_score, pc_score))

while input ("Do u wanna play some blackjack?(y/n)\n") == 'y':
      clear()
      play_game()
      
