# Albertian Window

Simulation of a real window

## Run
- download the [repository](https://github.com/AlessandroSoci/Albertian-Window.git) (clone or zip download)
- download landmarks predictor from [TensorFace](https://github.com/AKSHAYUBHAT/TensorFace/blob/master/openface/models/dlib/shape_predictor_68_face_landmarks.dat)
- add it on the main folder
- calibrate the camera:
  - run `take_picture_chess.py` and use a 10x7 chess in various position (at least 20 photos)
  - run `calibration.py`
- run `main.py`

## Introduction
The concept of the Albertian window born in the fifth century, as a new method to paint real scene. The Albertian window is a 2D image that recreates a 3D scene exactly from the observer's point of view.
In the past, the problem was that you could paint a scene from only one point of view, because of the static of the painting. Nowadays, using a camera (calibrated camera) and given a 3D scene, it's possible to generate an interactive Albertian window with many points of view.

## Goals
1. Find face landmarks of the observer
2. Compute the rotation, translation, and distance of the observer respect the screen
3. Move the point of view of 3D scene respect the observer

## Technologies
- OpenCV allows having control of the camera
- The camera interface is developed with PyQt Framework
- The face landmarks are calculated thanks to Dlib packages
- OpenGL to create a 3D scene
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

