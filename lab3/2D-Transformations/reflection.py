from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

from shapes import shapes, apply_transform
from utils import draw_shape

print("Choose axis of reflection:")
print("1: X-axis")
print("2: Y-axis")
print("3: Origin (both axes)")
choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    R = np.array([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 1]
    ])
elif choice == 2:
    R = np.array([
        [-1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])
elif choice == 3:
    R = np.array([
        [-1, 0, 0],
        [0, -1, 0],
        [0, 0, 1]
    ])
else:
    print("Invalid choice! Defaulting to X-axis.")
    R = np.array([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 1]
    ])

reflected_shapes = {}

print("\nReflected Coordinates:")
for name, shape in shapes.items():
    reflected_shapes[name] = apply_transform(shape, R)
    print(f"\n{name}:")
    print(reflected_shapes[name])

def draw_axes():
    """Draw X and Y axes."""
    glColor3f(0.5, 0.5, 0.5)  
    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2f(-500, 0)
    glVertex2f(500, 0)
    glVertex2f(0, -500)
    glVertex2f(0, 500)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    draw_axes()  

    for name in shapes:
        draw_shape(shapes[name], (0, 1, 0))           
        draw_shape(reflected_shapes[name], (1, 0, 0)) 

    glFlush()

def init():
    glClearColor(1, 1, 1, 1)
    gluOrtho2D(-500, 500, -500, 500)

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 800)
glutCreateWindow(b"2D Reflection")
init()
glutDisplayFunc(display)
glutMainLoop()