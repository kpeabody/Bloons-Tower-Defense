import pygame as py
import numpy as np
#Should I make the block class extend the turtle class?
#This way the Block class will have the same properties as turtle with some additional properties like x, y, width, height, IDGround, IDAir
#I think I need to have the block class inherit the turtle class 100%
class Block():
    testarray = np.genfromtxt('map1.txt', delimiter = ',')
    grass = py.image.load('grass.gif')
    redgrass = py.image.load('redgrass.gif')
    def __init__(self, x, y, size, Id):
        self.x = x
        self.y = y
        self.size = size
        self.Id = Id
    width = 800
    height = 600
    blockpy = py.display.set_mode((width, height))

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
        if(self.Id == 0):
            self.blockpy.blit(grass, (self.x, self.y))
        elif(self.Id == 1):
            self.blockpy.blit(redgrass, (self.x,self.y))
        #Creates Duplicates of the blockturtle object.  THis way we aren't changing data for the same turtle each time.
    
    def DrawGrid(self, row_count, column_count):
        #x constant which is set equal to the initial x position
        xCons = self.x
        #y constant which is set equal to the initial y position
        yCons = self.y
        for c in range(column_count):
            for r in range(row_count):
                self.SetXCoor(xCons + (c*self.size))
                self.SetYCoor(yCons - (r*self.size))
                if(self.testarray[r][c]==1):
                    self.Id = 1
                elif(self.testarray[r][c]==0):
                    self.Id = 0
                self.DrawBlock()
