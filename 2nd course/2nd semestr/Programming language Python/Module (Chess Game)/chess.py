import os


def clear_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

class Game:
    def start(self):
        clear_terminal()
        board = Board()
        board.get()
    """Base class for game logic (can be extended for specific games)."""
    pass

class Board(Game):
    """Represents the game board with its structure and functionalities."""

    map_symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    map_numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    empty_space = ' '  # Clearer naming for empty space representation

    def __init__(self):
        """Creates the map dictionary with all combinations as keys and empty_space as values."""
        self.map = {symbol + number: self.empty_space for symbol in self.map_symbols for number in self.map_numbers}
        #self.map = {symbol + number: symbol + number for symbol in self.map_symbols for number in self.map_numbers}

    def get_board(self):
        """Prints the formatted game board to the console."""
        symbols_lane = '    A   B   C   D   E   F   G   H    '
        top_border = '  ┏━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┓ '
        bottom_border = '  ┗━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┛ '
        middle_border = '  ┣───┼───┼───┼───┼───┼───┼───┼───┫ '

        print(symbols_lane)
        print(top_border)

         # Loop through rows (assuming 8 rows based on map_numbers)
        for row_number in range(1, 9):
            row_string = f"{row_number} ┃ "
            for symbol in self.map_symbols:
                cell_value = self.map[symbol + str(row_number)]
                if symbol is not 'h':
                    row_string += f"{cell_value} | "
                else:
                    row_string += f"{cell_value} ┃ {row_number}"
            row_string += f" ┃ {row_number}"
            
            if row_number is not 1:
                print(middle_border)
            print(row_string[:-3])  # Remove trailing whitespace and pipe

        print(bottom_border)
        print(symbols_lane)
        
    def get_map(self):
        """Prints the internal map dictionary representation (for debugging purposes)."""
        print(self.map)
        
    def get(self):
        self.get_map()
        self.get_board()


class Piece(Game):
    pass

class Horse(Piece):
    pass

game = Game()
game.start()