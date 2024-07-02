import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, \
    QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QPoint


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.oldPosition = None
        self.window_width, self.window_height = 800, 600
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet('''
            QWidget {
                font-size: 20px;
            }
        ''')

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(550, 50, 200, 50)

        self.btn = QPushButton('Hello', self)
        self.btn.setGeometry(250, 250, 300, 300)

    # action 1
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    # action 2
    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
