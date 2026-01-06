from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

from shapes import shapes, apply_transform
from utils import draw_shape

sx = float(input("Enter scaling factor in X direction: "))
sy = float(input("Enter scaling factor in Y direction: "))

S = np.array([
    [sx, 0, 0],
    [0, sy, 0],
    [0, 0, 1]
])

scaled_shapes = {}

print("\nScaled Coordinates (About Origin):")
for name, shape in shapes.items():
    scaled_shapes[name] = apply_transform(shape, S)
    print(f"\n{name}:")
    print(scaled_shapes[name])

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    for name in shapes:
        draw_shape(shapes[name], (0, 1, 0))         
        draw_shape(scaled_shapes[name], (1, 0, 0))

    glFlush()

def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(0, 500, 0, 500)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"2D Scaling")
init()
glutDisplayFunc(display)
glutMainLoop()