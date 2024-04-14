import os
from abc import ABC, abstractmethod

def clear_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def move():
    pass

class Game(ABC):
    def start(self):
        clear_terminal()
        board = Board()
        board.get()
        close_game = False
        while close_game == False:
            
            board.update()
            board.get()
            close_game = True
            
    """Base class for game logic (can be extended for specific games)."""
    pass

class Board(Game):
    """Represents the game board with its structure and functionalities."""

    map_symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    map_numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    empty_space = ' '  # Clearer naming for empty space representation
    map = {symbol + number: ' ' for symbol in map_symbols for number in ['1', '2', '3', '4', '5', '6', '7', '8']}
    
    def __init__(self):
        """Creates the map dictionary with all combinations as keys and empty_space as values."""
        pawn_init_positions = [symbol + number for number in ['2', '7'] for symbol in self.map_symbols ]

        for i, position in enumerate(pawn_init_positions[0:8]):
            pawn_name = f"pawn_{i+1}"  # Використання f-string для форматування індексу
            pawn = Pawn(position=position, color='white')
            setattr(self, pawn_name, pawn)  # Використання setattr() для створення атрибута

        for i, position in enumerate(pawn_init_positions[8:16]):
            pawn_name = f"pawn_{i+8+1}"
            pawn = Pawn(position=position, color='black')
            setattr(self, pawn_name, pawn)
        

    def get_board(self):
        """Prints the formatted game board to the console."""
        symbols_lane = '    A   B   C   D   E   F   G   H    '
        top_border = '  ┏━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┳━━━┓ '
        bottom_border = '  ┗━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┛ '
        middle_border = '  ┣───┼───┼───┼───┼───┼───┼───┼───┫ '

        print(symbols_lane)
        print(top_border)

         # Loop through rows (assuming 8 rows based on map_numbers)
        for row_number in range(1, 9)[::-1]:
            row_string = f"{row_number} ┃ "
            for symbol in self.map_symbols:
                if hasattr(self.map[symbol + str(row_number)], 'obj'):
                    cell_value = self.map[symbol + str(row_number)].symbol
                else: cell_value = self.map[symbol + str(row_number)]
                if symbol is not 'h':
                    row_string += f"{cell_value} | "
                else:
                    row_string += f"{cell_value} ┃ {row_number}"
            row_string += f" ┃ {row_number}"
            
            if row_number is not 8:
                print(middle_border)
            print(row_string[:-3])  # Remove trailing whitespace and pipe

        print(bottom_border)
        print(symbols_lane)
        
    def get_map(self):
        """Prints the internal map dictionary representation (for debugging purposes)."""
        print(self.map)
        
    def get_map_as_symbols(self):
        for key, value in self.map.items():
            if hasattr(value, 'obj'):
                self.map[key] = value.symbol
        print(self.map)     
        
    def get(self):
        self.get_map()
        self.get_map_as_symbols()
        self.get_board()
        
    def update(self):
        #for position in self.map.keys():
        for pawn in Pawn.get_all():
            self.map[pawn.position] = pawn


class Piece(Game):
    obj = True
    
    def __init__(self, position, color):
        self.position = position
        self.color = color
    
    @abstractmethod
    def move(self, result_position):
        self.position = result_position
    

class Pawn(Piece):
    all = []
    
    def __init__(self, position, color):
        self.id = len(Pawn.all) + 1
        Pawn.all.append(self)
        self.position = position
        self.color = color
        if self.color == 'white':
            self.symbol = '♙'
        else: self.symbol = '♟'
        
    def get_all():
        return Pawn.all

    def move(self, result_position):
        if self.move_validation(result_position) == True:
            self.position = result_position
        elif self.move_validation(result_position) == False:
            raise ValueError('It is not possible to move to this position')
        else:
            raise Exception('Unepxected issue in this move')
    
    def move_validation(self, result_position):
        expected_positions = []
        if self.color == 'white':
            if self.position[1] == '2':
                expected_positions += [self.position[0] + number for number in range(3,4)]
            else:
                expected_positions += [str(int(self.position[1]) + 1)]
        elif self.color == 'black':
            if self.position[1] == '7':
                expected_positions += [self.position[0] + number for number in range(5,6)]
            else:
                expected_positions += [str(int(self.position[1]) - 1)]
        else: raise ValueError("Piece's color not defined, or defined incorrectly")
                
        if result_position in expected_positions:
            return True
        elif result_position not in expected_positions:
            return False
        else: raise Exception('Unepxected issue in this validation')
        

game = Game()
game.start()