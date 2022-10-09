from turtle import Turtle
import random as r

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("green")
        self.speed("fastest")
        self.goto(r.randint(-250,250),r.randint(-250,250))

    def replant(self):
        self.goto(r.randint(-250,250),r.randint(-250,250))