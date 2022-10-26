import pygame as py
from pygame import mixer
import numpy as np
import sys
from EnemyClass import Enemy
from HumanClass import Human
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
        self.towermarket_img = py.image.load('towermarket.gif')
        self.towermarket = py.transform.scale(self.towermarket_img, (660,65))
        #The enemies initial x and y position must remain constant
        self.EN_X = 0
        self.EN_Y = 0
        self.en = None
        self.enNumber = 20
        self.enArr = []
        self.extragridinfo = np.array([0,0])
        #Used For Towers
        self.left_click_pressed = False
        self.left_click_up = False
        self.humanpos = (0,0)
        self.human = None
        self.humanArr = []
        self.human_draging = False
        self.mousepos = py.mouse.get_pos()

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
                #Logic For Human Tower In Market Place
                self.mousepos = py.mouse.get_pos()
                if event.type == py.MOUSEBUTTONDOWN and self.mousepos[0] <= 192 and self.mousepos[0] >= 80 and self.mousepos[1] >= 465 and self.mousepos[1] <=530:
                    self.human_draging = True
                    self.left_click_pressed = True
                    temp_x = 0
                    temp_y = 0
                temp_x = int
                temp_y = int

                for c in range(len(self.extragridinfo)):
                    if(self.extragridinfo[c][2] == 1):
                        temp_x = int (self.extragridinfo[c][0])
                        temp_y = int (self.extragridinfo[c][1])

                        notOnPath = not(int(self.humanpos[0]) >= temp_x and int(self.humanpos[0]) <= temp_x + self.blockSize) and not(int(self.humanpos[1]) >= temp_y and int(self.humanpos[1]) <= temp_y + self.blockSize)
                        if self.left_click_pressed == True and event.type == py.MOUSEBUTTONUP and self.left_click_up == False:
                            self.left_click_up = True
                            self.human_draging = False
                            #keep temp_human_pos
                            temp_human_pos = self.mousepos
                            if int(self.mousepos[1]) >= 465 or int(self.mousepos[0]) <= 80:
                                if int(self.mousepos[1]) >= 465:
                                    #please do not change next line but take inspiration from it's logic
                                    temp_human_pos = [int(temp_human_pos[0]), (int(self.mousepos[1])) - (abs(int(self.mousepos[1]) - 465)) - self.blockSize]
                                if int(self.mousepos[0]) <= 80:
                                    #please do not change next line but take inspiration from it's logic
                                    temp_human_pos = [(int(self.mousepos[0])) - (abs(int(self.mousepos[0])) - 80),int(temp_human_pos[1])]
                            else:
                                temp_human_pos = self.mousepos
                            self.humanpos = temp_human_pos
                        else:
                            self.left_click_up = False
                            self.human_draging = True
                            #print(self.humanArr)
                    
               
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
            for x in range(1,self.enNumber):
                self.enArr = np.append(self.enArr, Enemy(en_startx + (x*20), en_starty, self.blockSize, self.gridarr))

        for x in range(self.enNumber):
            self.enArr[x].Draw(self.screen, self.row_count, self.column_count)
        
        self.screen.blit(self.towermarket, (80, 465))
        
        if self.left_click_up == True and self.human == None and len(self.humanArr) == 0:
            self.human = Human(self.screen, self.humanpos, self.blockSize)
            self.humanArr = [self.human]
        elif self.left_click_up == True and self.human == None:
            self.human = Human(self.screen, self.humanpos, self.blockSize)
            self.humanArr = np.append(self.humanArr, self.human)
        if self.left_click_pressed == True and self.left_click_up == True:
            self.left_click_pressed = False
            self.left_click_up = False
            self.human = None
        if len(self.humanArr) != 0:
            humanArrSize = len(self.humanArr)
            for x in range(humanArrSize):
                takeo = self.humanArr[x].Draw(self.screen)
                if takeo.collidepoint(self.humanpos):
                    offset_humanposx = self.humanpos[0] - self.mousepos[0]
                    offset_humanposy = self.humanpos[1] - self.mousepos[1]
                    self.humanpos = (offset_humanposx, offset_humanposy)
                    mixer.init()
                    mixer.music.load("pinocchio.mp3")
                    mixer.music.set_volume(0.7)
                    mixer.music.play()

        if self.left_click_pressed == True:
            self.screen.blit(self.start, (self.mousepos))

    #Prints ExtraGridInfo Array and GridArr Array
    def PrintOnlyOnce(self):
        if(self.extragridinfo.size < ((self.row_count * self.column_count) * 2) + 1):
            self.extragridinfo = self.extragridinfo.reshape((self.row_count * self.column_count),2)
        #Adds gridarr to extragridinfo
        temp_gridarr = self.gridarr.reshape(759, 1)
        self.extragridinfo = np.concatenate((self.extragridinfo, temp_gridarr), axis = 1)
        print(self.extragridinfo)
    
    '''def PrintThisAlso(self):
        if(self.extragridinfo)'''
        
        
game = Game(xCoor,yCoor, width, height, 20)
game.run()
