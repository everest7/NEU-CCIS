from grid import Grid
from tile import Tile
from computer import Computer
WIDTH = 600
HEIGHT = 600
SPACING = 100
INTERVAL = 2000
ELAPSE = millis()
grid = Grid(WIDTH, HEIGHT, SPACING)
tile = Tile()
computer = Computer(tile)
start_time = millis()


def setup():
    background(88, 178, 220)
    size(WIDTH, HEIGHT)
    ELAPSE = millis()
    INTERVAL = 2000


def draw():
    global ELAPSE, INTERVAL
    grid.display()
    if millis() - ELAPSE >= INTERVAL:
        tile.ai_turn()
        ELAPSE = millis()
    tile.display()
    tile.game_over()
    if tile.over:
        name = input("Enter your name")
        if name:
            tile.record(name)
        elif name == '':
            print('[Empty string]')
        noLoop()


def mouseReleased():
    tile.update(mouseX, mouseY)


def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
