import os
from abc import ABC, abstractmethod


def clear_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def get_board_view(board):
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
        for symbol in board.map_symbols:
            cell_value = board.map[symbol + str(row_number)]
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
        
def move(player: str, position_from: tuple, position_to: tuple):
    map = Board.get(Board)
    if position_from in map:
        piece = map[position_from]
        if position_to in map:
            if piece in Piece.all:
                if player is piece.color:
                    piece.move(position_to)
                    map[position_from] = ' '
                else: raise ValueError("U can not move opponent's piece")
            else: raise ValueError('There is no piece in mentioned position')
        else: raise ValueError("Position to move to doesn't exist")
    else: raise ValueError("Position to move from doesn't exist")


class Game(ABC):
    def start(self):
        clear_terminal()
        board = Board()
        close_game = False
        while close_game == False:
            
            get_board_view(board)
            move('white', ('a2'), ('a3'))
            get_board_view(board)
            move('white', ('a3'), ('a4'))
            get_board_view(board)
            move('white', ('a4'), ('a5'))
            get_board_view(board)
            move('white', ('a5'), ('a6'))
            get_board_view(board)
            move('black', ('a7'), ('a5'))
            get_board_view(board)
            move('white', ('a1'), ('a5'))
            get_board_view(board)
            move('white', ('a5'), ('c5'))
            get_board_view(board)
            move('white', ('c5'), ('c7'))
            get_board_view(board)
            move('white', ('b1'), ('c3'))
            get_board_view(board)
            move('black', ('d7'), ('d5'))
            get_board_view(board)
            move('black', ('c8'), ('f5'))
            get_board_view(board)
            move('black', ('f5'), ('c2'))
            get_board_view(board)
            move('white', ('d1'), ('c2'))
            get_board_view(board)
            move('white', ('c2'), ('f5'))
            get_board_view(board)
            move('white', ('f5'), ('h5'))
            get_board_view(board)
            move('white', ('e1'), ('d1'))
            get_board_view(board)
            move('black', ('e8'), ('d7'))
            get_board_view(board)
            move('white', ('h5'), ('h7'))
            get_board_view(board)
            move('white', ('a6'), ('b7'))
            get_board_view(board)
            move('white', ('d2'), ('d4'))
            get_board_view(board)
            move('white', ('d4'), ('d5'))
            get_board_view(board)
            close_game = True
            
    """Base class for game logic (can be extended for specific games)."""
    pass


class Board(Game):
    """Represents the game board with its structure and functionalities."""

    map_symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    map_numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    empty_space = ' '  # Clearer naming for empty space representation
    map = {(symbol + number): ' ' for symbol in map_symbols for number in ['1', '2', '3', '4', '5', '6', '7', '8']}

    def __init__(self):
        """Creates the map initiation array with all positions for objects."""
        self.init_positions = {
            Pawn: [(symbol + number) for number in ['2', '7'] for symbol in self.map_symbols],
            Rook: [(symbol + number) for number in ['1', '8'] for symbol in ['a', 'h']],
            Knight: [(symbol + number) for number in ['1', '8'] for symbol in ['b', 'g']],
            Bishop: [(symbol + number) for number in ['1', '8'] for symbol in ['c', 'f']],
            Queen: [(symbol + number) for number in ['1', '8'] for symbol in ['d']],
            King: [(symbol + number) for number in ['1', '8'] for symbol in ['e']]
        }

        self.setup_pieces()

    def setup_pieces(self):
        """Creates and places pieces on the board."""
        for piece_type, positions in self.init_positions.items():
            for i, position in enumerate(positions):
                piece_name = f"{piece_type.__name__.lower()}_{i + 1}"
                num_pieces_per_color = len(self.init_positions[piece_type]) // 2  # Assuming Pawn is the reference piece type
                piece_color = 'white' if i < num_pieces_per_color else 'black'
                piece = piece_type(position=position, color=piece_color)
                setattr(self, piece_name, piece)
        
    def get(self):
        return self.map


class Piece(Game):
    all = []
    obj = True
    
    def __init__(self, position, color):
        self.position = position
        self.color = color
        Board.map[self.position] = self
        
    def move_on_map_validation(self, result_position):
        if result_position in list(Board.map.keys()):
            return True
        elif result_position not in list(Board.map.keys()): 
            return False
        else: raise Exception('Unepxected issue in this move')

    def move(self, result_position):
        if self.move_on_map_validation(result_position) and self.move_validation(result_position):
            result_position_content = Board.map[result_position]
            if result_position_content in Piece.all:
                Piece.all.remove(result_position_content)
            self.position = result_position
            Board.map[self.position] = self
        else: raise ValueError('It is not possible to move to this position')
    
    def __repr__(self) -> str:
        return self.symbol
    
    @abstractmethod
    def move_validation(self, result_position):
        if True:
            return True
        else: return False
    

