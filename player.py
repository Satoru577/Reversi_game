BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)

class player:

    def __init__(self, num):
        if num == 1:
            self.color = BLACK
        if num == 2:
            self.color = WHITE

    def putStone(self, erea, game_board):
        for _, rect, index in game_board.cell_color:
            erea_left  = rect[0]
            erea_right = erea_left + rect[2]
            erea_top   = rect[1]
            erea_botom = erea_top + rect[3]

            if erea_left <=  erea[0] <= erea_right and erea_top <= erea[1] <=erea_botom:
                for cellList in game_board.cells:
                    for cell in cellList:
                        if cell[0] == index:
                            cell[1] = self.color


