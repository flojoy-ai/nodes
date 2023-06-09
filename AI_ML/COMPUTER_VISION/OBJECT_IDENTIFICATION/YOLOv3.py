import cv2
import numpy as np

whT = 320

cap = cv2.VideoCapture(0)

classesFile = "coco.names"
classNames = []

with open("/Users/jinwonlee/Github/flojoy/studio/PYTHON/nodes/AI_ML/COMPUTER_VISION/OBJECT_IDENTIFICATION/coco.names", 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

modelConfiguration = 'yolov3.cfg'
modelWeights = 'yolov3.weights'

net = cv2.dnn.readNetFromDarknet("/Users/jinwonlee/Github/flojoy/studio/PYTHON/nodes/AI_ML/COMPUTER_VISION/OBJECT_IDENTIFICATION/yolov3.cfg",
                                  "/Users/jinwonlee/Github/flojoy/studio/PYTHON/nodes/AI_ML/COMPUTER_VISION/OBJECT_IDENTIFICATION/yolov3.weights")
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

while True:
    success, img = cap.read()

    blob = cv2.dnn.blobFromImage(img, 1/255, (whT, whT), [0,0,0], 1, crop=False)
    net.setInput(blob)

    layerNames = net.getLayerNames()

    outputNames = net.forward([layerNames[i[0]-1] for i in net.UnconnectedOutLayers()])

    outputs = net.forward(outputNames)
    

    cv2.imshow('Image', img)
    cv2.waitKey(1)