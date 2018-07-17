from PyQt5.QtWidgets import QApplication
from main_widget import MainWidget
from get_camera import Camera
from figures.Cube import *
from figures.Walls import *
from figures.Ground import *

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np
import sys
import qdarkstyle

if __name__ == '__main__':
    x = 0
    y = 0
    x1 = 0
    y1 = 0
    z = 0
    z1 = 0
    list_z = []
    nose_tmp = np.array([0, 0])
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    frontal_camera = Camera(0)
    mainWid = MainWidget(frontal_camera)
    mainWid.activate()
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glLightfv(GL_LIGHT0, GL_POSITION, (-40, 200, 100, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glTranslate(0, -2, -5)
    glRotatef(1, 70, 70, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                mainWid.deactivate()
                sys.exit(app.exec_())
                quit()

        # glRotatef(1, 3, 1, 1)

        nose = frontal_camera.get_nose()
        scale = frontal_camera.get_scale()
        frame_shape = frontal_camera.get_current_frame()
        if nose is not None and (nose[0] != nose_tmp[0] or nose[1] != nose_tmp[1]):
            z1 = z
            z = scale[2]
            if abs(z) < 2000:
                z = 2000
            elif abs(z) > 8500:
                z = 8500
            z = z - 2500
            z = z / 1000
            list_z.append(z)
            height = frame_shape.shape[0]
            width = frame_shape.shape[1]
            nose[0] = nose[0] - height
            nose[1] = nose[1] - width
            x1 = x
            y1 = y
            y = nose[0]/100 + 1
            x = nose[1]/100 + 3
            if len(list_z) >= 5:
                a = sum(list_z)
                mean = a/len(list_z)
                if z < mean - 1 or z > mean + 1:
                    z = z1
            glTranslatef(y1, -x1, z1)
            glTranslatef(-y, x, -z)
            nose_tmp = nose
            if len(list_z) >= 10:
                list_z.pop(0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube1()
        Cube2()
        Cube3()
        Cube4()
        Ground()
        Left_Wall()
        Behind_Wall()
        Right_Wall()
        pygame.display.flip()
        pygame.time.wait(100)
