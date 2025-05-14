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