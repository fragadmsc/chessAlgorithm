#imports
import numpy as np
import math

#constants
ROWS = 8
COLUMNS = 8
WHITE = 0
BLACK = 1

KNIGHT_MOVES = [(-1, 2), (1, 2), (-2, 1), (2, 1),
                (-2, -1), (2, -1), (-1, -2), (1, -2)]

BISHOP_MOVES = [(i,i) for i in range(1, 8)]\
            +  [(-i,i) for i in range(1, 8)]\
            +  [(i,-i) for i in range(1, 8)]\
            +  [(-i,-i) for i in range(1, 8)]

chessboard = [['-' for _ in range(COLUMNS)] for _ in range(ROWS)]

def chess_position(a):
    return chessboard[a[0]][a[1]]

def askmove(player):
    move
    if player == WHITE:
        move = input("Digite o movimento do jogador de brancas")
    elif player == BLACK:
        move = input("Digite o movimento do jogador de pretas")
    return move

def position_to_pair(pos):
    #converts a position b3 into a position (1, 2)
    x = pos[0]
    y = pos[1]
    return (int(x-'a'), int(y)-1)

def verify_piece_exists(move):
    playerc = move[0]
    piece = move[1]
    
    origin = position_to_pair(move[2:3])
    destin = position_to_pair(move[4:5])
    if chessboard[origin[0]][origin[1]] == playerc + piece:
        return True
    else:
        return False

def find_position(piece):
    for i in range(0, 8):
        for j in range(0, 8):
            if chessboard[i][j] == piece:
                return (i, j)
    return (-1, -1)

def rev(player):
    if player == 'w':
        return 'b'
    return 'w'

def verify_check(move):
    #return true if the king will be in check after the move, which means the move is illegal
    king_position = find_position(move[0]+'K')
    
    #knight check
    for kmove in KNIGHT_MOVES:
        knight_position = king_position + kmove
        if(knight_position[0] >= 0 and 
           knight_position[1] >= 0):
            if chess_position(king_position) == rev(move[0]) + 'N':
                #this means that there is a knight attacking the king
                return True
    
    #bishop check
    #check the 4 diagonals
    #first diagonal
    for i in range(0, 8):
        bishop_position = king_position + (i, i)
        if(bishop_position[0] >= 0 and
           bishop_position[1] >= 0):
            if chess_position(bishop_position) == rev(move[0]) + 'B':
                return False
            elif chess_position(bishop_position) != '-':
                #there is a piece blocking any possible bishop
                break
    for i in range(0, 8):
        bishop_position = king_position + (-i, i)
        if(bishop_position[0] >= 0 and
           bishop_position[1] >= 0):
            if chess_position(bishop_position) == rev(move[0]) + 'B':
                return False
            elif chess_position(bishop_position) != '-':
                #there is a piece blocking any possible bishop
                break
    for i in range(0, 8):
        bishop_position = king_position + (i, -i)
        if(bishop_position[0] >= 0 and
           bishop_position[1] >= 0):
            if chess_position(bishop_position) == rev(move[0]) + 'B':
                return False
            elif chess_position(bishop_position) != '-':
                #there is a piece blocking any possible bishop
                break
    for i in range(0, 8):
        bishop_position = king_position + (-i, -i)
        if(bishop_position[0] >= 0 and
           bishop_position[1] >= 0):
            if chess_position(bishop_position) == rev(move[0]) + 'B':
                return False
            elif chess_position(bishop_position) != '-':
                #there is a piece blocking any possible bishop
                break
            


    


def verify_move(move):
    verify_piece_exists(move)
    verify_check(move)


if __name__ == "__main__":
    #defining the initial chessboard
    chessboard[0] = ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
    chessboard[7] = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']
    chessboard[1] = ['wP' for p in range(0, 8)]
    chessboard[6] = ['bP' for p in range(0, 8)]
    
    player = 0 #0 is white, 1 is black
    while True: #main loop for the game
        move = askmove(player)
        if player == WHITE:
            move = 'w' + move
        elif player == BLACK:
            move = 'b' + move
        
        if verify_move(move):
            make_move(move)
            print("Movimento realizado")
        else:
            print("Movimento ilegal, faca outro")
            continue

        player = (player+1)%2
