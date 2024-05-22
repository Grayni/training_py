import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtGui import QScreen


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Center the app')
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()  # coords app
        screen = QApplication.primaryScreen()  # main screen
        cp = screen.availableGeometry().center()  # center point
        qr.moveCenter(cp)  # center app -> in center point
        self.move(qr.topLeft())  # move app


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Demo()

    sys.exit(app.exec_())
