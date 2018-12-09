from grid import Grid
from tile import Tile
WIDTH = 400
HEIGHT = 400
SPACING = 100
grid = Grid(WIDTH, HEIGHT, SPACING)
tile = Tile()


def setup():
    background(88, 178, 220)
    size(WIDTH, HEIGHT)


def draw():
    grid.display()
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


def keyPressed():
    print("KeyPressed")
    if key == 'r':
        print("r pressed")
        tile.refresh()
        print("Refreshed")
    tile.display()


def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
