from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

from shapes import shapes, apply_transform
from utils import draw_shape

tx = float(input("Enter translation in X direction: "))
ty = float(input("Enter translation in Y direction: "))

T = np.array([
    [1, 0, tx],
    [0, 1, ty],
    [0, 0, 1]
])

translated_shapes = {}

print("\nTranslated Coordinates:")
for name, shape in shapes.items():
    translated_shapes[name] = apply_transform(shape, T)
    print(f"\n{name}:")
    print(translated_shapes[name])

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    for name in shapes:
        draw_shape(shapes[name], (0, 1, 0))              
        draw_shape(translated_shapes[name], (1, 0, 0))  

    glFlush()

def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(0, 500, 0, 500)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"2D Translation")
init()
glutDisplayFunc(display)
glutMainLoop()