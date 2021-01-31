import numpy as np
import cv2
import os
import time
labelsPath = os.path.sep.join(["yolo-coco", "coco.names"])
LABELS = open(labelsPath).read().strip().split("\n")
weightsPath = os.path.sep.join(["yolo-coco", "yolov3.weights"])
configPath = os.path.sep.join(["yolo-coco", "yolov3.cfg"])
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
# image = cv2.imread("D:\downloads\crowd counter\yolo-object-detection/input.jpg")
def count(image):
    (H, W) = image.shape[:2]
    # determine only the *output* layer names that we need from YOLO
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),swapRB=True, crop=False)
  
    net.setInput(blob)
    start = time.time()
    layerOutputs = net.forward(ln)
    end = time.time()

    boxes = []
    confidences = []
    classIDs = []
    cnt=0
    # loop over each of the layer outputs
    for output in layerOutputs:
    # # loop over each of the detections
        for detection in output:
            
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]
            if confidence > 0.65 and classID == 0:
                pass
                print("human detected {}".format(confidence))
            if confidence > 0.65 and classID == 67:
                pass
                print("phone detected {}".format(confidence))
# count(image)