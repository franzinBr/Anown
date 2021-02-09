# BY: ALAN FRANZIN DE OLIVEIRA

import cv2
import os
import time
import numpy as np
from playsound import playsound
from queue import Queue
from threading import Thread


class Stream:
    def __init__(self):
        self.cap = None
        self.frame = None
        self.hasFrame = False
        self.frameProcessed = None
        self.video = None
        self.videoFps = 0
        self.isWebcam = True
        self.ports = []
        self.resolutions = []
        self.Q = None

    def on(self, video=None, queueSize=1024):
        if video:
            self.cap = cv2.VideoCapture(video)
            self.isWebcam = False
            self.Q = Queue(maxsize=queueSize)
            self.videoFps = self.cap.get(cv2.CAP_PROP_FPS)
        else:
            self.ports = self.listCam()
            if self.ports:
                self.cap = cv2.VideoCapture(self.ports[0], cv2.CAP_DSHOW)
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2000)
                self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2000)
                self.isWebcam = True

        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self.cap.isOpened()

    def update(self):
        while True:
            if self.isWebcam:
                hasFrame, frame = self.cap.read()
                self.frame = cv2.flip(frame, 1)
                self.hasFrame = hasFrame
            if not self.isWebcam and not self.Q.full():
                hasFrame, frame = self.cap.read()
                self.frame = cv2.flip(frame, 1)
                self.hasFrame = hasFrame
                self.Q.put((self.hasFrame, self.frame))

            if not self.hasFrame:
                return 0

    def read(self):
        if self.isWebcam:
            return self.hasFrame, self.frame
        print("aqui")
        return self.Q.get()

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

    def startRecord(self, fpsExternal):
        pSound = "res/sound_effects/record.wav"
        tSound = Thread(target=self.playSound, args=(pSound,))
        tSound.daemon = True
        tSound.start()

        outFolder = "Videos"
        if not os.path.exists(outFolder):
            os.makedirs(outFolder)
        if self.isWebcam:
            fps = int(fpsExternal) - 5
            size = (self.frameProcessed.shape[1], self.frameProcessed.shape[0])
        else:
            fps = self.cap.get(cv2.CAP_PROP_FPS)
            size = (int(self.cap.get(3)), int(self.cap.get(4)))

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        t = time.time()
        video_name = "{}/AnownV_{}.mp4".format(outFolder, t)
        self.videoFps = fps
        self.video = cv2.VideoWriter(video_name, fourcc, fps, size)

    def playSound(self, path):
        playsound(path)

    def stopRecord(self):
        pSound = "res/sound_effects/record_off.wav"
        tSound = Thread(target=self.playSound, args=(pSound,))
        tSound.daemon = True
        tSound.start()

        self.video.release()
        self.video = None

    def takePicture(self):
        pSound = "res/sound_effects/picture.mp3"
        tSound = Thread(target=self.playSound, args=(pSound,))
        tSound.daemon = True
        tSound.start()

        outFolder = "Pictures"
        if not os.path.exists(outFolder):
            os.makedirs(outFolder)
        t = time.time()
        img_name = "{}/AnownP_{}.png".format(outFolder, t)
        cv2.imwrite(img_name, self.frameProcessed)
