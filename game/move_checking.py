import pygame
import utils
import copy
import graphic_interface

def verify_knight_check(chessboard, move):
    king_position = utils.find_position(chessboard, move[0]+'K')
    
    #knight check
    for kmove in utils.KNIGHT_MOVES:
        knight_position = (king_position[0] + kmove[0], king_position[1] + kmove[1])
        if(knight_position[0]>= 0 and 
           knight_position[1] >= 0):
            if utils.chess_position(chessboard, king_position) == utils.rev(move[0]) + 'N':
                #this means that there is a knight attacking the king
                return True
    return False

def verify_bishop_check(chessboard, move):
    king_position = utils.find_position(chessboard, move[0]+'K')
    #check the 4 diagonals
    #first diagonal
    for i in range(1, 8):
        bishop_position = (king_position[0] + i, king_position[1] + i)
        if(bishop_position[0] >= 0 and bishop_position[0] < 8 and
           bishop_position[1] >= 0 and bishop_position[0] < 8 ):
            if utils.chess_position(chessboard,bishop_position) == utils.rev(move[0]) + 'B':
                return True
            elif utils.chess_position(chessboard,bishop_position) != '-':
                #there is a piece blocking any possible bishop
                break
    for i in range(1, 8):
        bishop_position = (king_position[0] - i, king_position[1] + i)
        if(bishop_position[0] >= 0 and bishop_position[0] < 8 and
           bishop_position[1] >= 0 and bishop_position[0] < 8 ):
            if utils.chess_position(chessboard,bishop_position) == utils.rev(move[0]) + 'B':
                return True
            elif utils.chess_position(chessboard,bishop_position) != '-':
                #there is a piece blocking any possible bishop
                break
    for i in range(1, 8):
        bishop_position = (king_position[0] + i, king_position[1] - i)
        if(bishop_position[0] >= 0 and bishop_position[0] < 8 and
           bishop_position[1] >= 0 and bishop_position[0] < 8 ):
            if utils.chess_position(chessboard,bishop_position) == utils.rev(move[0]) + 'B':
                return True
            elif utils.chess_position(chessboard,bishop_position) != '-':
                #there is a piece blocking any possible bishop
                break
    for i in range(1, 8):
        bishop_position = (king_position[0] - i, king_position[1] - i)
        if(bishop_position[0] >= 0 and bishop_position[0] < 8 and
           bishop_position[1] >= 0 and bishop_position[0] < 8 ):
            if utils.chess_position(chessboard,bishop_position) == utils.rev(move[0]) + 'B':
                return True
            elif utils.chess_position(chessboard,bishop_position) != '-':
                #there is a piece blocking any possible bishop
                break
    
    #default
    return False

def verify_rook_check(chessboard, move):
    king_position = utils.find_position(chessboard, move[0]+'K')

    for i in range(1, 8):
        rook_position = (king_position[0] + i, king_position[1])
        if(rook_position[0] < 0 or rook_position[1] < 0 or rook_position[0] > 7 or rook_position[1] > 7):
            break
        if utils.chess_position(chessboard,rook_position) == utils.rev(move[0]) + 'R':
            return True
        if utils.chess_position(chessboard,rook_position) != '-':
            break
    for i in range(1, 8):
        rook_position = (king_position[0] - i, king_position[1])
        if(rook_position[0] < 0 or rook_position[1] < 0 or rook_position[0] > 7 or rook_position[1] > 7):
            break
        if utils.chess_position(chessboard,rook_position) == utils.rev(move[0]) + 'R':
            return True
        if utils.chess_position(chessboard,rook_position) != '-':
            break
    for i in range(1, 8):
        rook_position = (king_position[0], king_position[1] + i)
        if(rook_position[0] < 0 or rook_position[1] < 0 or rook_position[0] > 7 or rook_position[1] > 7):
            break
        if utils.chess_position(chessboard,rook_position) == utils.rev(move[0]) + 'R':
            return True
        if utils.chess_position(chessboard,rook_position) != '-':
            break
    for i in range(1, 8):
        rook_position = (king_position[0], king_position[1] - i)
        if(rook_position[0] < 0 or rook_position[1] < 0 or rook_position[0] > 7 or rook_position[1] > 7):
            break
        if utils.chess_position(chessboard,rook_position) == utils.rev(move[0]) + 'R':
            return True
        if utils.chess_position(chessboard,rook_position) != '-':
            break

    #default
        return False

