# Albertian Window

To simulate a real window on the screen

## Run
- download the [repository](https://github.com/AlessandroSoci/Albertian-Window.git) (clone or zip download)
- download landmarks predictor from [TensorFace](https://github.com/AKSHAYUBHAT/TensorFace/blob/master/openface/models/dlib/shape_predictor_68_face_landmarks.dat)
- add it on the main folder
- calibrate the camera:
  - run `take_picture_chess.py` and use a 10x7 chess in various position (at least 20 photo)
  - run `calibration.py`
- run `main.py`

## Introduction
The concept of Albertian window born in fifth century, it consists to simulate real scene on a wall, on a painting or on a screen so as to deceive the people. Albertian window is a 2D image that recreates a 3D scene exactly among the point of view of the observer.
In past the problem was that you could paint scene among only one point of view.
Using a camera (calibrated camera) and given a 3D scene, it's possible generate an interactive Albertian window, with many points of view.

## Goals
1. Find face landmarks of the observer
2. Compute the rotation, traslation and distance of the observer respect the screen
3. Move the point of view of 3D scene respect the observer

## Technologies
- OpenCV allow to have control on camera
- Camera interface is developed with PyQt Framework
- The face landmark are calculated thanks to Dlib packages
- OpenGl to create 3D scene
- Pygame to render and control the 3D scene

## Description



###


## Requirements

| Software                                                    | Version         | Required |
| ------------------------------------------------------------|:---------------:| --------:|
| **Python**                                                  |     >= 3        |    Yes   |
| **Numpy** (Python Package)                                  |Tested on v1.13  |    Yes   |
| **opencv-python** (Python Package)                          |Tested on v3     |    Yes   |
| **PyQt5** (Python Package)                                  |Tested on v5.11  |    Yes   |
| **QDarkStyle** (Python Package)                             |Tested on v2.5.1 |    Yes   |
| **dlib** (Python Package)                                   |Tested on v19.8.1|    Yes   |
| **imutils** (Python Package)                                |Tested on v0.4.4 |    Yes   |
| **pygame** (Python Package)                                 |Tested on v1.9.3 |    Yes   |

