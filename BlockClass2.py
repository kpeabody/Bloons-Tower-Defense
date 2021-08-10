import pygame as py
import numpy as np
class Block():
    testarray = np.genfromtxt('map1.txt', delimiter = ',')
    width = 800
    height = 600
    #blockpy = py.display.set_mode((width, height))
    grass = py.image.load('grasstest.png')
    #redgrass = py.image.load('redgrass.gif')
    def __init__(self, x, y, size, Id, screen):
        self.x = x
        self.y = y
        self.size = size
        self.Id = Id
        self.screen = screen

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

    def GetTestArray(self):
        return self.testarray

    #Remember the DrawGrid class derives data from a file called map1.txt.
    #Returns testarray so the Id values of each grid block is known
    def CreateGrid(self, row_count, column_count):
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

    def PrintArray(self):
        print(self.testarray)
