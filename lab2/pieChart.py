from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

xc, yc, r = 0, 0, 200
slices = 0  
circle_points = []
line_points = []

def plot_symmetric_points(xc, yc, x, y, points):
    octant_points = [
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x)
    ]
    points.extend(octant_points)

def midpoint_circle(xc, yc, r):
    points = []
    x, y = 0, r
    P = 1 - r

    plot_symmetric_points(xc, yc, x, y, points)

    while x < y:
        x += 1
        if P < 0:
            P = P + 2 * x + 1
        else:
            y -= 1
            P = P + 2 * x + 1 - 2 * y
        plot_symmetric_points(xc, yc, x, y, points)

    return points

def draw_pie_lines(xc, yc, r, slices):
    points = []
    angle_step = 360 / slices
    for i in range(slices):
        theta = math.radians(i * angle_step)
        x_end = xc + int(r * math.cos(theta))
        y_end = yc + int(r * math.sin(theta))
        points.append((xc, yc, x_end, y_end))
    return points

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)
    glPointSize(2)

    glBegin(GL_POINTS)
    for x, y in circle_points:
        glVertex2i(x, y)
    glEnd()

    glLineWidth(2)
    glBegin(GL_LINES)
    for x0, y0, x1, y1 in line_points:
        glVertex2i(x0, y0)
        glVertex2i(x1, y1)
    glEnd()

    glFlush()

def main():
    global circle_points, line_points, slices

    slices = int(input("Enter number of slices: "))
    circle_points = midpoint_circle(xc, yc, r)
    line_points = draw_pie_lines(xc, yc, r, slices)

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Pie Chart - OpenGL")
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-300, 300, -300, 300)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()