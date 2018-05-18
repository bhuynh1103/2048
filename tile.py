from pygame.draw import *
from constants import *


class Tile:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.w = screenSize // gridSize
        self.x = i * self.w
        self.y = j * self.w
        self.num = None

    def setNum(self, grid):
        self.num = grid[self.i][self.j]

    def writeNum(self, window):
        if self.num != 0:
            writeText(window, str(self.num), black, self.x + self.w * .5, self.y + self.w * .5, self.w * .75)

    def draw(self, window):
        rect(window, white, (self.x, self.y, self.w, self.w))
        rect(window, gray(200), (self.x, self.y, self.w, self.w), 2)
        self.writeNum(window)

    def shift(self):
        pass

    def collapse(self):
        pass
        
