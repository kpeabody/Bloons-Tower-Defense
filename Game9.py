import turtle
import array
from WindowClass1 import Window1
from BlockClass1 import Block

#I only need a turtle object when I am wanting to draw a turtle
#Bg stands for background image

#Used to speed up the speed of complex graphics.  It will basically draw on the screen n number of times.
screen = turtle.Screen()

GameWindow = Window1(800, 600, 20, 7, screen)

col = 4
row = 4
blockArray1 = []
blockArray2 = []

for col in range(len(blockArray1)):
    blockArray1.append([Block(-300,-100,20,0)])
    for row in range(len(blockArray1[col])):
        blockArray1[col].append(Block(-300,-100,20,0))
print(str(blockArray1))

        

#This keeps the turtle objects drawing on the screen
turtle.done()
