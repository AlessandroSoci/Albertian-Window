from OpenGL.GL import *

vertices_cube1 = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

vertices_cube2 = (
    (-2, -1, -4),
    (-2, 1, -4),
    (-4, 1, -4),
    (-4, -1, -4),
    (-2, -1, -2),
    (-2, 1, -2),
    (-4, -1, -2),
    (-4, 1, -2)
    )

vertices_cube3 = (
    (3, -1, -21),
    (3, 1, -21),
    (1, 1, -21),
    (1, -1, -21),
    (3, -1, -19),
    (3, 1, -19),
    (1, -1, -19),
    (1, 1, -19)
    )

vertices_cube4 = (
    (1.7, -1, -7),
    (1.7, 1, -7),
    (-0.3, 1, -7),
    (-0.3, -1, -7),
    (1.7, -1, -5),
    (1.7, 1, -5),
    (-0.3, -1, -5),
    (-0.3, 1, -5)
    )

edges_cube = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
    )

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
    )


colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
    )


def Cube1():
    glBegin(GL_QUADS)

    for surface in surfaces:
        x = 0

        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices_cube1[vertex])

    glEnd()

    glBegin(GL_LINES)
    for edge in edges_cube:
        for vertex in edge:
            glVertex3fv(vertices_cube1[vertex])
    glEnd()

def Cube2():
    glBegin(GL_QUADS)

    for surface in surfaces:
        x = 0

        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices_cube2[vertex])

    glEnd()

    glBegin(GL_LINES)
    for edge in edges_cube:
        for vertex in edge:
            glVertex3fv(vertices_cube2[vertex])
    glEnd()

def Cube3():
    glBegin(GL_QUADS)

    for surface in surfaces:
        x = 0

        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices_cube3[vertex])

    glEnd()

    glBegin(GL_LINES)
    for edge in edges_cube:
        for vertex in edge:
            glVertex3fv(vertices_cube3[vertex])
    glEnd()


def Cube4():
    glBegin(GL_QUADS)

    for surface in surfaces:
        x = 0

        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices_cube4[vertex])

    glEnd()

    glBegin(GL_LINES)
    for edge in edges_cube:
        for vertex in edge:
            glVertex3fv(vertices_cube4[vertex])
    glEnd()
