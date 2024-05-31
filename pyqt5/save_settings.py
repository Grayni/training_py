import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QSettings


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.settings = QSettings('MyQtApp', 'App1')

        print(self.settings.fileName())
        try:
            self.resize(self.settings.value('window size'))
            self.move(self.settings.value('window position'))
        except Exception as e:
            print(e)

    def closeEvent(self, event):
        self.settings.setValue('window size', self.size())
        self.settings.setValue('window position', self.pos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
