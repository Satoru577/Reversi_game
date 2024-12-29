import pygame


BOARDSIZE = 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 150, 0)
GREEN_YELLOW = (173,255,47)

class board:
    def __init__(self):
        self.cells = []
        self.turn = 1

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

                row.append([color, rect, index, None])
                index += 1
            self.cells.append(row)
        self.cells[3][3][3] = WHITE
        self.cells[3][4][3] = BLACK
        self.cells[4][3][3] = BLACK
        self.cells[4][4][3] = WHITE


    def displaybord(self, screen):
        for vert_cells in self.cells:
            for color, rect, _, _ in vert_cells:
                pygame.draw.rect(screen, color, rect)

    def displaystone(self, screen):
        for cellList in self.cells:
            for cell in cellList:
                vert = cell[2] // 8
                hori = cell[2] % 8 #amari 
                if cell[3] is not None:
                        stone_location = (155 + hori *70, 55 + vert * 70)
                        pygame.draw.circle(screen, cell[3],(stone_location),30)


    def judgErea(self):
        for idx_v, cell_list in enumerate(self.cells):
            for idx_h, cell in enumerate(cell_list):
                #色のリセット
                if (idx_v + idx_h)% 2 == 0:
                    self.cells[idx_v][idx_h][0] = DARK_GREEN
                else:
                    self.cells[idx_v][idx_h][0] = GREEN

                if cell[3] is not None:
                    continue
                can_put = 0
                #white turn
                if self.turn == 0:
                    count = 1
                #brack
                else:
                    count = -1
                #左上確認
                can_put = judg_LU(self.cells, idx_v, idx_h, count, can_put)
                if can_put == 0:
                    can_put = judg_U(self.cells, idx_v, idx_h, count, can_put)
                if can_put == 0:
                    can_put = judg_RU(self.cells, idx_v, idx_h, count, can_put)
                if can_put == 0:
                    can_put = judg_L(self.cells, idx_v, idx_h, count, can_put)
                if can_put == 0:
                    can_put = judg_R(self.cells, idx_v, idx_h, count, can_put)
                if can_put == 0:
                    can_put = judg_LD(self.cells, idx_v, idx_h, count, can_put)
                if can_put == 0:
                    can_put = judg_D(self.cells, idx_v, idx_h, count, can_put)
                if can_put == 0:
                    can_put = judg_RD(self.cells, idx_v, idx_h, count, can_put)

                if can_put == 1:
                    self.cells[idx_v][idx_h][0] = GREEN_YELLOW


def judg_LU(cells, idx_v, idx_h, count, can_put):
    judg_flag = True
    while judg_flag:
        idx_L = idx_v - 1
        idx_U = idx_h - 1
        if 0 <= idx_L <= 7 and 0 <= idx_U <= 7:
            judg = count
            if cells[idx_L][idx_U][3] == WHITE:
                count -= 1
            elif cells[idx_L][idx_U][3] == BLACK:
                count += 1
            else:
                judg_flag = False
                continue
            if count == 0:
                judg_flag = False
                continue

            if abs(judg) < abs(count):
                can_put = judg_LU(cells, idx_L, idx_U, count, can_put)
            elif abs(judg) > abs(count):
                can_put = 1
            else:
                can_put = 0
            judg_flag = False
        else:
            judg_flag = False
    return can_put

def judg_U(cells, idx_v, idx_h, count, can_put):
    judg_flag = True
    while judg_flag:
        idx_L = idx_v - 1
        if 0 <= idx_L <= 7:
            judg = count
            if cells[idx_L][idx_h][3] == WHITE:
                count -= 1
            elif cells[idx_L][idx_h][3] == BLACK:
                count += 1
            else:
                judg_flag = False
                continue
            if count == 0:
                judg_flag = False
                continue

            if abs(judg) < abs(count):
                can_put = judg_U(cells, idx_L, idx_h, count, can_put)
            elif abs(judg) > abs(count):
                can_put = 1
            else:
                can_put = 0
            judg_flag = False
        else:
            judg_flag = False
    return can_put

