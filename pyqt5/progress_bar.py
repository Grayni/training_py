import sys
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
from PyQt5.QtCore import QBasicTimer


class ProgressBar(QWidget):
    def __init__(self):
        super().__init__()
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(50, 50, 300, 15)

        self.btnStart = QPushButton('Start', self)
        self.btnStart.setGeometry(50, 80, 100, 30)
        self.btnStart.clicked.connect(self.startBar)

        self.btnReset = QPushButton('Reset', self)
        self.btnReset.setGeometry(215, 80, 100, 30)
        self.btnReset.clicked.connect(self.resetBar)

        self.timer = QBasicTimer()
        self.step = 0

    def startBar(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btnStart.setText('Start')
        else:
            self.timer.start(100, self)
            self.btnStart.setText('Stop')

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.btnStart.setText('Start')
            return
        self.step += 1
        self.progressBar.setValue(self.step)

    def resetBar(self):
        self.step = 0
        self.timer.stop()
        self.progressBar.setValue(self.step)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    p_bar = ProgressBar()
    p_bar.resize(370, 130)
    p_bar.show()

    sys.exit(app.exec_())
