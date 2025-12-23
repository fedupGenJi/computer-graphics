from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

x1, y1, x2, y2 = 0, 0, 0, 0
points = []

def dda_algorithm():
    global points
    points = []

    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) >= abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    xinc = dx / steps
    yinc = dy / steps

    x = x1
    y = y1

    print("\nPlotted Points (DDA):")
    print("(x , y)")
    print("-------")

    for i in range(int(steps) + 1):
        px = math.floor(x+0.5)
        py = math.floor(y+0.5)
        points.append((px, py))
        print(f"({px}, {py})")

        x += xinc
        y += yinc


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0) 
    glPointSize(4)

    glBegin(GL_POINTS)
    for (x, y) in points:
        glVertex2i(x, y)
    glEnd()

    glFlush()


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-500, 500, -500, 500)


def main():
    global x1, y1, x2, y2

    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    dda_algorithm()

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"DDA Line Drawing Algorithm")

    init()
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()