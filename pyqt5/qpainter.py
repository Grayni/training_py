import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap, QPen

image_path = r"C:\Users\grayni\Pictures\GOGwizNXQAAkKTD.jpeg"


class WinPaint(QWidget):
    def __init__(self):
        super().__init__()
        self.image = QPixmap(image_path)

    def paintEvent(self, event):
        pen = QPen()
        pen.setWidth(5)

        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)
        painter.setPen(pen)
        painter.drawEllipse(300, 300, 150, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    paint = WinPaint()
    paint.show()

    sys.exit(app.exec_())
