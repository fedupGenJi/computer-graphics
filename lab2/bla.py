from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

x1, y1, x2, y2 = 0, 0, 0, 0
points = []

def bresenham_line(x1, y1, x2, y2):
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    x = x1
    y = y1

    print("\nPlotted Points (Bresenham):")
    print("(x , y)")
    print("-------")

    if dx >= dy:  # slope <= 1
        p = 2 * dy - dx
        for i in range(dx + 1):
            points.append((x, y))
            print(f"({x}, {y})")
            x += sx
            if p < 0:
                p += 2 * dy
            else:
                y += sy
                p += 2 * dy - 2 * dx
    else:  # slope > 1
        p = 2 * dx - dy
        for i in range(dy + 1):
            points.append((x, y))
            print(f"({x}, {y})")
            y += sy
            if p < 0:
                p += 2 * dx
            else:
                x += sx
                p += 2 * dx - 2 * dy

    return points

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
    global x1, y1, x2, y2, points

    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    points = bresenham_line(x1, y1, x2, y2)

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Bresenham Line Drawing Algorithm")

    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()