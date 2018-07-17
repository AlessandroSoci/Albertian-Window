from OpenGL.GL import *

ground_surfaces = (0, 1, 2, 3)

ground_vertices = (
    (-10, -0.1, 50),
    (10, -0.1, 50),
    (-10, -0.1, -300),
    (10, -0.1, -300),

)

def Ground():
    glBegin(GL_QUADS)

    x = 0
    for vertex in ground_vertices:
        x += 1
        glColor3fv((15, 2, 1))
        glVertex3fv(vertex)

    glEnd()