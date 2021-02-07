# BY: ALAN FRANZIN DE OLIVEIRA

import dlib
import os
import numpy as np


class Face_recognizer:
    def __init__(self, path="models"):
        self.shapeFile = os.path.sep.join(
            [path, "shape_predictor_5_face_landmarks.dat"]
        )
        self.recFile = os.path.sep.join(
            [path, "dlib_face_recognition_resnet_model_v1.dat"]
        )
        self.sp = dlib.shape_predictor(self.shapeFile)
        self.facerec = dlib.face_recognition_model_v1(self.recFile)
        self.face_descriptors = []

    def transform128D(self, boxes_face, img):
        facesd = []
        for face in boxes_face:
            r = dlib.rectangle(face[0], face[1], face[2], face[3])
            shape = self.sp(img, r)
            align_face = dlib.get_face_chip(img, shape)
            face_descriptor = np.array(self.facerec.compute_face_descriptor(
                align_face
            ))
            facesd.append([face_descriptor, face])
        return facesd

    def rec(self, facesd, face_l):
        lost_face = np.array(face_l)
        for des in facesd:
            euclidianDist = np.array(des[0]) - lost_face
            euclidianDist = np.sum(np.multiply(euclidianDist, euclidianDist))
            euclidianDist = np.sqrt(euclidianDist)
            if euclidianDist < 0.5:
                return des[1]
        return False
