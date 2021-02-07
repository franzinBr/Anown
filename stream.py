# BY: ALAN FRANZIN DE OLIVEIRA

import cv2
import os
import time
import numpy as np
import csv


class Stream:
    def __init__(self):
        self.cap = None
        self.frame = None
        self.frameProcessed = None
        self.video = None
        self.isWebcam = True
        self.ports = []
        self.resolutions = []

    def on(self, video=None):
        if video:
            self.cap = cv2.VideoCapture(video)
            self.isWebcam = False
        else:
            self.ports = self.listCam()
            if self.ports:
                self.cap = cv2.VideoCapture(self.ports[0], cv2.CAP_DSHOW)
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2000)
                self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2000)
                self.isWebcam = True

        return self.cap.isOpened()

    def listCam(self):
        port = 0
        working_ports = []
        while True:
            cam = cv2.VideoCapture(port, cv2.CAP_DSHOW)
            if not cam.isOpened():
                break
            hasFrame, img = cam.read()
            if hasFrame:
                working_ports.append(port)
            port += 1
        return working_ports

    def off(self):
        self.cap.release()

    def readStream(self):
        hasFrame, self.frame = self.cap.read()
        self.frame = cv2.flip(self.frame, 1)
        return hasFrame

    def startRecord(self):
        outFolder = "Videos"
        if not os.path.exists(outFolder):
            os.makedirs(outFolder)
        if self.isWebcam:
            fps = 20
            size = (self.frameProcessed.shape[1], self.frameProcessed.shape[0])
        else:
            fps = self.cap.get(cv2.CAP_PROP_FPS)
            size = (self.cap.get(3), self.cap.get(4))

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        t = time.time()
        video_name = "{}/AnownV_{}.mp4".format(outFolder, t)
        self.video = cv2.VideoWriter(video_name, fourcc, fps, size)

    def stopRecord(self):
        self.video.release()
        self.video = None

    def takePicture(self):
        outFolder = "Pictures"
        if not os.path.exists(outFolder):
            os.makedirs(outFolder)
        t = time.time()
        img_name = "{}/AnownP_{}.png".format(outFolder, t)
        cv2.imwrite(img_name, self.frameProcessed)
