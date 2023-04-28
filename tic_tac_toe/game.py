class Game:

    def __init__(self):
        """ Initializes a Game object(board = 3x3 grid of the game; winning_combos = \
        all the possible winning combinations)"""

        self.board = [["e"]*3, ["e"]*3, ["e"]*3]
        self.winning_combos = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 5, 9],
            [3, 5, 7],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
        ]

    def display_board(self):
        """
        displays the current board
        """
        row_counter = 0
        symbol_counter = 0
        for row in self.board:
            for symbol in row:
                if symbol == 'e':
                    print('  ', end=' ')
                elif symbol == 'x':
                    print(" x", end=" ")
                else:
                    print(" o", end=" ")
                if symbol_counter < 2:
                    print('|', end='')
                    symbol_counter += 1
                else:
                    symbol_counter = 0
            if row_counter < 2:
                print("\n-----------")
                row_counter += 1
            else:
                row_counter = 0

    def check_win(self, positions) -> bool:
        """
        Checks if the positions attribute of a Player object contains a winning combination

        :param positions: positions attribute of a Player object
        :return: True if positions contains a winning combination else False
        """

        for combo in self.winning_combos:
            combo = set(combo)
            if combo.issubset(positions):
                return True

        return False

    def check_availability(self, position, symbol) -> bool:
        """
        Checks if a position is available

        :param position:  position to be inserted
        :param symbol: the symbol attribute of the current player
        :return: True if available else False
        """
        if position in range(1, 10):  # checks if position is out of range
            row = int((position - 1) / 3)
            col = position % 3 - 1
            if self.board[row][col] == 'e':  # checks if cell is empty
                self.board[row][col] = symbol  # fills an empty cell
                return True
        return False
