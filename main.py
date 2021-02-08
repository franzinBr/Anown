# BY: ALAN FRANZIN DE OLIVEIRA

from anown import Ui_MainWindow

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets, QtGui, QtCore
from controller import Controller
import time, cv2


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.c = Controller()
        self.timer = QTimer()
        self.timerRecord = QTimer()
        self.pauseButton.hide()
        self.startTimer()

        self.frame_count = 0
        self.timeDiference = 0
        self.fps = 0
        self.record = False
        self.isPaused = False
        self.Pw = 0
        self.Ph = 0

        self.slots()

        self.frameLabel.installEventFilter(self)

    def closeEvent(self, event):
        self.timer.stop()
        self.c.stream.off()

    def eventFilter(self, obj, event):
        if not self.record:
            if obj is self.frameLabel and event.type() == QtCore.QEvent.MouseButtonPress:
                p = event.pos()
                gp = self.mapToGlobal(p)
                rw = self.window().mapFromGlobal(gp)
                x = int(rw.x()-((self.frameLabel.width()-self.Pw))/2)
                y = int(rw.y()-((self.frameLabel.height()-self.Ph))/2)
                if(x >= 0 and x <= self.Pw and y >= 0 and y <= self.Ph):
                    scaleX = self.c.stream.cap.get(3) / self.Pw
                    scaleY = self.c.stream.cap.get(4) / self.Ph
                    noScaledX = int(x * scaleX)
                    noScaledY = int(y * scaleY)
                    self.c.clickScreen(noScaledX, noScaledY)

        return super(MainWindow, self).eventFilter(obj, event)

    def slots(self):
        self.recordButton.clicked.connect(self.recordButtonClicked)
        self.pictureButton.clicked.connect(self.c.stream.takePicture)
        self.settingsButton.clicked.connect(self.settingsButtonClicked)
        self.pauseButton.clicked.connect(self.pauseButtonClicked)
        self.timer.timeout.connect(self.update)
        self.timerRecord.timeout.connect(self.writeVideo)

    def settingsButtonClicked(self):
        if self.stackedWidget.currentWidget() == self.home:
            self.stackedWidget.setCurrentWidget(self.settings)
        else:
            self.stackedWidget.setCurrentWidget(self.home)

    def pauseButtonClicked(self):
        icon = QIcon()
        self.isPaused = not self.isPaused
        if self.isPaused:
            icon.addFile(u":/Recording_icon/res/icons/recording.jpg", QSize(), QIcon.Normal, QIcon.Off)
            self.pauseButton.setIcon(icon)
            self.timerRecord.stop()
        else:
            icon.addFile(u":/pause_icon/res/icons/pause.png", QSize(), QIcon.Normal, QIcon.Off)
            self.pauseButton.setIcon(icon)
            self.timerRecord.start(1000/self.c.stream.videoFps)


    def recordButtonClicked(self):
        icon = QIcon()
        if self.record:
            self.record = False
            self.pauseButton.hide()
            icon.addFile(u":/Recording_icon/res/icons/recording.jpg", QSize(), QIcon.Normal, QIcon.Off)
            self.recordButton.setIcon(icon)
            self.isPaused = False
            self.c.stream.stopRecord()
            self.settingsButton.show()
            self.timerRecord.stop()
            print(self.i)

        else:
            self.record = True
            self.pauseButton.show()
            icon.addFile(u":/stopRecord_icon/res/icons/stop.png", QSize(), QIcon.Normal, QIcon.On)
            self.recordButton.setIcon(icon)
            self.c.stream.startRecord(self.fps)
            self.settingsButton.hide()
            self.timerRecord.start(1000/self.c.stream.videoFps)

    def startTimer(self):
        if self.c.stream.on():
            self.timer.start()

    def writeVideo(self):
        self.c.stream.video.write(self.c.stream.frameProcessed)

    def update(self):
        hasFrame, frame = self.c.stream.read()
        if hasFrame:
            self.frame_count += 1
            t = time.time()

            self.c.detector.detect(frame)
            boxes_face, index_false = self.c.tracker.face_track(frame)
            self.c.check(index_false)
            if boxes_face:
                frame = self.c.occluder.occluder(frame, boxes_face, "pixelated")

            self.c.stream.frameProcessed = frame

            image = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
            pixmap = QtGui.QPixmap.fromImage(image)
            w = self.width()
            h = self.height()
            pixmap = pixmap.scaled(w-140, h, QtCore.Qt.KeepAspectRatio)
            self.Pw = pixmap.width()
            self.Ph = pixmap.height()
            self.frameLabel.setPixmap(pixmap)

            self.timeDiference += time.time() - t
            self.fps = self.frame_count / self.timeDiference
            if self.frame_count == 1:
                self.timeDiference = 0

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.showMaximized()
    sys.exit(app.exec_())
