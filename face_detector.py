# BY: ALAN FRANZIN DE OLIVEIRA

from face_tracker import Face_tracker
import cv2
import os
import numpy as np
import dlib


class Face_detector:
    def __init__(self, path="models"):
        self.prototxtFile = os.path.sep.join([path, "deploy.prototxt"])
        self.modelFile = os.path.sep.join(
            [path, "res10_300x300_ssd_iter_140000_fp16.caffemodel"]
        )
        self.net = cv2.dnn.readNetFromCaffe(self.prototxtFile, self.modelFile)
        self.img = None
        self.boxes_face = []
        self.tracker = Face_tracker()

    def detect(self, img, conf_threshold=0.7):
        self.img = img.copy()
        self.boxes_face.clear()
        (height, width) = img.shape[:2]
        blob = cv2.dnn.blobFromImage(
            img, 1.0, (300, 300), [104, 117, 123], False, False
        )

        self.net.setInput(blob)
        detections = self.net.forward()

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > conf_threshold:
                box = detections[0, 0, i, 3:7] * np.array(
                    [width, height, width, height]
                )
                box = box.astype("int")
                (x1, y1, x2, y2) = box
                self.boxes_face.append(box)
        return self.boxes_face
