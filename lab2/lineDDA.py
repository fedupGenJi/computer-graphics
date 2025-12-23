from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
import random

lines = []
points = []

def dda_algorithm(x1, y1, x2, y2, color):
    global points

    dx = x2 - x1
    dy = y2 - y1

    steps = abs(dx) if abs(dx) >= abs(dy) else abs(dy)

    xinc = dx / steps
    yinc = dy / steps

    x = x1
    y = y1

    for i in range(int(steps) + 1):
        px = math.floor(x + 0.5)
        py = math.floor(y + 0.5)
        points.append(((px, py), color))

        x += xinc
        y += yinc

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(4)

    glBegin(GL_POINTS)
    for (x, y), (r, g, b) in points:
        glColor3f(r, g, b)
        glVertex2i(x, y)
    glEnd()

    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-500, 500, -500, 500)

def main():
    global lines, points

    n = int(input("Enter number of lines: "))

    print("\nLine 1")
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    r = random.random()
    g = random.random()
    b = random.random()
    lines.append((x1, y1, x2, y2, (r, g, b)))

    for i in range(1, n):
        print(f"\nLine {i + 1}")
        x1, y1 = lines[i-1][2], lines[i-1][3]
        print(f"Start point automatically: ({x1}, {y1})")
        x2 = int(input("Enter x2: "))
        y2 = int(input("Enter y2: "))

        r = random.random()
        g = random.random()
        b = random.random()
        lines.append((x1, y1, x2, y2, (r, g, b)))

    for line in lines:
        dda_algorithm(line[0], line[1], line[2], line[3], line[4])

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"DDA Consecutive Lines with Colors")

    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()