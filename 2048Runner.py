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
                                
def flip(array):
    flip = []
    for a in range(len(array)):
        flip.append([])
        for b in range(len(array)):
            flip[a].append(array[b][a])

    return flip

key = None

while True:
    screen.fill(gray(200))

    for i in range(gridSize):
        for j in range(gridSize):
            tile = board[i][j]

            tile.setNum(grid)

            tile.draw(screen)
            
    for i in range(gridSize):
        for j in range(gridSize):
            
            if key == "up":
                grid = flip(grid)
                count = 0
                while 0 in grid[i]:
                    grid[i].remove(0)
                    count += 1
                    
                for x in range(count):               
                        grid[i].insert(gridSize - 1, 0)   
                
                grid = flip(grid)
                    
            elif key == "right":
                count = 0
                while 0 in grid[i]:
                    grid[i].remove(0)
                    count += 1
                    
                for x in range(count):
                    grid[i].insert(0, 0)
                    
            elif key == "down":
                grid = flip(grid)
                count = 0
                while 0 in grid[i]:
                    grid[i].remove(0)
                    count += 1
                    
                for x in range(count):
                    grid[i].insert(0, 0)
                    
                grid = flip(grid)

            elif key == "left":
                count = 0
                while 0 in grid[i]:
                    grid[i].remove(0)
                    count += 1
                    
                for x in range(count):               
                    grid[i].insert(gridSize - 1, 0)                
            

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
            
        if event.type == KEYDOWN and event.key == K_UP:
            key = "up"
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            key = "right"
        elif event.type == KEYDOWN and event.key == K_DOWN:
            key = "down"
        elif event.type == KEYDOWN and event.key == K_LEFT:       
            key = "left"
        else:
            key = None