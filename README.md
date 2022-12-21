# calibration
The process of estimating the parameters of a camera is called camera calibration.

This means we have all the information (parameters or coefficients) about the camera required to determine an accurate relationship between a 3D point in the real world and its corresponding 2D projection (pixel) in the image captured by that calibrated camera.

Typically this means recovering two kinds of parameters

1. Internal parameters of the camera/lens system. E.g. focal length, optical center, and radial distortion coefficients of the lens.
2. External parameters : This refers to the orientation (rotation and translation) of the camera with respect to some world coordinate system.


Step 1: Define real world coordinates with checkerboard pattern
Step 2 : Capture multiple images of the checkerboard from different viewpoints
Step 3 : Find 2D coordinates of checkerboard
  3.1 Find checkerboard corners
  3.2 Refine checkerboard corners
Step 4: Calibrate Camera


##Python Code for Camera Calibration is given in calibration.py file
