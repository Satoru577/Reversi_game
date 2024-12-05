import pygame

WHITE = 0
BRACK = 1
BOARDSIZE = 8

GREEN = (0, 200, 0)
DARK_GREEN = (0, 150, 0)

class board:
    def __init__(self):
        self.cells = [[None for _ in range(BOARDSIZE)] for _ in range(BOARDSIZE)]
        self.cell_color = []

        for vert in range(BOARDSIZE):
            for hori in range(BOARDSIZE):
                if (vert + hori)% 2 == 0:
                    color = GREEN
                else:
                    color = DARK_GREEN
                rect =(120 + hori * 70,10 + vert * 70,70,70)
                self.cell_color.append((color, rect))
        self.cells[3][3] = WHITE
        self.cells[3][4] = BRACK
        self.cells[4][3] = BRACK
        self.cells[4][4] = WHITE

    def displaybord(self,screen):
        for color, rect in self.cell_color:
            pygame.draw.rect(screen, color, rect)


