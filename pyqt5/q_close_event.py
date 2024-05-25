import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.Qt import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            print('escape pressed')
            self.close()

    def closeEvent(self, event):
        reply = QMessageBox.question(self,
                                     'Window Close',
                                     'Are you sure you want to close the window?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
