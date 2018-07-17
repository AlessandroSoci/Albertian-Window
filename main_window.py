from PyQt5.QtWidgets import (QWidget, QComboBox, QAction, qApp, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel,
                             QSizePolicy, QSlider, QProgressBar)
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from get_camera import Camera
from video_widget import VideoWidget
from some_functions import toQImage, resizeImage
from main_widget import MainWidget


class MainWindow(QMainWindow):

    def __init__(self, camera):
        super().__init__()

        self.title = "3DMM"
        # self.setWindowIcon(QtGui.QIcon('images/1UP.ico'))
        # self.setFixedSize(1200, 700)
        # self.setGeometry(500, 100, 1200, 700)

        # self.right_label = RightLabel(self, self.model)
        self.camera = camera
        self.main_widget = MainWidget(self.camera, True)

        # self.initUI()

    def initUI(self):
        count = 0
        # self.addToolBarBreak()

    def activate(self):
        self.main_widget.activate()

    def deactivate(self):
        self.main_widget.deactivate()

    def closeEvent(self, event):
        self.camera.deactivate()
        self.main_widget.deactivate()
        event.accept()
