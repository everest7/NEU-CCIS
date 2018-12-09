

class Computer:
    def __init__(self, tile):
        """Computer constructor"""
        self.ai_turn = False
        self.player_turn = False
        self.ai_legal_moves = []
        self.player_legal_moves = []
        self.tile = tile
        self.best_move = [0, 0]

    def all_legal_moves(self):
        """Check all grid in the board, add the legal move
        for computer into a list, record the move that will flip
        the most black tiles."""
        maxi = 0
        for i in range(self.tile.row):
            for j in range(self.tile.col):
                if self.tile.check_legal_move(i, j):
                    move = (i, j)
                    self.ai_legal_moves.append(move)
                    if len(self.tile.flip_tiles) >= maxi:
                        maxi = len(self.tile.flip_tiles)
                        self.best_move[0] = i
                        self.best_move[1] = j
        return self.ai_legal_moves

    def ai_make_move(self):
        """AI choose one of the legal moves that flips
        the most white tiles"""
        r = self.best_move[0]
        c = self.best_move[1]
        if self.tile.check_legal_move(r, c):
            for tile in self.tile.flip_tiles:
                m = tile[0]
                n = tile[1]
                self.tile.tile[m][n] = 2
        self.tile.white_tile += 1
        self.tile.white_tile += len(self.tile.flip_tiles)
        self.tile.black_tile -= len(self.tile.flip_tiles)
        self.tile.tile[r][c] = 2
        self.tile.counter -= 1
