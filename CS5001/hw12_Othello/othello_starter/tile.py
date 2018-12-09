from grid import Grid
from computer import Computer


class Tile:
    def __init__(self):
        """Initialize the board as a nested array, specifying four tiles
        in the middle"""
        self.grid = Grid(600, 600, 100)
        self.WIDTH = self.grid.SPACING * 0.85
        self.HEIGHT = self.grid.SPACING * 0.85
        self.computer = Computer(self)
        self.row = self.grid.HEIGHT // self.grid.SPACING
        self.col = self.grid.WIDTH // self.grid.SPACING
        self.full_tile = self.row * self.col
        self.full = False
        self.tile = [[0] * self.col for i in range(self.row)]
        # Initialize starting four tiles.
        # 1 stands for black tile
        # 2 stands for white tile
        self.tile[self.row // 2 - 1][self.col // 2 - 1] = 2
        self.tile[self.row // 2][self.col // 2] = 2
        self.tile[self.row // 2 - 1][self.col // 2] = 1
        self.tile[self.row // 2][self.col // 2 - 1] = 1
        self.black_tile = 2
        self.white_tile = 2
        self.counter = 1  # Indicate whether player or AI's turn
        self.legal_move = False
        self.flip_tiles = []
        self.interval = 2000
        self.over = False
        self.text_position_x = self.grid.WIDTH / 2 - 100
        self.text_position_y = self.grid.HEIGHT / 2

    def display(self):
        """Drawing the tile to the screen after the player or
        computer has made a move"""
        for i in range(self.row):
            for j in range(self.col):
                # Draw white tile
                if self.tile[i][j] == 2:
                    fill(255)
                    ellipse(self.grid.SPACING * (j + 0.5),
                            self.grid.SPACING * (i + 0.5),
                            self.WIDTH, self.HEIGHT)
                # Draw black tile
                if self.tile[i][j] == 1:
                    fill(0)
                    ellipse(self.grid.SPACING * (j + 0.5),
                            self.grid.SPACING * (i + 0.5),
                            self.WIDTH, self.HEIGHT)

    def update(self, x, y):
        """Carry out necessary updates for each frame before
        drawing to screen"""
        row = y // self.grid.SPACING
        col = x // self.grid.SPACING
        legal_move_black = False
        for i in range(self.row):
            for j in range(self.col):
                if self.check_legal_move(i, j):
                    legal_move_black = True
        if legal_move_black:
            self.legal_move = self.check_legal_move(row, col)
        else:
            self.counter = 2
            print("No legal move for black. AI's turn")
        if self.legal_move:
            if self.counter == 1:
                self.tile[row][col] = 1
                self.counter += 1
                for tile in self.flip_tiles:
                    m = tile[0]
                    n = tile[1]
                    self.tile[m][n] = 1
                self.black_tile += 1
                self.black_tile += len(self.flip_tiles)
                self.white_tile -= len(self.flip_tiles)
                self.display()

    def game_over(self):
        """Graphical functionality. Announce winner as text
        on the screen when the game is over"""
        if self.black_tile + self.white_tile == self.full_tile:
            self.over = True
            if self.black_tile > self.white_tile:
                fill(56, 246, 137)
                textSize(50)
                text("Black Wins", self.text_position_x,
                     self.text_position_y)
            elif self.black_tile < self.white_tile:
                fill(56, 246, 137)
                textSize(50)
                text("White wins", self.text_position_x,
                     self.text_position_y)
            else:
                fill(56, 246, 137)
                textSize(50)
                text("Draw", self.text_position_x, self.text_position_y)
        elif self.black_tile == 0:
            self.over = True
            fill(56, 246, 137)
            textSize(50)
            text("White Wins", self.text_position_x, self.text_position_y)
        elif self.white_tile == 0:
            self.over = True
            fill(56, 246, 137)
            textSize(50)
            text("Black Wins", self.text_position_x, self.text_position_y)

    def record(self, name):
        """Sace user name and score in a file"""
        string = name + " " + str(self.black_tile) + "\n"
        with open("Score.txt", 'r') as rf:
            line = rf.readline()
            if line:
                score = line.split(" ")[-1]
                # When current score is higher than score on the top,
                # preappend it to the begining.
                # Otherwise, append it to the last.
                if self.black_tile >= int(score):
                    with open("Score.txt", "r+") as f:
                        old = f.read()
                        f.seek(0)
                        f.write(string + old)
                else:
                    with open("Score.txt", "a") as f:
                        f.write(string)
            else:
                with open("Score.txt", "a") as f:
                    f.write(string)

    def ai_turn(self):
        """AI makes move and flip tiles in between"""
        if self.counter == 2:
            legal_move = self.computer.all_legal_moves()
            self.computer.ai_make_move()

    def check_legal_move(self, row, col):
        """checks whether a specified move is legal or not. If it is legal,
        add the tiles that are about to be flipped to a list.
        Args:
            row: y coordinate of the point
            col: x coordinate of the point
        Return:
            True if the move is legal. Otherwise False
        """
        del self.flip_tiles[:]
        legal_move = False
        right_legal_move = False
        left_legal_move = False
        up_legal_move = False
        bottom_legal_move = False
        ul_legal_move = False
        ur_legal_move = False
        bl_legal_move = False
        br_legal_move = False
        right_tile, left_tile, up_tile, bottom_tile = [], [], [], []
        ul_tile, ur_tile, bl_tile, br_tile = [], [], [], []

        if self.tile[row][col] == 0:
            # Check legal move for black tile
            if self.counter == 1:
                # To the right
                for i in range(col, self.col):
                    if self.tile[row][i] == 1:
                        i = i - 1
                        while i > col:
                            if self.tile[row][i] != 2:
                                right_legal_move = False
                                del right_tile[:]
                                break
                            else:
                                flip_tile = (row, i)
                                right_tile.append(flip_tile)
                                right_legal_move = True
                            i -= 1
                        break
                # To the left
                for i in range(col, -1, -1):
                    if self.tile[row][i] == 1:
                        i = i + 1
                        while i < col:
                            if self.tile[row][i] != 2:
                                left_legal_move = False
                                del left_tile[:]
                                break
                            else:
                                flip_tile = (row, i)
                                left_tile.append(flip_tile)
                                left_legal_move = True
                            i += 1
                        break
                # To the top
                for i in range(row, -1, -1):
                    if self.tile[i][col] == 1:
                        i = i + 1
                        while i < row:
                            if self.tile[i][col] != 2:
                                up_legal_move = False
                                del up_tile[:]
                                break
                            else:
                                flip_tile = (i, col)
                                up_tile.append(flip_tile)
                                up_legal_move = True
                            i += 1
                        break
                # To the bottom
                for i in range(row, self.row):
                    if self.tile[i][col] == 1:
                        i = i - 1
                        while i > row:
                            if self.tile[i][col] != 2:
                                bottom_legal_move = False
                                del bottom_tile[:]
                                break
                            else:
                                flip_tile = (i, col)
                                bottom_tile.append(flip_tile)
                                bottom_legal_move = True
                            i -= 1
                        break
                # Upper left
                i, j = row, col
                while i >= 0 and j >= 0:
                    if self.tile[i][j] == 1:
                        i = i + 1
                        j = j + 1
                        while i < row and j < col:
                            if self.tile[i][j] != 2:
                                ul_legal_move = False
                                del ul_tile[:]
                                break
                            else:
                                flip_tile = (i, j)
                                ul_tile.append(flip_tile)
                                ul_legal_move = True
                            i += 1
                            j += 1
                        break
                    i -= 1
                    j -= 1
                # Upper right
                i, j = row, col
                while i >= 0 and j < self.col:
                    if self.tile[i][j] == 1:
                        i = i + 1
                        j = j - 1
                        while i < row and j > col:
                            if self.tile[i][j] != 2:
                                ur_legal_move = False
                                del ur_tile[:]
                                break
                            else:
                                flip_tile = (i, j)
                                ur_tile.append(flip_tile)
                                ur_legal_move = True
                            i += 1
                            j -= 1
                        break
                    i -= 1
                    j += 1
                # Bottom left
                i, j = row, col
                while i < self.row and j >= 0:
                    if self.tile[i][j] == 1:
                        i = i - 1
                        j = j + 1
                        while i > row and j < col:
                            if self.tile[i][j] != 2:
                                bl_legal_move = False
                                del bl_tile[:]
                                break
                            else:
                                flip_tile = (i, j)
                                bl_tile.append(flip_tile)
                                bl_legal_move = True
                            i -= 1
                            j += 1
                        break
                    i += 1
                    j -= 1
                # Bottom right
                i, j = row, col
                while i < self.row and j < self.col:
                    if self.tile[i][j] == 1:
                        i = i - 1
                        j = j - 1
                        while i > row and j > col:
                            if self.tile[i][j] != 2:
                                br_legal_move = False
                                del br_tile[:]
                                break
                            else:
                                flip_tile = (i, j)
                                br_tile.append(flip_tile)
                                br_legal_move = True
                            i -= 1
                            j -= 1
                        break
                    i += 1
                    j += 1
            # Check legal move for white tile
            if self.counter == 2:
                # To the right
                for i in range(col, self.col):
                    if self.tile[row][i] == 2:
                        i = i - 1
                        while i > col:
                            if self.tile[row][i] != 1:
                                right_legal_move = False
                                del right_tile[:]
                                break
                            else:
                                flip_tile = (row, i)
                                right_tile.append(flip_tile)
                                right_legal_move = True
                            i -= 1
                        break
                # To the left
                for i in range(col, -1, -1):
                    if self.tile[row][i] == 2:
                        i = i + 1
                        while i < col:
                            if self.tile[row][i] != 1:
                                left_legal_move = False
                                del left_tile[:]
                                break
                            else:
                                flip_tile = (row, i)
                                left_tile.append(flip_tile)
                                left_legal_move = True
                            i += 1
                        break
                # To the top
                for i in range(row, -1, -1):
                    if self.tile[i][col] == 2:
                        i = i + 1
                        while i < row:
                            if self.tile[i][col] != 1:
                                up_legal_move = False
                                del up_tile[:]
                                break
                            else:
                                flip_tile = (i, col)
                                up_tile.append(flip_tile)
                                up_legal_move = True
                            i += 1
                        break
                # To the bottom
                for i in range(row, self.row):
                    if self.tile[i][col] == 2:
                        i = i - 1
                        while i > row:
                            if self.tile[i][col] != 1:
                                bottom_legal_move = False
                                del bottom_tile[:]
                                break
                            else:
                                flip_tile = (i, col)
                                bottom_tile.append(flip_tile)
                                bottom_legal_move = True
                            i -= 1
                        break
                # Upper left
                i, j = row, col
                while i >= 0 and j >= 0:
                    if self.tile[i][j] == 2:
                        i = i + 1
                        j = j + 1
                        while i < row and j < col:
                            if self.tile[i][j] != 1:
                                ul_legal_move = False
                                del ul_tile[:]
                                break
                            else:
                                flip_tile = (i, j)
                                ul_tile.append(flip_tile)
                                ul_legal_move = True
                            i += 1
                            j += 1
                        break
                    i -= 1
                    j -= 1
                # Upper right
                i, j = row, col
                while i >= 0 and j < self.col:
                    if self.tile[i][j] == 2:
                        i = i + 1
                        j = j - 1
                        while i < row and j > col:
                            if self.tile[i][j] != 1:
                                ur_legal_move = False
                                del ur_tile[:]
                                break
                            else:
                                flip_tile = (i, j)
                                ur_tile.append(flip_tile)
                                ur_legal_move = True
                            i += 1
                            j -= 1
                        break
                    i -= 1
                    j += 1
                # Bottom left
                i, j = row, col
                while i < self.row and j >= 0:
                    if self.tile[i][j] == 2:
                        i = i - 1
                        j = j + 1
                        while i > row and j < col:
                            if self.tile[i][j] != 1:
                                bl_legal_move = False
                                del bl_tile[:]
                                break
                            else:
                                flip_tile = (i, j)
                                bl_tile.append(flip_tile)
                                bl_legal_move = True
                            i -= 1
                            j += 1
                        break
                    i += 1
                    j -= 1
                # Bottom right
                i, j = row, col
                while i < self.row and j < self.col:
                    if self.tile[i][j] == 2:
                        i = i - 1
                        j = j - 1
                        while i > row and j > col:
                            if self.tile[i][j] != 1:
                                br_legal_move = False
                                del br_tile[:]
                                break
                            else:
                                flip_tile = (i, j)
                                br_tile.append(flip_tile)
                                br_legal_move = True
                            i -= 1
                            j -= 1
                        break
                    i += 1
                    j += 1
        legal_move = (right_legal_move or left_legal_move or up_legal_move or
                      bottom_legal_move or ul_legal_move or ur_legal_move or
                      bl_legal_move or br_legal_move)
        self.flip_tiles = (right_tile + left_tile + up_tile + bottom_tile +
                           ul_tile + ur_tile + bl_tile + br_tile)
        return legal_move
