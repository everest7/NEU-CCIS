from grid import Grid


class Tile:
    def __init__(self):
        """Initialize the tile with a nested list"""
        self.WIDTH = 90
        self.HEIGHT = 90
        self.grid = Grid(400, 400, 100)
        self.row = self.grid.WIDTH // self.grid.SPACING
        self.col = self.grid.HEIGHT // self.grid.SPACING
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
        self.black_tile = 2  # number of black tile
        self.white_tile = 2  # number of white tile
        self.counter = 1  # Indicate who's turn
        self.over = False

    def display(self):
        """Display the checkerboard"""
        for i in range(self.row):
            for j in range(self.col):
                if self.tile[i][j] == 2:
                    fill(255)
                    noStroke()
                    ellipse(self.grid.SPACING * (i + 0.5),
                            self.grid.SPACING * (j + 0.5),
                            self.WIDTH, self.HEIGHT)
                if self.tile[i][j] == 1:
                    fill(0)
                    noStroke()
                    ellipse(self.grid.SPACING * (i + 0.5),
                            self.grid.SPACING * (j + 0.5),
                            self.WIDTH, self.HEIGHT)
        # if self.black_tile + self.white_tile == self.full_tile:
        #     if self.black_tile == self.white_tile:
        #         fill(153, 255, 51)
        #         textSize(25)
        #         string1 = "Game Over. Tied!"
        #         text(string1, self.grid.WIDTH/2 - 95, self.grid.HEIGHT/2)
        #         string2 = "Black tiles: " + str(self.black_tile) +\
        #             "\nWhite Tiles: " + str(self.white_tile)
        #         text(string2, self.grid.WIDTH/2 - 95, self.grid.HEIGHT/2 + 30)
        #     elif self.black_tile > self.white.tile:
        #         fill(153, 255, 51)
        #         textSize(50)
        #         text("Black Wins!!!", self.grid.WIDTH/2 - 95,
        #              self.grid.HEIGHT/2)
        #         string2 = "Black tiles: " + str(self.black_tile) +\
        #             "\nWhite Tiles: " + str(self.white_tile)
        #         text(string2, self.grid.WIDTH/2 - 95, self.grid.HEIGHT/2 + 30)
        #     elif self.black_tile < self.white_tile:
        #         fill(153, 255, 51)
        #         textSize(50)
        #         text("White Wins!!!", self.grid.WIDTH/2 - 95,
        #              self.grid.HEIGHT/2)
        #         string2 = "Black tiles: " + str(self.black_tile) +\
        #             "\nWhite Tiles: " + str(self.white_tile)
        #         text(string2, self.grid.WIDTH/2 - 95, self.grid.HEIGHT/2 + 30)

    def update(self, x, y):
        """Alternate between the black and white tile"""
        row = x // self.grid.SPACING
        col = y // self.grid.SPACING
        if self.tile[row][col] == 0:
            if self.counter == 1:
                self.tile[row][col] = 1
                self.counter += 1
                self.black_tile += 1
            elif self.counter == 2:
                self.tile[row][col] = 2
                self.counter -= 1
                self.white_tile += 1

    def record(self, name):
        string = name + " " + str(self.black_tile) + "\n"
        with open("Score.txt", 'r') as rf:
            # if len(rf.readlines()) > 0:  # Check if txt file is empty
            line = rf.readline()
            if line:
                score = line.split(" ")[1]
                print(score)
                print(self.black_tile)
                # When current score is higher than score on the top,
                # preappend the it to the begining.
                # Otherwise, append it to the last.
                if self.black_tile >= int(score):
                    print("!!")
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

    def game_over(self):
        if self.black_tile + self.white_tile == self.full_tile:
            self.over = True
            if self.black_tile > self.white_tile:
                fill(0, 105, 0)
                textSize(50)
                text("Black Wins", self.grid.WIDTH/2 - 80,
                     self.grid.HEIGHT/2)
            elif self.black_tile < self.white_tile:
                fill(0, 105, 0)
                textSize(50)
                text("White wins", self.grid.WIDTH/2 - 80,
                     self.grid.HEIGHT/2)
            else:
                fill(56, 246, 137)
                textSize(50)
                # textAlign(CENTER, CENTER)
                text("Draw", self.grid.WIDTH/2 - 80, self.grid.HEIGHT/2)
        elif self.black_tile == 0:
            self.over = True
            fill(0, 105, 0)
            textSize(50)
            text("White Wins!!!", self.grid.WIDTH/2 - 80, self.grid.HEIGHT/2)
        elif self.white_tile == 0:
            self.over = True
            fill(0, 105, 0)
            textSize(50)
            text("Black Wins!!!", self.grid.WIDTH/2 - 80, self.grid.HEIGHT/2)

    def refresh(self):
        del self.tile[:]
        self.tile = [[0] * self.col for i in range(self.row)]
        # Initialize starting four tiles.
        # 1 stands for black tile
        # 2 stands for white tile
        self.tile[self.row // 2 - 1][self.col // 2 - 1] = 2
        self.tile[self.row // 2][self.col // 2] = 2
        self.tile[self.row // 2 - 1][self.col // 2] = 1
        self.tile[self.row // 2][self.col // 2 - 1] = 1
        self.black_tile = 2  # number of black tile
        self.white_tile = 2  # number of white tile
        self.counter = 1  # Indicate who's turn
        self.over = False
        print(self.tile)
        
        
