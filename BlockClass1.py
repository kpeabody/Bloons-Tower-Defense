import turtle
import numpy as np
#Should I make the block class extend the turtle class?
#This way the Block class will have the same properties as turtle with some additional properties like x, y, width, height, IDGround, IDAir
#I think I need to have the block class inherit the turtle class 100%
class Block():
    blockturtle = turtle.Turtle()
    testarray = np.genfromtxt('map1.txt', delimiter = ',')
    turtle.addshape('grass.gif')
    turtle.addshape('redgrass.gif')
    def __init__(self, x, y, size, Id):
        self.x = x
        self.y = y
        self.size = size
        self.Id = Id

    def GetXCoor(self):
        return self.x
    
    def SetXCoor(self, x):
        self.x = x
    
    def GetYCoor(self,y):
        return self.y
    
    def SetYCoor(self, y):
        self.y = y

    def GetSize(self):
        return self.size

    def SetSize(self, size):
        self.size = size

    def DrawBlock(self):
        self.blockturtle.penup()
        self.blockturtle.speed(0)
        if(self.Id == 0):
            self.blockturtle.shape('grass.gif')
        elif(self.Id == 1):
            self.blockturtle.shape('redgrass.gif')
        #Creates Duplicates of the blockturtle object.  THis way we aren't changing data for the same turtle each time.
        self.blockturtle.stamp()

    def DrawGrid(self, row_count, column_count):
        #x constant which is set equal to the initial x position
        xCons = self.x
        #y constant which is set equal to the initial y position
        yCons = self.y
        for c in range(column_count):
            for r in range(row_count):
                self.blockturtle.penup()
                self.SetXCoor(xCons + (c*self.size))
                self.SetYCoor(yCons - (r*self.size))
                if(self.testarray[r][c]==1):
                    self.Id = 1
                elif(self.testarray[r][c]==0):
                    self.Id = 0
                '''
                if(self.y <= (yCons + 0*self.size)):
                    self.Id = 1
                elif(self.x == xCons + (column_count-1)*self.size and self.y <= yCons + int(row_count/5)*self.size):
                    self.Id = 1
                elif(self.y == yCons + int(row_count/5)*self.size):
                    self.Id = 1
                elif(self.x == xCons + 0*self.size and self.y >= yCons + int(row_count/5)*self.size and self.y <= yCons + int(2*row_count/5)*self.size):
                    self.Id = 1
                else:
                    self.Id = 0
                '''
                self.blockturtle.setpos(self.x,self.y)
                self.DrawBlock()

    def PrintArray(self):
        print(self.testarray)
