from visual import *

length = 0
height = 0
width = 0

size = 18
radius = (size * 0.1)/2


sphere(pos=vector(0, 0, 10),
       radius=1,
       color=color.red)

#Center
cone(pos=vector(length + 0, height, width),
     axis=vector(size, 0, 0),
     radius=radius - (radius*0.2))

cone(pos=vector(length + size, height, width),
     axis=vector(-size, 0, 0),
     radius=radius - (radius*0.2))

#Balls
sphere(pos=vector(length + size, height + 0.1, width),
       radius=radius)

sphere(pos=vector(length + size + 0.5, height + -0.4, width),
       radius=radius)

sphere(pos=vector(length + 2, height + 0.1, width),
       radius=radius)

sphere(pos=vector(length + 1.2, height + -0.4, width),
       radius=radius)
