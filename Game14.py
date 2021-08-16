import pygame as py
import numpy as np
import sys
from EnemyClass import Enemy

width = 800
height = 600
blockSize = 20
xCoor = 80
yCoor = 5

class Game():
    def __init__(self, x, y, width, height, blockSize):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.blockSize = blockSize
        self.screen = py.display.set_mode((self.width, self.height))
        self.row_count = 33
        self.column_count = 23
        self.gridarr = np.genfromtxt('map1.txt', delimiter = ',')
        self.grass = py.image.load('grass.gif')
        self.redgrass = py.image.load('redgrass.gif')
        self.enemy = []
        self.tower = []

    def GetXCoor(self):
        return self.x
    
    def SetXCoor(self, x):
        self.x = x
    
    def GetYCoor(self,y):
        return self.y
    
    def SetYCoor(self, y):
        self.y = y

    def GetSize(self):
        return self.blockSize

    def SetSize(self, blockSize):
        self.blockSize = blockSize

    def GetTestArray(self):
        return self.gridarr

    def PrintArray(self):
        print(self.gridarr)

    def run(self):
        gameover = False
        FPS = 60
        clock = py.time.Clock()

        en = Enemy(xCoor + self.row_count*self.blockSize - self.blockSize, yCoor + self.blockSize, self.blockSize, self.gridarr)

        while not gameover:
            self.screen.fill((0,0,0))
            self.DrawGrid()
            en.Draw(self.screen, self.row_count, self.column_count)
            for event in py.event.get():
                if event.type == py.QUIT:
                    gameover = True
            #Sets the frames per second the run loop will draw things onto the screen
            clock.tick(FPS)
            py.display.update()

    def DrawGrid(self):
        #Remember gridarr derives data from a file called map1.txt.

        #x constant which is set equal to the initial x position
        xCons = self.x
        #y constant which is set equal to the initial y position
        yCons = self.y
        for r in range(self.row_count):
            for c in range(self.column_count):
                self.SetXCoor(xCons + (r*self.blockSize))
                self.SetYCoor(yCons + (c*self.blockSize))
                if(self.gridarr[c][r] == 0):
                    self.screen.blit(self.grass, (self.x, self.y))
                elif(self.gridarr[c][r] == 1):
                    self.screen.blit(self.redgrass, (self.x, self.y))
        self.x = xCons
        self.y = yCons

game = Game(xCoor,yCoor, width, height, 20)
game.run()
