import pygame as py
import numpy as np
import sys
from EnemyClass import Enemy


py.init()

width = 800
height = 600
#The grid x start position
xCons = -300
#The grid y start position
yCons = 280
blockSize = 20

class Game():
    def __init__(self, x, y, width, height, blockSize, Id):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.blockSize = blockSize
        self.Id = Id
        self.screen = py.display.set_mode((self.width, self.height))
        self.row_count = 21
        self.column_count = 31
        self.gridarr = np.genfromtxt('map1.txt', delimiter = ',')
        self.grass = py.image.load('grass.gif')
        self.redgrass = py.image.load('redgrass.gif')
        self.enemy = []
        self.tower = []

    def run(self):
        gameover = False

        while not gameover:
            for event in py.event.get():
                if event.type == py.QUIT:
                    gameover = True
                    #sys.exit()
                self.CreateGrid(self.row_count, self.column_count)

                print(self.gridarr)

                for r in range(self.row_count):
                    for c in range(self.column_count):
                        if(self.gridarr[r][c] == 0):
                            self.screen.blit(self.grass, (c*game.GetSize(), r*game.GetSize()))
                        elif(self.gridarr[r][c] == 1):
                            self.screen.blit(self.redgrass, (c*game.GetSize(), r*game.GetSize()))
                en = Enemy(self.x, self.y, self.blockSize, self.gridarr)
                self.enemy.append(en)
                self.enemy[0].Draw(self.screen, self.row_count, self.column_count)
                py.display.update()

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

    #Remember the DrawGrid class derives data from a file called map1.txt.
    #Returns gridarr so the Id values of each grid game is known
    def CreateGrid(self, row_count, column_count):
        #x constant which is set equal to the initial x position
        xCons = self.x
        #y constant which is set equal to the initial y position
        yCons = self.y
        for c in range(self.column_count):
            for r in range(self.row_count):
                self.SetXCoor(xCons + (c*self.blockSize))
                self.SetYCoor(yCons - (r*self.blockSize))
                if(self.gridarr[r][c]==1):
                    self.Id = 1
                elif(self.gridarr[r][c]==0):
                    self.Id = 0

    def PrintArray(self):
        print(self.gridarr)

game = Game(xCons, yCons, width, height, 20, 0)
game.run()
