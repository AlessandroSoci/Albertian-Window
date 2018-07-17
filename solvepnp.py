import numpy as np
import cv2
import glob
import dlib
from imutils import face_utils
import pickle
import os.path


def compute_rot_tran(image_points, src, test=False):
	# Getting back the calibration matrix:
	if src == 0:
		with open('K_matrix.pkl', 'rb') as f:
			unpickler = pickle.Unpickler(f)
			K_matrix = unpickler.load()
		open('K_matrix.pkl', 'a').close()
	elif src == 1:
		with open('K_matrix_camera2.pkl', 'rb') as f:
			unpickler = pickle.Unpickler(f)
			K_matrix = unpickler.load()
		open('K_matrix_camera2.pkl', 'a').close()

	# 3D model points.
	model_points = np.array([
							(0.0, 0.0, 0),               # Nose tip
							(0.0, -330.0, -65.0),        # Chin
							(-225.0, 170.0, -135.0),     # Left eye left corner
							(225.0, 170.0, -135.0),      # Right eye right corner
							(-150.0, -150.0, -125.0),    # Left Mouth corner
							(150.0, -150.0, -125.0)     # Right mouth corner
                        ])

	# print(model_points.shape)
	# print(image_points.shape)

	dist_coeffs = np.zeros((4,1)) # Assuming no lens distortion
	(success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, image_points, K_matrix, dist_coeffs)

	# if not test:
	# 	print ("Rotation Vector:\n {0}".format(rotation_vector))
	# 	print ("Translation Vector:\n {0}".format(translation_vector))
	# elif test:
	# 	print("Rotation Vector_test:\n {0}".format(rotation_vector))
	# 	print("Translation Vector_test:\n {0}".format(translation_vector))

	(nose_end_point2D, jacobian) = cv2.projectPoints(np.array([(0.0, 0.0, 1000.0)]), rotation_vector,
													 translation_vector, K_matrix, dist_coeffs)

	estimate_points, jacobian = cv2.projectPoints(model_points, rotation_vector, translation_vector, K_matrix, dist_coeffs)
	return nose_end_point2D, rotation_vector, translation_vector, estimate_points
