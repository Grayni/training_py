import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QListWidget,\
                            QHBoxLayout, QVBoxLayout, QFrame
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

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.layout_1 = QVBoxLayout()
        self.layout_2 = QVBoxLayout()

        # column 1
        self.list = QListWidget()
        self.btn1 = QPushButton('Stop')

        self.layout_1.addWidget(self.list)
        self.layout_1.addWidget(self.btn1)

        self.frame = QFrame()
        self.frame.setLayout(self.layout_1)
        self.layout.addWidget(self.frame)

        self.layout.addLayout(self.layout_2, 7)

        # column 2
        self.btn2 = QPushButton('Start', clicked=self.resize_animation)
        self.layout_2.addWidget(self.btn2)

    def resize_animation(self):
        self.animation = QPropertyAnimation(self.frame, b'geometry')
        self.animation.setDuration(500)  # 0.5 sec

        if self.frame.width() == 278:
            # x, y, width, height
            self.animation.setStartValue(QRect(self.frame.x(), self.frame.y(), 278, self.frame.height()))
            self.animation.setEndValue(QRect(self.frame.x(), self.frame.y(), 100, self.frame.height()))
            self.animation.start()
        else:
            # x, y, width, height
            self.animation.setStartValue(QRect(self.frame.x(), self.frame.y(), 100, self.frame.height()))
            self.animation.setEndValue(QRect(self.frame.x(), self.frame.y(), 278, self.frame.height()))
            self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
