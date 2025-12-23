from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

circle_points = []
xc, yc, r = 0, 0, 0

def plot_symmetric_points(xc, yc, x, y, points):
    """Calculate 8 symmetric points and shift by circle center"""
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
    x = 0
    y = r
    P = round(5/4 - r)
    k = 0

    print(f"{'k':<5}{'Pk':<10}{'(xk, yk)':<12}{'(xk+1, yk+1)':<15}")
    print("-" * 45)

    plot_symmetric_points(xc, yc, x, y, points)

    while x <= y:
        x_next = x + 1
        if P < 0:
            y_next = y
            P_next = round(P + 2 * x_next + 1)
        else:
            y_next = y - 1
            P_next = round(P + 2 * x_next + 1 - 2 * y_next)

        print(f"{k:<5}{P:<10}{(x, y)!s:<12}{(x_next, y_next)!s:<15}")

        x = x_next
        y = y_next
        P = P_next
        k += 1

        plot_symmetric_points(xc, yc, x, y, points)

    return points

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(3)
    glBegin(GL_POINTS)
    for px, py in circle_points:
        glVertex2i(px, py)
    glEnd()
    glFlush()

def get_int_input(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid integer.")

def main():
    global xc, yc, r, circle_points

    r = get_int_input("Enter radius of circle: ")
    xc = get_int_input("Enter x-coordinate of center: ")
    yc = get_int_input("Enter y-coordinate of center: ")

    circle_points = midpoint_circle(xc, yc, r)

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Midpoint Circle Algorithm - Rounded Pk")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3f(1.0, 1.0, 1.0)
    gluOrtho2D(-250, 250, -250, 250)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()