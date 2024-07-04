import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, \
    QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QRect, QPropertyAnimation


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 800, 600
        self.setMinimumSize(self.window_width, self.window_height)
        self.setStyleSheet('''
            QWidget {
                font-size: 20px;
            }
        ''')
        self.layout = QVBoxLayout()

        self.button = QPushButton('Start', clicked=self.animation)
        self.layout.addWidget(self.button)

        self.frame = QFrame(self)
        self.frame.setStyleSheet('background-color: red;')
        self.frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.frame.move(10, 10)
        self.frame.resize(100, 100)

        self.setLayout(self.layout)

    def animation(self):
        self.animation = QPropertyAnimation(self.frame, b'geometry')
        self.animation.setDuration(10000)
        self.animation.setStartValue(QRect(10, self.frame.y(), 100, 100))
        self.animation.setEndValue(QRect(10, self.frame.y(), 200, 200))
        self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
