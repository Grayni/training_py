import sys
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar
from PyQt5.QtCore import QTimer


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Progress Bar Demo')
        self.resize(500, 75)

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(25, 25, 300, 40)
        self.progressBar.setMaximum(10)
        self.progressBar.setValue(0)

        timer = QTimer(self)
        timer.timeout.connect(self.increaseStep)
        timer.start(1000)

    def increaseStep(self):
        self.progressBar.setValue(self.progressBar.value() + 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()

    sys.exit(app.exec_())
