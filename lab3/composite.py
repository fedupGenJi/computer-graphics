from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys

original_shape = [
    (10, 20),
    (10, 90),
    (100, 90),
    (100, 20)
]

final_shape = []

def mat_mult(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3))
             for j in range(3)] for i in range(3)]

def apply_matrix(M, pts):
    res = []
    for x, y in pts:
        nx = M[0][0]*x + M[0][1]*y + M[0][2]
        ny = M[1][0]*x + M[1][1]*y + M[1][2]
        res.append((round(nx, 2), round(ny, 2)))
    return res

def translate(tx, ty):
    return [[1,0,tx],[0,1,ty],[0,0,1]]

def rotate(theta):
    r = math.radians(theta)
    return [
        [math.cos(r), -math.sin(r), 0],
        [math.sin(r),  math.cos(r), 0],
        [0, 0, 1]
    ]

def shear(shx, shy):
    return [[1, shx, 0],[shy, 1, 0],[0,0,1]]

def scale(sx, sy):
    return [[sx,0,0],[0,sy,0],[0,0,1]]

def closest_to_origin(pts):
    return min(pts, key=lambda p: p[0]**2 + p[1]**2)

def perform_transformations():
    global final_shape

    theta = 30
    shx, shy = 0.3, 0.2
    sx, sy = 1.5, 1.2

    xc, yc = closest_to_origin(original_shape)
    print("Closest point to origin:", (xc, yc))


    #translation
    M = translate(-xc, -yc)
    print("After translation to origin:", apply_matrix(M, original_shape))

    #rotation
    M = mat_mult(rotate(theta), M)
    print("After rotation:", apply_matrix(M, original_shape))

    #shearing
    M = mat_mult(shear(shx, shy), M)
    print("After shearing:", apply_matrix(M, original_shape))

    #scaling
    M = mat_mult(scale(sx, sy), M)
    print("After scaling:", apply_matrix(M, original_shape))

    #translation
    M = mat_mult(translate(xc, yc), M)
    final_shape = apply_matrix(M, original_shape)

    print("\nFinal transformed coordinates:")
    for p in final_shape:
        print(p)

def draw_shape(pts, color, alpha=1.0):
    glColor4f(color[0], color[1], color[2], alpha)
    glBegin(GL_POLYGON)
    for x, y in pts:
        glVertex2f(x, y)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    draw_shape(original_shape, (0, 0, 1), 1.0)   
    draw_shape(final_shape, (1, 0, 0), 0.4)      

    glFlush()

def init():
    glClearColor(1, 1, 1, 1)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    gluOrtho2D(-200, 300, -200, 300)

def main():
    perform_transformations()

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(700, 700)
    glutCreateWindow(b"Polygon Transformations")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

main()