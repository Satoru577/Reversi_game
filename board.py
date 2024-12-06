import pygame


BOARDSIZE = 8
WHITE = (255, 255, 255)
BRACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 150, 0)

class board:
    def __init__(self):
        self.cells = []
        self.cell_color = []

        index = 0
        for vert in range(BOARDSIZE):
            row = []
            for hori in range(BOARDSIZE):
                if (vert + hori)% 2 == 0:
                    color = DARK_GREEN
                    rect =(120 + hori * 70,20 + vert * 70,70,70)
                else:
                    color = GREEN
                    rect =(120 + hori * 70,20 + vert * 70,70,70)
                self.cell_color.append((color, rect, index))

                row.append([index, None])
                index += 1
            self.cells.append(row)
        self.cells[3][3] = [27,WHITE]
        self.cells[3][4] = [28,BRACK]
        self.cells[4][3] = [35,BRACK]
        self.cells[4][4] = [36,WHITE]

    def displaybord(self,screen):
        for color, rect, _ in self.cell_color:
            pygame.draw.rect(screen, color, rect)

    def displaystone(self, screen):
        vert = 0
        for cellList in self.cells:
            hori = 0
            for cell in cellList:
                if cell[1] is not None:
                    stone_location = (155 + hori *70, 55 + vert * 70)
                    pygame.draw.circle(screen, cell[1],(stone_location),30)
                hori += 1
            vert += 1 