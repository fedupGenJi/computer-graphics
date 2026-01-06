import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from shapes import shapes, apply_transform
from utils import draw_shape

angle = float(input("Enter rotation angle (degrees): "))
rad = np.radians(angle)

R = np.array([
    [np.cos(rad), -np.sin(rad), 0],
    [np.sin(rad),  np.cos(rad), 0],
    [0, 0, 1]
])

rotated_shapes = {}

print("\nRotated Coordinates:")
for name, shape in shapes.items():
    rotated_shapes[name] = apply_transform(shape, R)
    print(f"\n{name}:")
    print(rotated_shapes[name])

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    for name in shapes:
        draw_shape(shapes[name], (0, 1, 0))           
        draw_shape(rotated_shapes[name], (1, 0, 0))   

    glFlush()

def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-300, 300, -300, 300)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"2D Rotation")
init()
glutDisplayFunc(display)
glutMainLoop()