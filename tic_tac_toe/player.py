class Player:
    def __init__(self, symbol: str, number: int):
        """
        Initializes a Player object(positions = list containing all  the cells occupied by the player's symbol)

        :param symbol: The symbol of the player('x' or 'o')
        :param number: The number of the player ('1' or '2')
        """
        self.symbol = symbol
        self.positions = []
        self.number = number
