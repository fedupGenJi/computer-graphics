from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

H = 200     
W = 80      
T = 20      
BASE = 100  


def rect(x1, y1, x2, y2):
    glBegin(GL_POLYGON)
    glVertex2i(x1, y1)
    glVertex2i(x2, y1)
    glVertex2i(x2, y2)
    glVertex2i(x1, y2)
    glEnd()

def thick_diag(x1, y1, x2, y2, t):
    dx = y2 - y1
    dy = x1 - x2
    length = (dx*dx + dy*dy) ** 0.59
    dx = dx / length * t
    dy = dy / length * t

    glBegin(GL_POLYGON)
    glVertex2f(x1 + dx, y1 + dy)
    glVertex2f(x1 - dx, y1 - dy)
    glVertex2f(x2 - dx, y2 - dy)
    glVertex2f(x2 + dx, y2 + dy)
    glEnd()



def drawA(x):
    thick_diag(x + 10, BASE, x + W//2, BASE + H, T)

    thick_diag(x + W - 10, BASE, x + W//2, BASE + H, T)

    glBegin(GL_POLYGON)
    glVertex2i(x + 25, BASE + H//2)
    glVertex2i(x + 55, BASE + H//2)
    glVertex2i(x + 55, BASE + H//2 + 15)
    glVertex2i(x + 25, BASE + H//2 + 15)
    glEnd()



def drawK(x):
    glBegin(GL_POLYGON)
    glVertex2i(x, BASE)
    glVertex2i(x + 20, BASE)
    glVertex2i(x + 20, BASE + H)
    glVertex2i(x, BASE + H)
    glEnd()

    thick_diag(x + 20, BASE + H // 2, x + W, BASE + H, T)

    thick_diag(x + 20, BASE + H // 2, x + W, BASE , T)



def drawS(x):
    rect(x, BASE + H - T, x + W, BASE + H)

    rect(x, BASE + H // 2 - T // 2, x + W, BASE + H // 2 + T // 2)

    rect(x, BASE, x + W, BASE + T)

    rect(x, BASE + H // 2, x + T, BASE + H)

    rect(x + W - T, BASE, x + W, BASE + H // 2)


def drawH(x):
    rect(x, BASE, x + T, BASE + H)

    rect(x + W - T, BASE, x + W, BASE + H)

    rect(x + T, BASE + H // 2 - T // 2,
         x + W - T, BASE + H // 2 + T // 2)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.1, 0.6, 0.2)

    drawA(50)
    drawA(150)
    drawK(250)
    drawA(370)
    drawS(490)
    drawH(610)

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(900, 500)
    glutCreateWindow(b"AAKASH - Symmetric PyOpenGL")

    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 900, 0, 500)

    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()