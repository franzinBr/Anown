# BY: ALAN FRANZIN DE OLIVEIRA

from face_detector import Face_detector
from face_tracker import Face_tracker
from face_recognizer import Face_recognizer
from face_occluder import Face_occluder
from stream import Stream
import cv2
import dlib


class Controller:
    def __init__(self, path="models"):
        self.stream = Stream()
        self.detector = Face_detector()
        self.tracker = Face_tracker()
        self.recognizer = Face_recognizer()
        self.occluder = Face_occluder()
        self.iface_wanted = []
        self.framePreProcessed = None

    def clear(self):
        self.detector = Face_detector()
        self.tracker = Face_tracker()
        self.recognizer = Face_recognizer()
        self.iface_wanted = []
        self.framePreProcessed = None

    def check(self, iT_suspect):
        for i in iT_suspect:
            self.iface_wanted.append([self.recognizer.face_descriptors[i], i])

        if self.iface_wanted:
            facesd = self.recognizer.transform128D(
                self.detector.boxes_face, self.framePreProcessed
            )

        facew_remove = []
        for face_dec in self.iface_wanted:
            face = self.recognizer.rec(facesd, face_dec[0])
            if type(face) is not bool:
                track = dlib.correlation_tracker()
                r = dlib.rectangle(face[0], face[1], face[2], face[3])
                rgb = cv2.cvtColor(self.framePreProcessed, cv2.COLOR_BGR2RGB)
                track.start_track(rgb, r)
                self.tracker.trackers[face_dec[1]] = track
                facew_remove.append([face_dec[0], face_dec[1]])

        for facew in facew_remove:
            self.iface_wanted.remove(facew)


    def isPointInRect(self, x, y, rect):
        if x > rect[0] and x < rect[2] and y > rect[1] and y < rect[3]:
            return True
        return False

    def clickScreen(self, x, y):
        for index, faceT in enumerate(self.tracker.boxes_face):
            if self.isPointInRect(x, y, faceT):
                self.tracker.trackers.pop(index)
                self.recognizer.face_descriptors.pop(index)
                return

        for faceD in self.detector.boxes_face:
            if self.isPointInRect(x, y, faceD):
                track = dlib.correlation_tracker()
                r = dlib.rectangle(faceD[0], faceD[1], faceD[2], faceD[3])
                rgb = cv2.cvtColor(self.framePreProcessed, cv2.COLOR_BGR2RGB)
                track.start_track(rgb, r)
                self.tracker.trackers.append(track)

                shape = self.recognizer.sp(self.framePreProcessed, r)
                align_face = dlib.get_face_chip(self.framePreProcessed, shape)
                face_descriptor = (
                    self.recognizer.facerec.compute_face_descriptor(
                        align_face
                    )
                )
                self.recognizer.face_descriptors.append(face_descriptor)