class Pawn(Piece):
    all = []
    
    def __init__(self, position, color):
        self.id = len(Pawn.all) + 1
        Pawn.all.append(self)
        Piece.all.append(self)
        self.position = position
        self.color = color
        Board.map[self.position] = self
        if self.color == 'white':
            self.symbol = '♙'
        elif self.color is 'black':
            self.symbol = '♟'
        else: raise ValueError('Color not defined')
        
    def get_all():
        return Pawn.all
    
    def move_validation(self, result_position):
        symbol, number = result_position[0], int(result_position[1])

        if self.color == 'white':
            if number == int(self.position[1]) + 1:
                # Normal move forward by one square
                if Board.map[result_position] not in Piece.all:
                    return True
                elif Board.map[result_position].color is not self.color:
                    return True
                else: 
                    return False
            elif number == int(self.position[1]) + 2 and self.position[1] == '2':
                # Move forward by two squares if on starting position
                if Board.map[result_position] not in Piece.all:
                    return True
                elif Board.map[result_position].color is not self.color:
                    return True
                else: 
                    return False
            elif number == int(self.position[1]) + 1:
                # Diagonal capture (one square forward and to the left or right)
                adjacent_columns = [chr(ord(symbol) + i) for i in (-1, 1) if 'a' <= chr(ord(symbol) + i) <= 'h']
                return result_position[0] in adjacent_columns and Board.map[result_position] in Piece.all
            else:
                return False
        elif self.color == 'black':
            if number == int(self.position[1]) - 1:
                # Normal move forward by one square
                if Board.map[result_position] not in Piece.all:
                    return True
                elif Board.map[result_position].color is not self.color:
                    return True
                else: 
                    return False
            elif number == int(self.position[1]) - 2 and self.position[1] == '7':
                # Move forward by two squares if on starting position
                if Board.map[result_position] not in Piece.all:
                    return True
                elif Board.map[result_position].color is not self.color:
                    return True
                else: 
                    return False
            elif number == int(self.position[1]) - 1:
                # Diagonal capture (one square forward and to the left or right)
                adjacent_columns = [chr(ord(symbol) + i) for i in (-1, 1) if 'a' <= chr(ord(symbol) + i) <= 'h']
                return result_position[0] in adjacent_columns and Board.map[result_position] in Piece.all
            else:
                return False
            

class Rook(Piece):
    all = []
    
    def __init__(self, position, color):
        self.id = len(Rook.all) + 1
        Rook.all.append(self)
        Piece.all.append(self)
        self.position = position
        self.color = color
        Board.map[self.position] = self
        if self.color is 'white':
            self.symbol = '♖'
        elif self.color is 'black':
            self.symbol = '♜'
        else: raise ValueError('Color not defined')
        
    def get_all():
        return Rook.all
    
    def move_validation(self, result_position):
        current_file, current_rank = self.position[0], int(self.position[1])
        target_file, target_rank = result_position[0], int(result_position[1])

        if current_file == target_file:
            # Moving vertically
            step = 1 if target_rank > current_rank else -1
            for rank in range(current_rank + step, target_rank, step):
                if Board.map[current_file + str(rank)] != ' ':
                    return False
            if Board.map[result_position] not in Piece.all:
                return True
            elif Board.map[result_position].color is not self.color:
                return True
            else: 
                return False
        elif current_rank == target_rank:
            # Moving horizontally
            step = 1 if ord(target_file) > ord(current_file) else -1
            for file in range(ord(current_file) + step, ord(target_file), step):
                if Board.map[chr(file) + str(current_rank)] != ' ':
                    return False
            if Board.map[result_position] not in Piece.all:
                return True
            elif Board.map[result_position].color is not self.color:
                return True
            else: 
                return False
        else:
            return False


class Knight(Piece):
    all = []
    
    def __init__(self, position, color):
        self.id = len(Knight.all) + 1
        Knight.all.append(self)
        Piece.all.append(self)
        self.position = position
        self.color = color
        Board.map[self.position] = self
        if self.color == 'white':
            self.symbol = '♘'
        elif self.color is 'black':
            self.symbol = '♞'
        else: raise ValueError('Color not defined')
        
    def get_all():
        return Knight.all
    
    def move_validation(self, result_position):
        current_file, current_rank = self.position[0], int(self.position[1])
        target_file, target_rank = result_position[0], int(result_position[1])

        file_diff = abs(ord(target_file) - ord(current_file))
        rank_diff = abs(target_rank - current_rank)

        # Knight moves in an "L" shape: (2,1) or (1,2) steps
        if (file_diff == 2 and rank_diff == 1) or (file_diff == 1 and rank_diff == 2):
            if Board.map[result_position] not in Piece.all:
                return True
            elif Board.map[result_position].color is not self.color:
                return True
            else: 
                return False
        else:
            return False


