from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

from shapes import shapes, apply_transform
from utils import draw_shape

shx = float(input("Enter shear factor in X direction: "))
shy = float(input("Enter shear factor in Y direction: "))

Sh = np.array([
    [1, shx, 0],
    [shy, 1, 0],
    [0, 0, 1]
])

sheared_shapes = {}

print("\nSheared Coordinates (About Origin):")
for name, shape in shapes.items():
    sheared_shapes[name] = apply_transform(shape, Sh)
    print(f"\n{name}:")
    print(sheared_shapes[name])

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    for name in shapes:
        draw_shape(shapes[name], (0, 1, 0))          
        draw_shape(sheared_shapes[name], (1, 0, 0))

    glFlush()

def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(0, 500, 0, 500)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"2D Shearing")
init()
glutDisplayFunc(display)
glutMainLoop()