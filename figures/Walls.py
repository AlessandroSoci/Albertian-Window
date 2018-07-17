from OpenGL.GL import *

left_wall_vertices = (
    (-5, -0.1, 50),
    (-5, -0.1, -100),
    (-5, 40, 50),
    (-5, 40, -100)
)

behind_wall_vertices = (
    (-5, -0.1, -30),
    (5, -0.1, -30),
    (5, 40, -30),
    (-5, 40, -30)
)

right_wall_vertices = (
    (5, -0.1, 50),
    (5, -0.1, -100),
    (5, 40, 50),
    (5, 40, -100)
)


def Left_Wall():
    glBegin(GL_QUADS)

    for vertex in left_wall_vertices:
        glColor3fv((1, 0, 0))
        glVertex3fv(vertex)

    glEnd()

def Behind_Wall():
    glBegin(GL_QUADS)

    for vertex in behind_wall_vertices:
        glColor3fv((60, 0, 0))
        glVertex3fv(vertex)

    glEnd()


def Right_Wall():
    glBegin(GL_QUADS)

    for vertex in right_wall_vertices:
        glColor3fv((1, 0, 0))
        glVertex3fv(vertex)

    glEnd()