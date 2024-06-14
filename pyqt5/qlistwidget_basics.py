import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem


class MainWindow(QListWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setStyleSheet("font-size: 35px;")

        jan = 'January'
        feb = 'February'
        mar = 'March'
        apr = 'April'
        may = 'May'
        jun = 'June'

        # add one item at a time
        self.addItem(jan)
        #self.addItem(QListWidgetItem(jan))
        self.addItem(feb)

        # add multiple items
        self.addItems([apr, jun])

        # add item based row position
        self.insertItem(2, QListWidgetItem(mar))
        self.insertItem(4, QListWidgetItem(may))

        self.itemDoubleClicked.connect(self.getItem)

    def getItem(self, lstItem):
        print(self.currentItem().text())
        print(lstItem.text())
        print(self.currentRow())





if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
