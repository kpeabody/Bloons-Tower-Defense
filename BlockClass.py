import turtle
class Block:
    def __init__(self, x, y, width, height, IDGround, IDAir):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.IDGround = IDGround
        self.IDAir = IDAir

    def GetXCoor(self):
        return self.x
    
    def GetYCoor(self):
        return self.y

    def GetWidth(self):
        return self.width

    def GetHeight(self):
        return self.height

    def DrawBlock(self):
        testturt = turtle.Turtle()
        testturt.color('red')
        testturt.penup()
        testturt.shape('square')
        testturt.goto(self.x, self.y)
