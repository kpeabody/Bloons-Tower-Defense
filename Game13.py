import sys
import numpy as np
import pygame as py
from BlockClass2 import Block

width = 800
height = 600
size = (width, height)
gameover = False

py.init()

screen = py.display.set_mode((width, height))

grass = py.image.load('grass.gif')
redgrass = py.image.load('redgrass.gif')

while not gameover:
    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()
        row_count = 21
        column_count = 31
        count = 0

        block = Block(-300,280,20,0,screen)
        block.CreateGrid(row_count, column_count)

        testarray2 = block.GetTestArray()
        print(testarray2)

        for r in range(row_count):
            for c in range(column_count):
                if(testarray2[r][c] == 0):
                    screen.blit(grass, (c*block.GetSize(), r*block.GetSize()))
                elif(testarray2[r][c] == 1):
                    screen.blit(redgrass, (c*block.GetSize(), r*block.GetSize()))
        
        py.display.update()
