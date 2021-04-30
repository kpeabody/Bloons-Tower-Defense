import turtle

#I only need a turtle object when I am wanting to draw a turtle
#Bg stands for background image

class Screen(turtle):

    def _init_(self, width, height, startx, starty):
        self.width = width
        self.height = height
        self.startx = startx
        self.starty = starty

    screen = Screen(800, 600, 20, 7)

    window = turtle.Screen()
    #Sets the title of the screen
    window.title("Bloons Tower Defense Game")
    #Sets background color of the screen
    window.bgcolor("white")
    #Sets the size and position of the screen
    window.setup(Screen.width, Screen.height, Screen.startx, Screen.starty)
    #Used to speed up the speed of complex graphics.  It will basically draw on the screen n number of times.
    window.tracer(0)
    #This seems to be the function which allows the game to run.  Basically if tracer is turned off then the screen will update.
    while True:
      window.update()

