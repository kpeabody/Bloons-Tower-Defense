import turtle
import Window1

#I only need a turtle object when I am wanting to draw a turtle
#Bg stands for background image

main_turtle = turtle.Screen()
#Used to speed up the speed of complex graphics.  It will basically draw on the screen n number of times.
main_turtle.tracer(0)
#This seems to be the function which allows the game to run.  Basically if tracer is turned off then the screen will update.
while True:
    main_turtle.update()

denum = Window1(800, 600, 20, 7, main_turtle)






    
