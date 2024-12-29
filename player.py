BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
GREEN_YELLOW = (173,255,47)

class players:

    def __init__(self):
            self.color = BLACK
            self.num = 1

    def putStone(self, erea, game_board):
        for idx_v, cell_list in enumerate(game_board.cells):
            for idx_h, cell in enumerate(cell_list):
                bord_color = cell[0]
                rect = cell[1]
                index = cell[2]
                color = cell[3]
                if color is None:
                    erea_left  = rect[0]
                    erea_right = erea_left + rect[2]
                    erea_top   = rect[1]
                    erea_botom = erea_top + rect[3]

                    if erea_left <=  erea[0] <= erea_right and erea_top <= erea[1] <=erea_botom:
                        if game_board.cells[idx_v][idx_h][0] == GREEN_YELLOW:
                            new_stone = self.color 
                            game_board.cells[idx_v][idx_h] = [bord_color, rect, index , new_stone]

                            if self.num == 1:
                                chang_stone(game_board, self.color, idx_v ,idx_h)
                                self.color = WHITE
                                self.num = 2
                                game_board.turn = 0
                            else:
                                chang_stone(game_board, self.color, idx_v ,idx_h)
                                self.color = BLACK
                                self.num = 1
                                game_board.turn = 1

def chang_stone(game_board, color, idx_v ,idx_h):
                chang_flag = 0
                #white turn
                if game_board.turn == 0:
                    count = 1
                #brack
                else:
                    count = -1
                #左上確認
                chang_LU(game_board.cells, idx_v, idx_h, count, chang_flag, color)
                chang_U(game_board.cells, idx_v, idx_h, count, chang_flag, color)
                chang_RU(game_board.cells, idx_v, idx_h, count, chang_flag, color)
                chang_L(game_board.cells, idx_v, idx_h, count, chang_flag, color)
                chang_R(game_board.cells, idx_v, idx_h, count, chang_flag, color)
                chang_LD(game_board.cells, idx_v, idx_h, count, chang_flag, color)
                chang_D(game_board.cells, idx_v, idx_h, count, chang_flag, color)
                chang_RD(game_board.cells, idx_v, idx_h, count, chang_flag, color)




def chang_LU(cells, idx_v, idx_h, count, can_put, color):
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
                can_put = chang_LU(cells, idx_L, idx_U, count, can_put, color)
            elif abs(judg) > abs(count):
                can_put = 1
            else:
                can_put = 0
            judg_flag = False
        else:
            judg_flag = False
    if can_put == 1:
        cells[idx_L][idx_U][3] = color
    return can_put

def chang_U(cells, idx_v, idx_h, count, can_put, color):
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
                can_put = chang_U(cells, idx_L, idx_h, count, can_put, color)
            elif abs(judg) > abs(count):
                can_put = 1
            else:
                can_put = 0
            judg_flag = False
        else:
            judg_flag = False
    if can_put == 1:
        cells[idx_L][idx_h][3] = color
    return can_put

def chang_RU(cells, idx_v, idx_h, count, can_put, color):
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
                can_put = chang_RU(cells, idx_L, idx_U, count, can_put, color)
            elif abs(judg) > abs(count):
                can_put = 1
            else:
                can_put = 0
            judg_flag = False
        else:
            judg_flag = False
    if can_put == 1:
        cells[idx_L][idx_U][3] = color
    return can_put

def chang_L(cells, idx_v, idx_h, count, can_put, color):
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
                can_put = chang_L(cells, idx_v, idx_U, count, can_put, color)
            elif abs(judg) > abs(count):
                can_put = 1
            else:
                can_put = 0
            judg_flag = False
        else:
            judg_flag = False
    if can_put == 1:
        cells[idx_v][idx_U][3] = color
    return can_put

def chang_R(cells, idx_v, idx_h, count, can_put, color):
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
                can_put = chang_R(cells, idx_v, idx_U, count, can_put, color)
            elif abs(judg) > abs(count):
                can_put = 1
            else:
                can_put = 0
            judg_flag = False
        else:
            judg_flag = False
    if can_put == 1:
        cells[idx_v][idx_U][3] = color
    return can_put

def chang_LD(cells, idx_v, idx_h, count, can_put, color):
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
                can_put = chang_LD(cells, idx_L, idx_U, count, can_put, color)
            elif abs(judg) > abs(count):
                can_put = 1
            else:
                can_put = 0
            judg_flag = False
        else:
            judg_flag = False
    if can_put == 1:
        cells[idx_L][idx_U][3] = color
    return can_put

def chang_D(cells, idx_v, idx_h, count, can_put, color):
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
                can_put = chang_D(cells, idx_L, idx_h, count, can_put, color)
            elif abs(judg) > abs(count):
                can_put =1
            else:
                can_put = 0
            judg_flag = False
        else:
            judg_flag = False
    if can_put == 1:
        cells[idx_L][idx_h][3] = color
    return can_put

def chang_RD(cells, idx_v, idx_h, count, can_put, color):
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
                can_put = chang_RD(cells, idx_L, idx_U, count, can_put, color)
            elif abs(judg) > abs(count):
                can_put =1
            else:
                can_put = 0
            judg_flag = False
        else:
            judg_flag = False
    if can_put == 1:
        cells[idx_L][idx_U][3] = color
    return can_put
