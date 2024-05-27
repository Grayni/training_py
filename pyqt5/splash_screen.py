import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt, QTimer


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lbl = QLabel('<font color=Green size=12> <b>Hello Word</b> </font>')
    lbl.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    lbl.show()
    QTimer.singleShot(2000, app.quit)

    sys.exit(app.exec_())
