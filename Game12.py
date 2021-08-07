import numpy as np
from WindowClass1 import Window1
from BlockClass1 import Block

#I only need a turtle object when I am wanting to draw a turtle
#Bg stands for background image

#Used to speed up the speed of complex graphics.  It will basically draw on the screen n number of times.
screen = turtle.Screen()

GameWindow = Window1(800, 600, 20, 7, screen)

row_count = 20
column_count = 30
count = 0

block = Block(-300,-100,20,0)
block.DrawGrid(row_count, column_count)
block.CreateArray()

#This keeps the turtle objects drawing on the screen
turtle.done()