def verify_pawn_check(chessboard, move):
    player = move[0]  

    king_position = utils.find_position(chessboard, move[0]+'K')
    if(player == utils.WHITE): #white has made the move, we want to check for checks of black pawns
        if(king_position[1] <= 6):# n ta no canto do tabuleiro
            if(king_position[0] >= 1):
                if(utils.chess_position(chessboard,(king_position[0] - 1, king_position[1] + 1)) == 'bP'):
                    return True
            if(king_position[1] <= 6):
                if(utils.chess_position(chessboard,(king_position[0] + 1, king_position[1] + 1)) == 'bP'):
                    return True
    
    elif(player == utils.BLACK):
         if(king_position[1] >= 0):# n ta no canto do tabuleiro
            if(king_position[0] >= 1):
                if(utils.chess_position(chessboard,(king_position[0] - 1, king_position[1] - 1)) == 'wP'):
                    return True
            if(king_position[1] <= 6):
                if(utils.chess_position(chessboard,(king_position[0] + 1, king_position[1] - 1)) == 'wP'):
                    return True
                
    return False        
    
def verify_queen_check(chessboard, move):
    king_position = utils.find_position(chessboard, move[0]+'K')
    #check the 4 diagonals
    #first diagonal
    for i in range(1, 8):
        bishop_position = (king_position[0] + i, king_position[1]+i)
        if(bishop_position[0] >= 0 and bishop_position[0] < 8 and
           bishop_position[1] >= 0 and bishop_position[0] < 8 ):
            if utils.chess_position(chessboard,bishop_position) == utils.rev(move[0]) + 'Q':
                return True
            elif utils.chess_position(chessboard,bishop_position) != '-':
                #there is a piece blocking any possible bishop
                break
    for i in range(1, 8):
        bishop_position = (king_position[0] - i, king_position[1]+i)
        if(bishop_position[0] >= 0 and bishop_position[0] < 8 and
           bishop_position[1] >= 0 and bishop_position[0] < 8 ):
            if utils.chess_position(chessboard,bishop_position) == utils.rev(move[0]) + 'Q':
                return True
            elif utils.chess_position(chessboard,bishop_position) != '-':
                #there is a piece blocking any possible bishop
                break
    for i in range(1, 8):
        bishop_position = (king_position[0] + i, king_position[1]-i)
        if(bishop_position[0] >= 0 and bishop_position[0] < 8 and
           bishop_position[1] >= 0 and bishop_position[0] < 8 ):
            if utils.chess_position(chessboard,bishop_position) == utils.rev(move[0]) + 'Q':
                return True
            elif utils.chess_position(chessboard,bishop_position) != '-':
                #there is a piece blocking any possible bishop
                break
    for i in range(1, 8):
        bishop_position = (king_position[0] - i, king_position[1]-i)
        if(bishop_position[0] >= 0 and bishop_position[0] < 8 and
           bishop_position[1] >= 0 and bishop_position[0] < 8 ):
            if utils.chess_position(chessboard,bishop_position) == utils.rev(move[0]) + 'Q':
                return True
            elif utils.chess_position(chessboard,bishop_position) != '-':
                #there is a piece blocking any possible bishop
                break

    for i in range(1, 8):
        rook_position = (king_position[0] + i, king_position[1])
        if(rook_position[0] < 0 or rook_position[1] < 0 or rook_position[0] > 7 or rook_position[1] > 7):
            break
        if utils.chess_position(chessboard,rook_position) == utils.rev(move[0]) + 'Q':
            return True
        if utils.chess_position(chessboard,rook_position) != '-':
            break
    for i in range(1, 8):
        rook_position = (king_position[0] - i, king_position[1])
        if(rook_position[0] < 0 or rook_position[1] < 0 or rook_position[0] > 7 or rook_position[1] > 7):
            break
        if utils.chess_position(chessboard,rook_position) == utils.rev(move[0]) + 'Q':
            return True
        if utils.chess_position(chessboard,rook_position) != '-':
            break
    for i in range(1, 8):
        rook_position = (king_position[0], king_position[1] + i)
        if(rook_position[0] < 0 or rook_position[1] < 0 or rook_position[0] > 7 or rook_position[1] > 7):
            break
        if utils.chess_position(chessboard,rook_position) == utils.rev(move[0]) + 'Q':
            return True
        if utils.chess_position(chessboard,rook_position) != '-':
            break
    for i in range(1, 8):
        rook_position = (king_position[0], king_position[1] - i)
        if(rook_position[0] < 0 or rook_position[1] < 0 or rook_position[0] > 7 or rook_position[1] > 7):
            break
        if utils.chess_position(chessboard,rook_position) == utils.rev(move[0]) + 'Q':
            return True
        if utils.chess_position(chessboard,rook_position) != '-':
            break
    
    #default
    return False

def verify_king_check(chessboard, move):
    king_position = utils.find_position(chessboard, move[0] + 'K')
    for i in utils.KING_MOVES:
        if utils.chess_position(chessboard,(king_position[0] + i[0], king_position[1]+i[1])) == utils.rev(move[0]) + 'K':
            return True
    return False

