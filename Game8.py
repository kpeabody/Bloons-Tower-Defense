import turtle
import array
from WindowClass1 import Window1
from BlockClass1 import Block

#I only need a turtle object when I am wanting to draw a turtle
#Bg stands for background image

#Used to speed up the speed of complex graphics.  It will basically draw on the screen n number of times.
screen = turtle.Screen()

GameWindow = Window1(800, 600, 20, 7, screen)
'''
blockArray = []
#XCoor Blocks
for i in range(30):
    blockArray.append(Block(-300 + (i*20),-100,20,0))
    blockArray[i].DrawBlock()

#YCoor Blocks
for i in range(30,50):
    blockArray.append(Block(-300,-100 + ((i-30)*20),20,0))
    blockArray[i].DrawBlock()
'''
col = 4
rows = 4
blockArray1 = [[0]*col]*rows
blockArray2 = []

while col 

'''
i = 0
while i < range(len(blockArray1)):
    blockArray1.append(Block(-300,-100 + (i*20),20,0))
    blockArray1[i].DrawBlock()
    i += 1
    j = i - 1
    while j <= range(len(blockArray1[i])):
        blockArray1.append(Block(-300 + (i*20),-100,20,0))
        blockArray1[i].DrawBlock()
        print ('\n' + str(blockArray1))
        j += 1
''' 

#This keeps the turtle objects drawing on the screen
turtle.done()
