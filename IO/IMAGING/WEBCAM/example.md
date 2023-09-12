---
title: CAMERA
description: In this example, the CAMERA node takes and returns a picture if a USB camera is connected to the computer. The IMSHOW node then displays the image taken by the camera, and the END node terminates the process.
keyword: [Python, Instrument, Web cam, Camera, Python webcam integration, Camera instrument in Python, Capture images and videos, Streamline webcam usage, Python-based camera control, Webcam integration techniques, Python image and video capture, Enhance projects with webcam, Accurate media processing, Webcam usage with Python]
image: https://raw.githubusercontent.com/flojoy-ai/docs/main/docs/nodes/INSTRUMENTS/WEB_CAM/CAMERA/examples/EX1/output.jpeg
---  

In this example app, the [`CAMERA`](https://github.com/flojoy-io/nodes/blob/main/INSTRUMENTS/WEB_CAM/CAMERA/CAMERA.py) node takes and returns a picture from a camera connected to the computer.

Before using the node, you'll need to define the Camera index in the node parameter to choose your Camera (e.g. Webcam, USB camera, etc.).

To do that, you can follow [this link](https://stackoverflow.com/questions/57577445/list-available-cameras-opencv-python?fbclid=IwAR2PJTQGE7QohTPChRG_N6hk07gjaGDnanT02aWX0oYvr9ytNGzdSkEC48c), run the python script to list all the cameras available on your computer, and then select the one that you want to use. (The index is the port where the camera is connected).

The [`IMSHOW`](https://github.com/flojoy-io/nodes/blob/main/VISUALIZERS/PLOTLY/TABLE/TABLE.py) node displays the image taken by the camera that was selected.