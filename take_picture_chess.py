# import the necessary packages
from imutils.video import VideoStream
from imutils import face_utils
import datetime
import argparse
import imutils
import time
import dlib
import cv2

print("[INFO] camera sensor warming up...")
vs = cv2.VideoCapture(1)
time.sleep(2.0)
count = 1

while True:
	# grab the frame from the threaded video stream, resize it to
	# have a maximum width of 400 pixels, and convert it to
	# grayscale
	cap, frame = vs.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	ret, corners = cv2.findChessboardCorners(gray, (9,6),None)
	if ret:
		print(count)
		cv2.imwrite("photo_to_calibration_camera2/frame%d.jpg" % count, frame)
		time.sleep(2.0)
		count = count + 1
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()
