import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QPushButton, QListWidget
from PyQt5.QtCore import Qt, QUrl


class ListboxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(600, 600)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []

            for url in event.mimeData().urls():
                if url.isLocalFile():
                    links.append(str(url.toLocalFile()))
                else:
                    links.append(str(url.toString()))

            self.addItems(links)

        else:
            event.ignore()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200, 600)
        self.listView = ListboxWidget(self)

        self.btn = QPushButton('Get Value', self)
        self.btn.setGeometry(800, 400, 200, 50)

        self.btn.clicked.connect(lambda: print(self.getSelectedItem()))

    def getSelectedItem(self):
        item = QListWidgetItem(self.listView.currentItem())
        return item.text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    listbox_view = MainWindow()
    listbox_view.show()

    sys.exit(app.exec_())
