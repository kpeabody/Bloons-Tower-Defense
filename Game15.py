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
        self.start_img = py.image.load('start.gif')
        self.start = py.transform.scale(self.start_img, (40,40))
        self.end_img = py.image.load('end.gif')
        self.end = py.transform.scale(self.end_img, (40,40))
        self.enemy = []
        self.tower = []
        #The enemies initial x and y position must remain constant
        self.EN_X = 0
        self.EN_Y = 0
        self.en = None
        self.enArr = []
        self.extragridinfo = np.array([0,0])

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

        while not gameover:
            self.screen.fill((0,0,0))
            self.Draw()
            for event in py.event.get():
                if event.type == py.QUIT:
                    gameover = True
            #Sets the frames per second the run loop will draw things onto the screen
            clock.tick(FPS)
            py.display.update()

    def AddToGridInfo(self, ACoor, BCoor):
        self.extragridinfo = np.append(self.extragridinfo, [ACoor, BCoor])

    def Draw(self):
        #Remember gridarr derives data from a file called map1.txt.

        #x constant which is set equal to the initial x position
        xCons = self.x
        #y constant which is set equal to the initial y position
        yCons = self.y
        #Draws the grid, enemies, towers, ect.
        for r in range(self.row_count):
            for c in range(self.column_count):
                self.SetXCoor(xCons + (r*self.blockSize))
                self.SetYCoor(yCons + (c*self.blockSize))
                #Deletes the initialized [0,0] coordinates which are only used as place holders.
                if(self.extragridinfo.size == (self.row_count * self.column_count) * 2):
                    self.extragridinfo = np.delete(self.extragridinfo, 0)
                    self.extragridinfo = np.delete(self.extragridinfo, 0)
                #Creates coordinates of every block on the grid in (x, y)
                if(self.extragridinfo.size < ((self.row_count * self.column_count) * 2) + 1):
                    self.AddToGridInfo(xCons + (r*self.blockSize), yCons + (c*self.blockSize))
                #Draws Grass
                if(self.gridarr[c][r] == 0):
                    self.screen.blit(self.grass, (self.x, self.y))
                #Draws Red Grass
                elif(self.gridarr[c][r] == 1):
                    self.screen.blit(self.redgrass, (self.x, self.y))
                #Draws Start
                elif(self.gridarr[c][r] == 2):
                    self.screen.blit(self.start, (self.x, self.y))
                    #This variable is needed for the enemy class
                    en_startx = self.x
                    en_starty = self.y
                #Draws End
                elif(self.gridarr[c][r] == 3):
                    self.screen.blit(self.end, (self.x, self.y))
        self.x = xCons
        self.y = yCons

        #Logic works because an enemy is only created once.
        if(self.en == None):
            self.PrintOnlyOnce()

        #This declares the enemy if the enemy has not already been declared
        if (self.en == None):
            self.en = Enemy(en_startx, en_starty, self.blockSize, self.gridarr)

        self.enArr = [self.en]
        
        for x in range(1,6):
            self.enArr = np.append(self.enArr, Enemy(en_startx + (x*20), en_starty, self.blockSize, self.gridarr))
            self.enArr[x-1].Draw(self.screen, self.row_count, self.column_count)
            print(self.enArr)

    #Prints ExtraGridInfo Array and GridArr Array
    def PrintOnlyOnce(self):
        if(self.extragridinfo.size < ((self.row_count * self.column_count) * 2) + 1):
            self.extragridinfo = self.extragridinfo.reshape((self.row_count * self.column_count),2)
            print('Coordinates For Every Point Array')
            print(self.extragridinfo)
        print('Grid Array')
        print(self.gridarr)

game = Game(xCoor,yCoor, width, height, 20)
game.run()
