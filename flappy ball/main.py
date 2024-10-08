import pgzrun
import random

HEIGHT = 800
WIDTH = 800
TITLE = "Flappy ball"
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
randcolor=(r,g,b)

class Ball:
    def __init__(self,initial_x,initial_y):
        self.x = initial_x
        self.y = initial_y
        self.velocity_x = 200
        self.velocity_y = 0
        self.radius = 40

    def draw(self):
        position = (
            self.x,self.y
        )
        screen.draw.filled_circle(position,self.radius,randcolor)
        