class Bishop(Piece):
    all = []
    
    def __init__(self, position, color):
        self.id = len(Bishop.all) + 1
        Bishop.all.append(self)
        Piece.all.append(self)
        self.position = position
        self.color = color
        Board.map[self.position] = self
        if self.color == 'white':
            self.symbol = '♗'
        elif self.color is 'black':
            self.symbol = '♝'
        else: raise ValueError('Color not defined')
        
    def get_all():
        return Bishop.all
    
    def move_validation(self, result_position):
        current_file, current_rank = self.position[0], int(self.position[1])
        target_file, target_rank = result_position[0], int(result_position[1])

        file_diff = abs(ord(target_file) - ord(current_file))
        rank_diff = abs(target_rank - current_rank)

        # Bishop moves diagonally (file_diff must equal rank_diff)
        if file_diff == rank_diff:
            # Determine direction of diagonal movement
            file_step = 1 if ord(target_file) > ord(current_file) else -1
            rank_step = 1 if target_rank > current_rank else -1

            # Check each square on the diagonal path (excluding start and end)
            for i in range(1, file_diff):
                check_file = chr(ord(current_file) + i * file_step)
                check_rank = current_rank + i * rank_step
                if Board.map[check_file + str(check_rank)] != ' ':
                    return False
            if Board.map[result_position] not in Piece.all:
                return True
            elif Board.map[result_position].color is not self.color:
                return True
            else: 
                return False
        else:
            return False


class Queen(Piece):
    all = []
    
    def __init__(self, position, color):
        self.id = len(Queen.all) + 1
        Queen.all.append(self)
        Piece.all.append(self)
        self.position = position
        self.color = color
        Board.map[self.position] = self
        if self.color == 'white':
            self.symbol = '♕'
        elif self.color is 'black':
            self.symbol = '♛'
        else: raise ValueError('Color not defined')
        
    def get_all():
        return Queen.all
    
    def move_validation(self, result_position):
        current_file, current_rank = self.position[0], int(self.position[1])
        target_file, target_rank = result_position[0], int(result_position[1])

        file_diff = abs(ord(target_file) - ord(current_file))
        rank_diff = abs(target_rank - current_rank)

        # Queen moves like a rook (horizontally or vertically) or a bishop (diagonally)
        if (file_diff == 0 and rank_diff > 0) or (file_diff > 0 and rank_diff == 0):
            # Moving vertically or horizontally (like a rook)
            if file_diff == 0:  # Moving vertically
                step = 1 if target_rank > current_rank else -1
                for rank in range(current_rank + step, target_rank, step):
                    if Board.map[current_file + str(rank)] != ' ':
                        return False
            else:  # Moving horizontally
                step = 1 if ord(target_file) > ord(current_file) else -1
                for file in range(ord(current_file) + step, ord(target_file), step):
                    if Board.map[chr(file) + str(current_rank)] != ' ':
                        return False
            if Board.map[result_position] not in Piece.all:
                return True
            elif Board.map[result_position].color is not self.color:
                return True
            else: 
                return False
        elif file_diff == rank_diff:
            # Moving diagonally (like a bishop)
            file_step = 1 if ord(target_file) > ord(current_file) else -1
            rank_step = 1 if target_rank > current_rank else -1
            for i in range(1, file_diff):
                check_file = chr(ord(current_file) + i * file_step)
                check_rank = current_rank + i * rank_step
                if Board.map[check_file + str(check_rank)] != ' ':
                    return False
            if Board.map[result_position] not in Piece.all:
                return True
            elif Board.map[result_position].color is not self.color:
                return True
            else: 
                return False
        else:
            return False


class King(Piece):
    all = []
    
    def __init__(self, position, color):
        self.id = len(King.all) + 1
        King.all.append(self)
        Piece.all.append(self)
        self.position = position
        self.color = color
        Board.map[self.position] = self
        if self.color == 'white':
            self.symbol = '♔'
        elif self.color is 'black':
            self.symbol = '♚'
        else: raise ValueError('Color not defined')
        
    def get_all():
        return King.all
    
    def move_validation(self, result_position):
        current_file, current_rank = self.position[0], int(self.position[1])
        target_file, target_rank = result_position[0], int(result_position[1])

        file_diff = abs(ord(target_file) - ord(current_file))
        rank_diff = abs(target_rank - current_rank)

        # King moves one square in any direction (horizontally, vertically, or diagonally)
        if file_diff <= 1 and rank_diff <= 1:
            if Board.map[result_position] not in Piece.all:
                return True
            elif Board.map[result_position].color is not self.color:
                return True
            else: 
                return False
        else:
            return False
        

game = Game()
game.start()
print(Piece.all)