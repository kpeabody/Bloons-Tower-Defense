import turtle

#I only need a turtle object when I am wanting to draw a turtle
#Bg stands for background image

class Window (turtle):
    
    def _init_(self, width, height, startx, starty, turtle):
        self.turtle = turtle
        self.width = width
        self.height = height
        self.startx = startx
        self.starty = starty

        turtle = turtle.Screen()
        #Sets the title of the screen
        turtle.title("Bloons Tower Defense Game")
        #Sets background color of the screen
        turtle.bgcolor("white")
        #Sets the size and position of the screen
        turtle.setup(width, height, startx, starty)
        #Used to speed up the speed of complex graphics.  It will basically draw on the screen n number of times.
        turtle.tracer(0)
        #This seems to be the function which allows the game to run.  Basically if tracer is turned off then the screen will update.
        while True:
            turtle.update()

main_turtle = turtle
window = Window(800, 600, 20, 7, main_turtle)






    
