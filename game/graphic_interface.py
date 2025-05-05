import pygame
import utils

COLORS = [(240, 217, 181), (181, 136, 99)]
FONTSIZE = 48
RED = (200, 50, 20)
OFFSET = 10
PADDING = 20
SIDE = 640
SIDE_RECT = int(SIDE/8)

def show_board(chessboard, screen, player):

    pygame.draw.rect(screen, RED, (SIDE + 2*OFFSET + PADDING, PADDING + OFFSET, 2*SIDE_RECT, SIDE_RECT))
    font = pygame.font.SysFont(None, FONTSIZE)        
    text_surface = font.render("Desistir", True, (255, 255, 255)) 
    screen.blit(text_surface, (SIDE + 2*OFFSET + 2*PADDING, 2*PADDING + OFFSET))
    text_surface = font.render(f"vez do jogador {player}", True, (255, 255, 255)) 
    screen.blit(text_surface, (SIDE + 2*OFFSET + 2*PADDING, 6*PADDING + OFFSET))
    

    for row in range(0, 8):
        for col in range(0, 8):
            color = COLORS[(row+col)%2]
            pygame.draw.rect(screen, color, ((7-col)*SIDE_RECT + OFFSET, (7-row)*SIDE_RECT + OFFSET, SIDE_RECT, SIDE_RECT))
            if(chessboard[row][col] != '-'):
                piece = chessboard[row][col]
                piecedraw = pygame.transform.scale(
                    pygame.image.load(f"pieces/{piece}.svg"),
                    (SIDE_RECT, SIDE_RECT)
                )
                screen.blit(piecedraw, ((7-col)*SIDE_RECT + OFFSET, (7-row)*SIDE_RECT + OFFSET))
                pygame.display.update()


def show_winning_message(player, screen):
    font = pygame.font.SysFont(None, FONTSIZE) 
    message = None
    if player == utils.WHITE:
        message = "O jogador de brancas ganhou!"
    else:
        message = "O jogador de negras ganhou!"
    text_surface = font.render(message, True, (255, 255, 255)) 
    screen.blit(text_surface, (SIDE/2, SIDE/2))

