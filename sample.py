from visual import *

from Bone import Bone

size = 12
height = 0
width = 10
vertical = 1
horizontal = 20

# Create a instance with your size
osso = Bone()

# Set configs
osso.setSize(size)
osso.setPos(width, height)
osso.rotate(vertical, horizontal)

# And generate
osso.generate()

# To help, create a redpoint of reference
sphere(pos=vector(0, 0, -1),
       radius=1,
       color=color.red)
