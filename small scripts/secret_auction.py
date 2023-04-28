import os
def clear(): 
    os.system('cls') 

def find_highest_bidder(auctions):
  
  highest_bidder = max(auctions.keys(), key = lambda x: auctions[x])
  print ("The highest bidder is {} with a bid of ${}".format(highest_bidder,auctions[highest_bidder]))

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
auctions = {}

while True:
  name = input("What is your name?\n")
  bid = input("How much are you bidding?$\n")

  auctions[name] = int(bid)
  answ = input("Are there any other users,willing to bid?(yes/no)\n")

  if answ == 'no':
    find_highest_bidder(auctions)
    break

  clear()
