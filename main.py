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
        self.closeFileButton.hide()
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
        self.fileButton.clicked.connect(self.fileButtonClicked)
        self.closeFileButton.clicked.connect(self.closeFileButtonClicked)
        self.timer.timeout.connect(self.update)
        self.timerRecord.timeout.connect(self.writeVideo)

    def fileButtonClicked(self):
        fileName = QFileDialog.getOpenFileName(self, "Open video", QtCore.QDir.homePath(), "Video Files (*.mp4 *.avi *.gif)")
        if fileName[0]:
            self.closeFileButton.show()
            self.timer.stop()
            self.c.stream.off()
            self.c.clear()
            # self.setUpdatesEnabled(False)
            self.c.stream.on(fileName[0])
            # self.setUpdatesEnabled(True)
            self.timer.start()

    def closeFileButtonClicked(self):
        self.closeFileButton.hide()
        self.timer.stop()
        self.c.stream.off()
        self.c.clear()
        self.c.stream.on()
        self.timer.start()

    def settingsButtonClicked(self):
        if self.stackedWidget.currentWidget() == self.home:
            self.timer.stop()
            self.stackedWidget.setCurrentWidget(self.settings)
            self.anim = QPropertyAnimation(self.settings, b"geometry")
            self.anim.setDuration(500)
            self.anim.setStartValue(QRect(0, 0, 0, self.height()))
            self.anim.setEndValue(QRect(0, 0, self.width()-40, self.height()))
            self.anim.setEasingCurve(QtCore.QEasingCurve.Linear)
            self.anim.start()
            self.fileButton.hide()
        else:
            self.anim2 = QPropertyAnimation(self.settings, b"geometry")
            self.anim2.setDuration(500)
            self.anim2.setStartValue(QRect(0, 0, self.width()-40, self.height()))
            self.anim2.setEndValue(QRect(0, 0, 0, self.height()))
            self.anim2.setEasingCurve(QtCore.QEasingCurve.Linear)
            self.anim2.start()
            self.anim2.finished.connect(lambda: self.stackedWidget.setCurrentWidget(self.home))
            self.fileButton.show()
            self.timer.start()


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
            self.fileButton.show()
            self.timerRecord.stop()

        else:
            self.record = True
            self.pauseButton.show()
            icon.addFile(u":/stopRecord_icon/res/icons/stop.png", QSize(), QIcon.Normal, QIcon.On)
            self.recordButton.setIcon(icon)
            self.c.stream.startRecord(self.fps)
            self.settingsButton.hide()
            self.fileButton.hide()
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

            self.c.framePreProcessed = frame.copy()
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

            if not self.c.stream.isWebcam and self.c.stream.videoFps < self.fps:
                # print(f"FPS:{self.fps} FPSVid{self.c.stream.videoFps} = {round(1000/(self.fps - self.c.stream.videoFps))}")
                cv2.waitKey(round(1000/(self.fps - self.c.stream.videoFps)))
            else:
                pass
        else:
            pass


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.showMaximized()
    sys.exit(app.exec_())
