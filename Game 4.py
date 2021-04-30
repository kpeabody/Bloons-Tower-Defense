import turtle

#I only need a turtle object when I am wanting to draw a turtle
#Bg stands for background image

#Variables
width = 800
height = 600
startx = 20
starty = 7

temp_turtle = turtle.Screen()
#Sets the title of the screen
temp_turtle.title("Bloons Tower Defense Game")
#Sets background color of the screen
temp_turtle.bgcolor("white")
#Sets the size and position of the screen
temp_turtle.setup(width, height, startx, starty)
#Used to speed up the speed of complex graphics.  It will basically draw on the screen n number of times.
temp_turtle.tracer(0)
#This seems to be the function which allows the game to run.  Basically if tracer is turned off then the screen will update.
while True:
    temp_turtle.update()


class Window (turtle):
    
    def _init_(self, turtle):
        self.turtle = turtle

window = Window(temp_turtle)






    