def judg_RU(cells, idx_v, idx_h, count, can_put):
    judg_flag = True
    while judg_flag:
        idx_L = idx_v - 1
        idx_U = idx_h + 1
        if 0 <= idx_L <= 7 and 0 <= idx_U <= 7:
            judg = count
            if cells[idx_L][idx_U][3] == WHITE:
                count -= 1
            elif cells[idx_L][idx_U][3] == BLACK:
                count += 1
            else:
                judg_flag = False
                continue
            if count == 0:
                judg_flag = False
                continue

            if abs(judg) < abs(count):
                can_put = judg_RU(cells, idx_L, idx_U, count, can_put)
            elif abs(judg) > abs(count):
                can_put = 1
            else:
                can_put = 0
            judg_flag = False
        else:
            judg_flag = False
    return can_put

def judg_L(cells, idx_v, idx_h, count, can_put):
    judg_flag = True
    while judg_flag:
        idx_U = idx_h - 1
        if  0 <= idx_U <= 7:
            judg = count
            if cells[idx_v][idx_U][3] == WHITE:
                count -= 1
            elif cells[idx_v][idx_U][3] == BLACK:
                count += 1
            else:
                judg_flag = False
                continue
            if count == 0:
                judg_flag = False
                continue

            if abs(judg) < abs(count):
                can_put = judg_L(cells, idx_v, idx_U, count, can_put)
            elif abs(judg) > abs(count):
                can_put = 1
            else:
                can_put = 0
            judg_flag = False
        else:
            judg_flag = False
    return can_put

def judg_R(cells, idx_v, idx_h, count, can_put):
    judg_flag = True
    while judg_flag:
        idx_U = idx_h + 1
        if 0 <= idx_U <= 7:
            judg = count
            if cells[idx_v][idx_U][3] == WHITE:
                count -= 1
            elif cells[idx_v][idx_U][3] == BLACK:
                count += 1
            else:
                judg_flag = False
                continue
            if count == 0:
                judg_flag = False
                continue

            if abs(judg) < abs(count):
                can_put = judg_R(cells, idx_v, idx_U, count, can_put)
            elif abs(judg) > abs(count):
                can_put = 1
            else:
                can_put = 0
            judg_flag = False
        else:
            judg_flag = False
    return can_put

def judg_LD(cells, idx_v, idx_h, count, can_put):
    judg_flag = True
    while judg_flag:
        idx_L = idx_v + 1
        idx_U = idx_h - 1
        if 0 <= idx_L <= 7 and 0 <= idx_U <= 7:
            judg = count
            if cells[idx_L][idx_U][3] == WHITE:
                count -= 1
            elif cells[idx_L][idx_U][3] == BLACK:
                count += 1
            else:
                judg_flag = False
                continue
            if count == 0:
                judg_flag = False
                continue

            if abs(judg) < abs(count):
                can_put = judg_LD(cells, idx_L, idx_U, count, can_put)
            elif abs(judg) > abs(count):
                can_put = 1
            else:
                can_put = 0
            judg_flag = False
        else:
            judg_flag = False
    return can_put

def judg_D(cells, idx_v, idx_h, count, can_put):
    judg_flag = True
    while judg_flag:
        idx_L = idx_v + 1
        if 0 <= idx_L <= 7:
            judg = count
            if cells[idx_L][idx_h][3] == WHITE:
                count -= 1
            elif cells[idx_L][idx_h][3] == BLACK:
                count += 1
            else:
                judg_flag = False
                continue
            if count == 0:
                judg_flag = False
                continue

            if abs(judg) < abs(count):
                can_put = judg_D(cells, idx_L, idx_h, count, can_put)
            elif abs(judg) > abs(count):
                can_put =1
            else:
                can_put = 0
            judg_flag = False
        else:
            judg_flag = False
    return can_put

def judg_RD(cells, idx_v, idx_h, count, can_put):
    judg_flag = True
    while judg_flag:
        idx_L = idx_v + 1
        idx_U = idx_h + 1
        if 0 <= idx_L <= 7 and 0 <= idx_U <= 7:
            judg = count
            if cells[idx_L][idx_U][3] == WHITE:
                count -= 1
            elif cells[idx_L][idx_U][3] == BLACK:
                count += 1
            else:
                judg_flag = False
                continue
            if count == 0:
                judg_flag = False
                continue

            if abs(judg) < abs(count):
                can_put = judg_RD(cells, idx_L, idx_U, count, can_put)
            elif abs(judg) > abs(count):
                can_put =1
            else:
                can_put = 0
            judg_flag = False
        else:
            judg_flag = False
    return can_put

            #-1-1 -10 -11 0-1 01 1-1 10 11