def verify_ischeck(chessboard, move):
    #this function presumes that the chessboard will have the move and calculates with it
    #return true if the king will be in check after the move, which means the move is illegal
    
    #knight check
    if verify_knight_check(chessboard, move):
        return True
    
    #bishop check
    if verify_bishop_check(chessboard, move):
        return True

    #rook check
    if verify_rook_check(chessboard, move):
        return True
    
    #pawn check
    if verify_pawn_check(chessboard, move):
        return True
    
    #queen check
    if verify_queen_check(chessboard, move):
        return True
    
    if verify_king_check(chessboard, move):
        return True

    #default
    return False #movimento valido


def check_move_pawn(chessboard, move):
    ini = move[0]
    fim = move[1]
    moveRel = (fim[1]-ini[1], fim[0]-ini[0])
    player = utils.chess_position(chessboard, ini)[0]
    if player == utils.WHITE:
        if ini[0] == 1:
            if moveRel == (0, 2) and utils.chess_position(chessboard, fim) == '-':
                return True
        if moveRel == (0, 1) and utils.chess_position(chessboard, fim) == '-':
            return True
        if (moveRel == (1, 1) or moveRel == (-1, 1)) and \
            utils.chess_position(chessboard, fim)[0] == utils.rev(player):
            return True; 
    elif player == utils.BLACK:
        if ini[0] == 6:
            if moveRel == (0, -2) and utils.chess_position(chessboard, fim) == '-':
                return True
        if moveRel == (0, -1) and utils.chess_position(chessboard, fim) == '-':
            return True
        if (moveRel == (1, -1) or moveRel == (-1, -1)) and \
            utils.chess_position(chessboard, fim)[0] == utils.rev(player):
            return True;
    return False

def check_move_bishop(chessboard, move):
    ini = move[0]
    fim = move[1]
    moveRel = (fim[0]-ini[0], fim[1]-ini[1])
    if moveRel not in utils.BISHOP_MOVES:
        return False
    direction = (int(moveRel[0]/abs(moveRel[0])), int(moveRel[1]/abs(moveRel[1])))
    for i in range(1, int(abs(moveRel[0]))):
        if utils.chess_position(chessboard, (ini[0] + i*direction[0], ini[1]+i*direction[1])) != '-':
            return False
        
    return True
    
def check_move_rook(chessboard, move):
    ini = move[0]
    fim = move[1]
    moveRel = (fim[0]-ini[0], fim[1]-ini[1])
    if moveRel not in utils.ROOK_MOVES:
        return False
    direction = (0 if moveRel[0] == 0 else int(moveRel[0]/abs(moveRel[0])),
                 0 if moveRel[1] == 0 else int(moveRel[1]/abs(moveRel[1])))
    for i in range(1, max(int(abs(moveRel[0])), int(abs(moveRel[1])))):
        if utils.chess_position(chessboard, (ini[0] + i*direction[0], ini[1]+i*direction[1])) != '-':
            return False
        
    return True

def check_move_queen(chessboard, move):
    ini = move[0]
    fim = move[1]
    moveRel = (fim[0]-ini[0], fim[1]-ini[1])
    if moveRel not in utils.QUEEN_MOVES:
        return False
    direction = (0 if moveRel[0] == 0 else int(moveRel[0]/abs(moveRel[0])),
                 0 if moveRel[1] == 0 else int(moveRel[1]/abs(moveRel[1])))
    for i in range(1, max(int(abs(moveRel[0])), int(abs(moveRel[1])))):
        if utils.chess_position(chessboard, (ini[0] + i*direction[0], ini[1]+i*direction[1])) != '-':
            return False
        
    return True

def check_move_king(chessboard, move, wCR, wCL, bCR, bCL):
    ini = move[0]
    fim = move[1]
    player = utils.chess_position(chessboard, ini)[0]
    moveRel = (fim[0]-ini[0], fim[1]-ini[1])
    if moveRel not in utils.KING_MOVES + utils.KING_CASTLE_MOVES:
        return False
        
    if moveRel == (0, 2):
        if player == utils.WHITE:
            if not wCL:
                return False                   
        if player == utils.BLACK:
            if not bCL:
                return False
        if utils.chess_position(chessboard, (ini[0], ini[1]+1)) != '-' or \
               utils.chess_position(chessboard, (ini[0], ini[1]+2)) != '-' or \
               utils.chess_position(chessboard, (ini[0], ini[1]+3)) != '-':
                return False
        chessboard_aux = copy.deepcopy(chessboard) 
        chessboard_aux[ini[0]][ini[1]+1] = chessboard_aux[ini[0]][ini[1]]
        chessboard_aux[ini[0]][ini[1]] = '-'
        player = utils.chess_position(chessboard, ini)
        if utils.verify_ischeck(chessboard_aux, player):
            return False
            
    if moveRel == (0, -2):
        if player == utils.WHITE:
            if not wCR:
                return False
        if player == utils.BLACK:
            if not bCR:
                return False
        if utils.chess_position(chessboard, (ini[0], ini[1]-1)) != '-' or \
           utils.chess_position(chessboard, (ini[0], ini[1]-2)) != '-':
            return False
        chessboard_aux = copy.deepcopy(chessboard) 
        chessboard_aux[ini[0]][ini[1]-1] = chessboard_aux[ini[0]][ini[1]]
        chessboard_aux[ini[0]][ini[1]] = '-'
        player = utils.chess_position(chessboard, ini)
        if utils.verify_ischeck(chessboard_aux, player):
            return False
        

    return True

