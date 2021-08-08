import sys
import numpy as np
import pygame as py
from WindowClass2 import Window1
from BlockClass2 import Block

width = 800
height = 600
size = (width, height)
gameover = False

py.init()

screen = py.display.set_mode((width, height))

while not gameover:
    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()
        row_count = 21
        column_count = 31
        count = 0

        block = Block(-300,280,20,0)
        block.PrintArray()
        block.DrawGrid(row_count, column_count)
        
        py.display.update() 

#GameWindow = Window1(800, 600, 20, 7, screen
