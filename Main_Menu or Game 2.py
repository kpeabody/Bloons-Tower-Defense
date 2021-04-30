import turtle

#Bg stands for background image

#Variables for Window Setup
width = 800
height = 600
startx = 20
starty = 7

#Variables for game logic
running = True
playing = False


window = turtle.Screen()
#Sets the title of the screen
window.title("Bloons Tower Defense Game")
#Sets background color of the screen
window.bgcolor("white")
#Sets the size and position of the screen
window.setup(width, height, startx, starty)
#Used to speed up the speed of complex graphics.  It will basically draw on the screen n number of times.
window.tracer(0)
#This seems to be the function which allows the game to run.  Basically if tracer is turned off then the screen will update.
while True & notMenu1 & notMenu2:  #If the game is a part of the menue it also won't update
    window.update()
elif notMenu1
    notMenu1 = 