def check_move(chessboard, move, wCR, wCL, bCR, bCL):
    ini = move[0]
    fim = move[1]
    piece = utils.chess_position(chessboard, ini)[1]

    #this checks if this piece can do this move
    moveRel = (fim[0]-ini[0], fim[1]-ini[1])
    possible = True
    if piece == 'P':
        if not check_move_pawn(chessboard, move):
            possible = False
    elif piece == 'B':
        if not check_move_bishop(chessboard, move):
            possible = False
    elif piece == 'R':
        if not check_move_rook(chessboard, move):
            possible = False        
    elif piece == 'N':
        if moveRel not in utils.KNIGHT_MOVES:
            possible = False
    elif piece == 'K':
        if not check_move_king(chessboard, move, wCR, wCL, bCR, bCL):
            possible = False
    elif piece == 'Q':
        if not check_move_queen(chessboard, move):
            possible = False
    
    if not possible:
        return False
    
    chessboard_aux = copy.deepcopy(chessboard) 
    chessboard_aux[fim[0]][fim[1]] = chessboard_aux[ini[0]][ini[1]]
    chessboard_aux[ini[0]][ini[1]] = '-'
    #isso aqui de player n tem nada, a funcao recebe uma peca e a partir dela identifica o player, e nos parametros da funcao ainda ta move
    player = utils.chess_position(chessboard, ini)
    if verify_ischeck(chessboard_aux, player):
        return False
            
    return True

def get_move(chessboard, player, wCR, wCL, bCR, bCL):
    movePart = 0
    posIni, posFim = None, None
    clock = pygame.time.Clock()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                posAbs = event.pos
                posRel = ((7-posAbs[1]//graphic_interface.SIDE_RECT), (7-posAbs[0]//graphic_interface.SIDE_RECT))

                if(movePart == 0):
                    if(utils.chess_position(chessboard, posRel) == '-'): continue
                    if(utils.chess_position(chessboard, posRel)[0] == utils.rev(player)): continue                    
                    posIni = posRel
                    movePart += 1

                elif(movePart == 1):
                    if(utils.chess_position(chessboard, posRel)[0] == player):
                        posIni = posRel #deixa clicar de novo em outra branca
                        continue
                    if(check_move(chessboard, (posIni, posRel), wCR, wCL, bCR, bCL)):
                        posFim = posRel
                        return (posIni, posFim)                    
                    else: continue
        clock.tick(60) 

def make_move(chessboard, move, wCR, wCL, bCR, bCL):
    ini = move[0]
    fim = move[1]
    moveRel = (fim[0]-ini[0], fim[1]-ini[1])

    #if we are clasting, we must move the rook
    if utils.chess_position(chessboard, ini) != '-':
        if utils.chess_position(chessboard, ini)[1] == 'K' and \
        moveRel in utils.KING_CASTLE_MOVES:
            if moveRel == (0, 2):
                chessboard[ini[0]][4] = chessboard[ini[0]][7]
                chessboard[ini[0]][7] = '-'
            elif moveRel == (0, -2):
                chessboard[ini[0]][2] = chessboard[ini[0]][0]
                chessboard[ini[0]][0] = '-'
    
    chessboard[fim[0]][fim[1]] = chessboard[ini[0]][ini[1]]
    chessboard[ini[0]][ini[1]] = '-'

    #here we need to promote pawns
    if fim[0] == 7 and utils.chess_position(chessboard, fim) == 'wP':
        chessboard[fim[0]][fim[1]] = "wQ"
    if fim[0] == 0 and utils.chess_position(chessboard, fim) == 'bP':
        chessboard[fim[0]][fim[1]] = "bQ"

    #here we need to make the conditions for castling
    #(0, 0 is the botton right)
    if ini == (0, 0):
        wCR = False
    elif ini == (0, 7):
        wCL = False
    elif ini == (7, 7):
        bCL = False
    elif ini == (7, 0):
        bCR = False
    
    return wCR, wCL, bCR, bCL

