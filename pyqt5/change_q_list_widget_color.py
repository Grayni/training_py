import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt


class MainWindow(QListWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setStyleSheet('font-size: 50px;')

        colors = ['red', 'green', 'blue', 'purple']
        toColors = [True, False, True, False]

        for color, cond in zip(colors, toColors):
            item = QListWidgetItem(color)

            if cond:
                item.setForeground(Qt.red)
            self.addItem(item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
