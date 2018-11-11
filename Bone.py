from visual import *


class Bone():
    size = 0
    radius = 0
    length = 0
    height = 0
    width = 0

    def __init__(self, size):
        self.size = size
        self.calcRadius(size)

    def calcRadius(self, size):
        self.radius = (size * 0.1) / 2

    def setVector(self, length, height, width):
        self.length = length
        self.height = height
        self.width = width

    def center(self):
        cone(pos=vector(self.length + 0, self.height, self.width),
             axis=vector(self.size, 0, 0),
             radius=self.radius - (self.radius * 0.2))

        cone(pos=vector(self.length + self.size, self.height, self.width),
             axis=vector(-self.size, 0, 0),
             radius=self.radius - (self.radius * 0.2))

    def edgeLeft(self):
        size = self.length
        sphere(pos=vector(size, self.radius * 0.5, self.width),
               radius=self.radius + (self.radius * 0.1))

        sphere(pos=vector(size + (self.radius * 0.5),  self.radius * -0.2, self.width),
               radius=self.radius)

    def edgeRight(self):
        size = (self.length + self.size)
        sphere(pos=vector(size, self.radius * 0.3, self.width),
               radius=self.radius)

        sphere(pos=vector(size + (size * 0.025), self.radius * -0.4, self.width),
               radius=self.radius)

    def generate(self):
        self.center()
        self.edgeLeft()
        self.edgeRight()
