from turtle import Turtle
import random as rd

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.comer()

    def comer(self):
        xPos = rd.randint(-280, 280)
        yPos = rd.randint(-280, 280)
        self.setposition(xPos, yPos)