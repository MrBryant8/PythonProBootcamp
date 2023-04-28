from player import Player
from game import Game
from time import sleep


# Checks if the player has played his turn successfully
def check_turn_successful(player):
    print(f"\nPlayer {player.number}, go!\n")
    position = int(input("Where are you placing your symbol? \n(1-2-3\n4-5-6\n7-8-9)\n"))

    if not game_session.check_availability(position, player.symbol):  # checks if the position is already occupied
        print("\nIllegal placement, try again!\n")
        return False

    player.positions.append(position)
    return True


if __name__ == '__main__':
    user_answer = input("Welcome to my Tic Tac Toe Game!\nWanna start?(y->yes, n-> no)\n")
    while True:
        if user_answer == 'y':

            game_session = Game()
            player1 = Player('x', 1)
            player2 = Player('o', 2)
            turn = 0

            while turn < 9:
                game_session.display_board()  # Displays the current board every turn
                sleep(1)
                if turn % 2 == 0:
                    if not check_turn_successful(player1):
                        turn -= 1

                    elif turn >= 4:  # win could be achieved with 5 turns or more so skips the check on the first 4
                        if game_session.check_win(player1.positions):  # checks if a player won
                            print(f"\nPlayer {player1.number} wins!")
                            break

                else:
                    if not check_turn_successful(player2):
                        turn -= 1

                    elif turn >= 4:
                        if game_session.check_win(player2.positions):
                            print(f"\nPlayer {player2.number} wins!")
                            break
                turn += 1

            if turn == 9:
                game_session.display_board()
                print("\nIt's a draw, fair play.")

            user_answer = input("\nWanna play again?(y->yes, n-> no) ")

        else:
            print("\nSorry to see u go :(")
            break
