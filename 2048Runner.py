import pygame, sys
from pygame.locals import *
from constants import *
from tile import *
from random import randint as rand

pygame.init()
screen = pygame.display.set_mode((screenSize, screenSize))

board = []
for i in range(gridSize):
    board.append([])
    for j in range(gridSize):
        board[i].append(Tile(i, j))

grid = []
for i in range(gridSize):
    grid.append([])
    for j in range(gridSize):
        grid[i].append(0)

def flip():
    pass

while True:
    screen.fill(gray(200))

    for i in range(gridSize):
        for j in range(gridSize):
            tile = board[i][j]

            tile.setNum(grid)

            tile.draw(screen)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
