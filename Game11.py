import turtle
import numpy as np
from WindowClass1 import Window1
from BlockClass1 import Block

#I only need a turtle object when I am wanting to draw a turtle
#Bg stands for background image

#Used to speed up the speed of complex graphics.  It will basically draw on the screen n number of times.
screen = turtle.Screen()

GameWindow = Window1(800, 600, 20, 7, screen)

'''
for col in range(len(blockArray1)):
    blockArray1.append([Block(-300,-100,20,0)])
    for row in range(len(blockArray1[col])):
        blockArray1[col].append(Block(-300,-100,20,0))
print(str(blockArray1))
'''
'''
for i in range(i):
    blockArray2.append(Block(-300,-100 + (i*20),20,0))
    blockArray2[i].DrawBlock()
for i in range(i+1):
    blockArray2.append(Block(-300 + (i*20),-100,20,0))
    blockArray2[i+j].DrawBlock()
'''
'''
count = 0
for i in range(i):
    for j in range(j):
        blockArray2.append(Block(-300,-100 + (j*20),20,0))
        blockArray2[j].DrawBlock()
        count = j
    blockArray2.append(Block(-300 + ((count+i)*20),-100,20,0))
    blockArray2[i+count+1].DrawBlock()
'''
r = 1
c = 1
count = 0
blockArray1 = np.array(Block(-300 + 0*20,-100,20,0))
blockArray2 = np.array([Block(-300 + 1*20,-100,20,0)])
blockArray1 = np.expand_dims(blockArray2, axis=0)
for c in range(c):
    for r in range(r):
        blockArray1[r][c].DrawBlock()
        print("Custom: (" + str(r) + "," + str(c) + ")")
print(blockArray1.shape)
print(blockArray1.ndim)
print(blockArray1)

#This keeps the turtle objects drawing on the screen
turtle.done()
