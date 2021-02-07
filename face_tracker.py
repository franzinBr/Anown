# BY: ALAN FRANZIN DE OLIVEIRA

import dlib
import cv2


class Face_tracker:
    def __init__(self):
        self.trackers = []
        self.boxes_face = []

    def face_track(self, img):
        index_false = []
        self.boxes_face.clear()
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        for i, track in enumerate(self.trackers):
            conf = track.update(rgb)
            if conf > 7:
                pos = track.get_position()
                x1 = int(pos.left())
                y1 = int(pos.top())
                x2 = int(pos.right())
                y2 = int(pos.bottom())
                face = [x1, y1, x2, y2]
                self.boxes_face.append(face)
            else:
                index_false.append(i)

        return self.boxes_face, index_false
