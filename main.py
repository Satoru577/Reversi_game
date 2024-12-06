import pygame
import sys
import time
import os 
from board import board
from player import player

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
GRAY =(220, 220, 220)

#画面サイズ
SCEEN_HEIGHT = 600
SCREEN_HEIGHT = 800

os.environ['SDL_VIDEODRIVER'] = 'x11'
pygame.init()

game_board = board()
player1 = player(1)
player2 = player(2)
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCEEN_HEIGHT))
pygame.display.set_caption("reversi")

click = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # 左クリック 
                player1.putStone(event.pos, game_board)
    screen.fill(GRAY)
    game_board.displaybord(screen)
    game_board.displaystone(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()

