import pygame
import sys
import time

pygame.init()

#画面サイズ
screen_hight = 600
screen_wight = 800
screen = pygame.display.set_mode((screen_wight, screen_hight))
pygame.display.set_caption("reversi")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()