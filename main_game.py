#imports
import numpy as np
import pygame
import sys
import graphic_interface
import utils
from move_checking import get_move
from move_checking import make_move

#chessboard
chessboard = [['-' for _ in range(utils.DIMENTION)] for _ in range(utils.DIMENTION)]

if __name__ == "__main__":
    #defining the initial chessboard
    chessboard[0] = ['wR', 'wN', 'wB', 'wK', 'wQ', 'wB', 'wN', 'wR']
    chessboard[7] = ['bR', 'bN', 'bB', 'bK', 'bQ', 'bB', 'bN', 'bR']
    chessboard[1] = ['wP' for p in range(0, 8)]
    chessboard[6] = ['bP' for p in range(0, 8)]
    
    #defining the previous informations
    player = utils.WHITE #0 is white, 1 is black
    running = True
    pygame.init()
    screen = pygame.display.set_mode(\
            (graphic_interface.SIDE + graphic_interface.SIDE/2 + 2*graphic_interface.OFFSET, 
             graphic_interface.SIDE + 2*graphic_interface.OFFSET))
    pygame.display.set_caption("CHESS")
    
    #the variables for saying if it still possible to castle
    wCR, wCL, bCR, bCL = True, True, True, True

    
    while running: #main loop for the game
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        graphic_interface.show_board(chessboard, screen, player) 
        pygame.display.flip()
        
        move = get_move(chessboard, player, wCR, wCL, bCR, bCL) #this gets a valid move

        if(move == "quit"):
            break

        wCR, wCL, bCR, bCL = make_move(chessboard, move, wCR, wCL, bCR, bCL)

        if player == utils.BLACK:
            player = utils.WHITE  
        else:  
            player = utils.BLACK
            
    pygame.quit()
    sys.exit()