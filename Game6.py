import turtle
from WindowClass import Window1
from BlockClass import Block

#I only need a turtle object when I am wanting to draw a turtle
#Bg stands for background image

#Used to speed up the speed of complex graphics.  It will basically draw on the screen n number of times.
screen = turtle.Screen()

GameWindow = Window1(800, 600, 20, 7, screen)

'''
#If tracer is turned off then the screen will update.  Remember 'tracer' is another way to refer to speed
GameWindow.GetTurtle().tracer(0)
while True:
    #This line of code will update your screen
    GameWindow.GetTurtle().update()
'''

block = Block(10,10,100,100,0,1).DrawBlock()

#This keeps the turtle objects drawing on the screen
turtle.done()






    
