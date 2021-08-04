import turtle
import array
from WindowClass1 import Window1
from BlockClass1 import Block

#I only need a turtle object when I am wanting to draw a turtle
#Bg stands for background image

#Used to speed up the speed of complex graphics.  It will basically draw on the screen n number of times.
screen = turtle.Screen()

GameWindow = Window1(800, 600, 20, 7, screen)

blockArray = []
#XCoor Blocks
for i in range(30):
    blockArray.append(Block(-300 + (i*20),-100,20,0))
    blockArray[i].DrawBlock()

#YCoor Blocks
for i in range(30,50):
    blockArray.append(Block(-300,-100 + ((i-30)*20),20,0))
    blockArray[i].DrawBlock()

blockArray1 = []
blockArray2 = []

'''
i = 20
for i in range(i):
    i -= 1
    j = i
    for j in range(j):
        j -= 1
        blockArray1[j][i].append([Block(-300 + (i*30),-100 + (i*20),20,0)])
        blockArray1[j][i].DrawBlock()
'''

#This keeps the turtle objects drawing on the screen
turtle.done()
