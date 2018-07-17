from PyQt5.QtCore import pyqtSignal, QThread
from imutils.video import VideoStream
from imutils import face_utils
from solvepnp import compute_rot_tran
import numpy as np
import dlib
import cv2
import sys


class Camera(QThread):

    updated = pyqtSignal()  # in order to work it has to be defined out of the constructor

    def __init__(self, src, main=False, another_camera=None):
        super().__init__()

        self.currentFrame = None
        self.active = False
        if main:
            self.another_camera = another_camera
        self.rotation = None
        self.translation = None
        self.estimate = None
        self.prev_shape = []
        self.points = 0
        self.src = src
        self.main = main
        self.nose = None
        self.offset_x = 0
        self.offset_y = 0
        self.z = 0

    def get_current_frame(self):
        """Getter for the currentFrame attribute"""
        return self.currentFrame

    def get_nose(self):
        return self.nose

    def get_rotation(self):
        return self.rotation

    def get_scale(self):
        return self.translation

    def deactivate(self):
        """Method called to stop and deactivate the get camera Thread"""
        self.active = False
        if self.isRunning():
            self.terminate()
            sys.exit('Error')

    def loop(self):
        """Method called to initialize and start the face recognition Thread"""
        self.start()

    def run(self):
        """Main loop of this Thread"""
        self.active = True
        bounding_box = None
        box = True

        if not self.main:
            vs = VideoStream(src=self.src).start()
            print("[INFO] loading facial landmark predictor...")
            detector = dlib.get_frontal_face_detector()
            predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

        while self.active:

            # Scene camera
            if self.main:
                count = 0

            # Frontal Camera
            else:

                # Grab a single frame of video
                frame = vs.read()
                # frame = imutils.resize(frame, width=500)
                frame = cv2.flip(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), 1)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.equalizeHist(gray)

                # detect faces in the grayscale frame
                rect = detector(gray, 0)
                if len(rect) == 1:
                    # (x, y, w, h) = face_utils.rect_to_bb(rect[0])

                    # bounding_box = gray[int(y - 20):int(y + h + 20), int(x - 10):int(x + w + 10)]
                    # bounding_box = imutils.resize(bounding_box, width=500)
                    # rect_bounding_box = detector(bounding_box, 0)
                    # if len(rect_bounding_box) == 1:
                    #     shape_box = predictor(gray, rect[0])
                    #     shape_box = face_utils.shape_to_np(shape_box)
                    #     shape_box = shape_box[np.array([30, 8, 36, 45, 48, 54])]
                    #     image_points = np.array([
                    #         shape_box[0],  # Nose
                    #         shape_box[1],  # Chin
                    #         shape_box[2],  # Left Eye
                    #         shape_box[3],  # Right Eye
                    #         shape_box[4],  # Left-part mouth
                    #         shape_box[5]   # Right-part mouth
                    #     ], dtype="double")
                    #     nose_point_2D, self.rotation, self.translation, self.estimate = compute_rot_tran(image_points, self.src, True)


                    shape = predictor(gray, rect[0])
                    shape = face_utils.shape_to_np(shape)
                    shape = shape[np.array([30, 8, 36, 45, 48, 54, 1, 2, 15, 14, 27])]

                    self.prev_shape.append(shape)

                    if len(self.prev_shape) >= 2:
                        if (abs(self.prev_shape[-1][0][0] - self.prev_shape[-2][0][0]) >= 1) or \
                                (abs(self.prev_shape[-1][0][1] - self.prev_shape[-2][0][1]) >= 1):
                            length = len(self.prev_shape)
                            a = range(length+1)
                            max_sum = sum(a)
                            for i in range(0, length):
                                self.points = self.points + (self.prev_shape[i] * (i+1)/max_sum)
                            self.points = self.points  # / len(self.prev_shape)

                            image_points = np.array([
                                self.points[0],     # Nose
                                self.points[1],     # Chin
                                self.points[2],     # Left Eye
                                self.points[3],     # Right Eye
                                self.points[4],     # Left-part mouth
                                self.points[5]      # Right-part mouth
                            ], dtype="double")
                            nose_point_2D, self.rotation, self.translation, self.estimate = compute_rot_tran(image_points, self.src)
                            self.nose = shape[-1]

                        else:
                            self.points = self.prev_shape[-1]
                            image_points = np.array([
                                self.points[0],  # Nose
                                self.points[1],  # Chin
                                self.points[2],  # Left Eye
                                self.points[3],  # Right Eye
                                self.points[4],  # Left-part mouth
                                self.points[5]  # Right-part mouth
                            ], dtype="double")
                            nose_point_2D, self.rotation, self.translation, self.estimate = compute_rot_tran(
                                image_points, self.src)
                    else:
                        self.points = self.prev_shape[0]
                        image_points = np.array([
                            self.points[0],  # Nose
                            self.points[1],  # Chin
                            self.points[2],  # Left Eye
                            self.points[3],  # Right Eye
                            self.points[4],  # Left-part mouth
                            self.points[5]   # Right-part mouth
                        ], dtype="double")
                        nose_point_2D, self.rotation, self.translation, self.estimate = compute_rot_tran(image_points,
                                                                                                   self.src)
                        self.nose = shape[-1]

                    # cv2.rectangle(frame, (int(x), int(y)), (int(x + w), int(y + h)), (0, 255, 255), 2)

                    # is for the error
                    if self.estimate is not None:
                        for i in range(0, self.estimate.shape[0]):
                            for(x, y) in self.estimate[i]:
                                cv2.circle(frame, (int(x), int(y)), 1, (0, 255, 0), -1)

                    for (x, y) in image_points:
                        cv2.circle(frame, (int(x), int(y)), 1, (0, 0, 255), -1)
                    if len(self.prev_shape) >= 10:
                        self.prev_shape.pop(0)
                    self.points = 0

                    p1 = (int(image_points[0][0]), int(image_points[0][1]))
                    p2 = (int(nose_point_2D[0][0][0]), int(nose_point_2D[0][0][1]))

                    cv2.line(frame, p1, p2, (255, 0, 0), 2)

                self.currentFrame = frame

            self.updated.emit()

        vs.stop()
