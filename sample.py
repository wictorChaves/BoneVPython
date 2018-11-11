from visual import *

from Bone import Bone

size = 12

length = 0
height = 0
width = 0

#Create a instance with your size
osso = Bone(size)

#Define your vector with length, height and width
osso.setVector(1, height, width)

#And generate
osso.generate()

#To help, create a redpoint of reference
sphere(pos=vector(0, 0, -1),
       radius=1,
       color=color.red)