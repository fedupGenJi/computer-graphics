from OpenGL.GL import *

def draw_shape(shape, color):
    glColor3f(*color)
    glBegin(GL_LINE_LOOP)
    for x, y, _ in shape:
        glVertex2f(x, y)
    glEnd()