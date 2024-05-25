import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.Qt import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
