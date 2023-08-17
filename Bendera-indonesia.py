import numpy as np
import matplotlib.pyplot as py
import matplotlib.patches as patch

#Plot warna bendera indonesia
a = patch.Rectangle((0,1), width=6, height=2, facecolor='#FFFFFF', edgecolor='grey')
b = patch.Rectangle((0,3), width=6, height=2, facecolor='#FF0000', edgecolor='grey')
m,n = py.subplots()
n.add_patch(a)
n.add_patch(b)

py.axis('equal')
py.show()
