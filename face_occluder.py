# BY: ALAN FRANZIN DE OLIVEIRA

import cv2
import numpy as np


class Face_occluder:

    def face_gaus(self, image, f=3.0):
        sh = image.shape[:2]
        s = map(lambda s: int(s/f-1) if int(s/f) % 2 == 0 else int(s/f), sh)
        s = list(s)
        return cv2.GaussianBlur(image, (s[1], s[0]), 0)

    def face_black(self, image):
        return np.zeros((image.shape[0], image.shape[1], 3), np.uint8)

    def face_pixelate(self, image, blocks=3):
        (h, w) = image.shape[:2]
        xSteps = np.linspace(0, w, blocks + 1, dtype="int")
        ySteps = np.linspace(0, h, blocks + 1, dtype="int")
        for i in range(1, len(ySteps)):
            for j in range(1, len(xSteps)):

                startX = xSteps[j - 1]
                startY = ySteps[i - 1]
                endX = xSteps[j]
                endY = ySteps[i]
                roi = image[startY:endY, startX:endX]
                (B, G, R) = [int(x) for x in cv2.mean(roi)[:3]]
                cv2.rectangle(
                    image, (startX, startY), (endX, endY), (B, G, R), -1
                )
        return image

    def occluder(self, img, boxes_face, type="pixelated"):
        image = img.copy()
        for bface in boxes_face:
            face = img[bface[1]:bface[3], bface[0]:bface[2]]
            if type == "pixelated":
                face = self.face_pixelate(face, 15)
            elif type == "gaus":
                face = self.face_gaus(face)
            elif type == "black":
                face = self.face_black(face)

            image[bface[1]:bface[3], bface[0]:bface[2]] = face

        return image
