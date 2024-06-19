import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTreeView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QImage, QStandardItemModel, QStandardItem


class StandardItem(QStandardItem):
    def __init__(self, txt='', image_path='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)

        if image_path:
            image = QImage(image_path)
            self.setData(image, Qt.DecorationRole)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        treeView = QTreeView()
        treeView.setHeaderHidden(True)
        treeView.header().setStretchLastSection(True)

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()

        photos = StandardItem('Photos', '', set_bold=True)

        stars = StandardItem('stars', './sources/images/1.jpg', 14)
        photos.appendRow(stars)

        dog = StandardItem('dog', './sources/images/2.jpg', 16)
        photos.appendRow(dog)

        rootNode.appendRow(photos)
        treeView.setModel(treeModel)
        treeView.expandAll()

        self.setCentralWidget(treeView)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
