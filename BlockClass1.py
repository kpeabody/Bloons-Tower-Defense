import turtle
#Should I make the block class extend the turtle class?
#This way the Block class will have the same properties as turtle with some additional properties like x, y, width, height, IDGround, IDAir
#I think I need to have the block class inherit the turtle class 100%
class Block():
    blockturtle = turtle.Turtle()
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
            self.blockturtle.color("red")
        elif(self.Id == 1):
            self.blockturtle.color("green")
        turtle.register_shape("test_square", ((0,0),(0,self.size),(self.size,self.size),(self.size,0)))
        self.blockturtle.shape("test_square")
        #Creates Duplicates of the blockturtle object.  THis way we aren't changing data for the same turtle each time.
        self.blockturtle.stamp()

    def DrawGrid(self, row_count, column_count):
        for c in range(column_count):
            for r in range(row_count):
                self.blockturtle.penup()
                self.SetXCoor(-300 + (c*self.size))
                self.SetYCoor(-100 + (r*self.size))
                self.blockturtle.setpos(self.x,self.y)
                self.DrawBlock()
