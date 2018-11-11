from visual import *


class Bone():
    radius = (10 * 0.1) / 2
    height = 0
    width = 0
    size = 0
    frame = None

    def __init__(self):
        self.frame = frame()

    def center(self):
        cone(frame=self.frame, pos=vector(0, 0, 0),
             axis=vector(10, 0, 0),
             radius=self.radius - (self.radius * 0.2))

        cone(frame=self.frame, pos=vector(10, 0, 0),
             axis=vector(-10, 0, 0),
             radius=self.radius - (self.radius * 0.2))

    def edgeLeft(self):
        sphere(frame=self.frame, pos=vector(0, self.radius * 0.5, 0),
               radius=self.radius + (self.radius * 0.1))

        sphere(frame=self.frame, pos=vector(0 + (self.radius * 0.5), self.radius * -0.2, 0),
               radius=self.radius)

    def edgeRight(self):
        sphere(frame=self.frame, pos=vector(10, self.radius * 0.3, 0),
               radius=self.radius)

        sphere(frame=self.frame, pos=vector(10 + (10 * 0.025), self.radius * -0.4, 0),
               radius=self.radius)

    def generate(self):
        self.center()
        self.edgeLeft()
        self.edgeRight()
        self.updatePosFrame()

    def setPos(self, width, height):
        self.width = width
        self.height = height

    def setSize(self, size):
        self.size = size

    def updatePosFrame(self):
        self.frame.pos = (self.width, self.height, self.size)

    def rotate(self, vertical, horizontal):
        self.frame.axis = vector(1, vertical, horizontal)
