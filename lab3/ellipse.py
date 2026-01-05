from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

ellipse_points = []

xc = int(input("Enter center x (xc): "))
yc = int(input("Enter center y (yc): "))
rx = int(input("Enter x-radius (rx): "))
ry = int(input("Enter y-radius (ry): "))


def plot_symmetric_points(x, y):
    ellipse_points.extend([
        ( x + xc,  y + yc),
        (-x + xc,  y + yc),
        ( x + xc, -y + yc),
        (-x + xc, -y + yc)
    ])


def midpoint_ellipse():
    global ellipse_points
    ellipse_points = []

    rx2 = rx * rx
    ry2 = ry * ry

    x = 0
    y = ry

    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)

    dx = 2 * ry2 * x
    dy = 2 * rx2 * y

    while dx < dy:
        plot_symmetric_points(x, y)

        if p1 < 0:
            x += 1
            dx += 2 * ry2
            p1 += dx + ry2
        else:
            x += 1
            y -= 1
            dx += 2 * ry2
            dy -= 2 * rx2
            p1 += dx - dy + ry2

    p2 = (ry2 * (x + 0.5) ** 2) + (rx2 * (y - 1) ** 2) - (rx2 * ry2)

    while y >= 0:
        plot_symmetric_points(x, y)

        if p2 <= 0:
            x += 1
            y -= 1
            dx += 2 * ry2
            dy -= 2 * rx2
            p2 += dx - dy + rx2
        else:
            y -= 1
            dy -= 2 * rx2
            p2 += rx2 - dy


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)
    glPointSize(2)

    glBegin(GL_POINTS)
    for x, y in ellipse_points:
        glVertex2i(int(x), int(y))
    glEnd()

    glFlush()


def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-500, 500, -500, 500)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Midpoint Ellipse Algorithm - User Input")

    init()
    midpoint_ellipse()
    glutDisplayFunc(display)
    glutMainLoop()

main()