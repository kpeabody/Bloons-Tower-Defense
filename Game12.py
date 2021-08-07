import sys
import turtle
import numpy as np
from WindowClass1 import Window1
from BlockClass1 import Block

#I only need a turtle object when I am wanting to draw a turtle
#Bg stands for background image

#Used to speed up the speed of complex graphics.  It will basically draw on the screen n number of times.
screen = turtle.Screen()

GameWindow = Window1(800, 600, 20, 7, screen)

row_count = 21
column_count = 31
count = 0

block = Block(-300,280,20,0)
block.PrintArray()
block.DrawGrid(row_count, column_count)

#This keeps the turtle objects drawing on the screen
turtle.done()
