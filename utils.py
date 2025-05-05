import numpy as np

DIMENTION = 8
WHITE = 'w'
BLACK = 'b'



KNIGHT_MOVES = [(-1, 2), (1, 2), (-2, 1), (2, 1),
                (-2, -1), (2, -1), (-1, -2), (1, -2)]

BISHOP_MOVES = [(i,i) for i in range(1, 8)] \
            +  [(-i,i) for i in range(1, 8)]\
            +  [(i,-i) for i in range(1, 8)]\
            +  [(-i,-i) for i in range(1, 8)]

KING_MOVES = [(1, 1),    (1, 0),  (0, 1),
              (-1, -1,), (-1, 0), (0, -1),
              (-1, 1),   (1, -1)]

KING_CASTLE_MOVES = [(0, 2), (0, -2)]

ROOK_MOVES = [(0, i) for i in range(-8, 8)]\
           + [(i, 0) for i in range(-8, 8)]

QUEEN_MOVES = [(0, i) for i in range(-8, 8)]\
           +  [(i, 0) for i in range(-8, 8)]\
           +  [(i,i) for i in range(1, 8)]  \
           +  [(-i,i) for i in range(1, 8)] \
           +  [(i,-i) for i in range(1, 8)] \
           +  [(-i,-i) for i in range(1, 8)]

PAWN_MOVES = [(0, 1)]

def chess_position(chessboard, a):
    if(0<=a[0] and a[0]<8 and 0<=a[1] and a[1]<8):
        return chessboard[a[0]][a[1]]
    return '-'

def position_to_pair(pos):
    #converts a position b3 into a position (1, 2)
    x = pos[0]
    y = pos[1]
    return np.array(int(x-'a'), int(y)-1)

def find_position(chessboard, piece):
    for i in range(0, 8):
        for j in range(0, 8):
            if chessboard[i][j] == piece:
                return (i, j)
    return (-1, -1)

def rev(player):
    if player == 'w':
        return 'b'
    return 'w'

