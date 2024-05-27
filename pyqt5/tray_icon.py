import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon


if __name__ == '__main__':
    app = QApplication(sys.argv)
    trayIcon = QSystemTrayIcon(QIcon('sources/twitter.png'), parent=app)
    trayIcon.setToolTip('Check out my tray icon')
    trayIcon.show()

    menu = QMenu()
    exitAction = menu.addAction('Exit')
    exitAction.triggered.connect(app.quit)
    trayIcon.setContextMenu(menu)

    sys.exit(app.exec_())
