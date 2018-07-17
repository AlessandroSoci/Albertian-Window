from PyQt5.QtWidgets import (QWidget, QComboBox, QAction, qApp, QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QSizePolicy, QGraphicsBlurEffect)
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from video_widget import VideoWidget
from get_camera import Camera
from some_functions import resizeImage, toQImage


class MainWidget(QWidget):

    def __init__(self, camera, main=False):
        super().__init__()
        self.title = "3DMM"
        self.main = main
        # self.setWindowIcon(QtGui.QIcon('images/1UP.ico'))
        self.camera = camera

        if main:
            # self.camera = Camera(1, main, )
            self.showFullScreen()
        else:
            # self.camera = Camera(0)
            self.setGeometry(100, 100, 600, 500)

        self.video_widget = VideoWidget(self.camera)

        self.initUI()

    def initUI(self):

        if self.main:
            self.video_widget.setFixedWidth(1000)
            self.video_widget.move(0, 200)
            self.video_widget.setAlignment(Qt.AlignCenter)
        h = QHBoxLayout()
        h.addWidget(self.video_widget)
        self.setLayout(h)

    def activate(self):
        self.video_widget.activate()
        if not self.main:
            self.show()

    def deactivate(self):
        self.hide()
        self.video_widget.deactivate()

    def closeEvent(self, event):
        self.camera.deactivate()
        self.main_widget.deactivate()
        event.accept()
