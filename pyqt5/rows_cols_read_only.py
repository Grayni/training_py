import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QStyledItemDelegate


class ReadOnlyDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        print('createEditor event fired')
        return


class MainWindow(QTableWidget):
    def __init__(self):
        super().__init__(5, 5)
        self.resize(1400, 600)

        for i in range(5):
            self.setColumnWidth(i, 250)
            self.setRowHeight(i, 100)

        delegate = ReadOnlyDelegate(self)
        self.setItemDelegateForRow(1, delegate)
        self.setItemDelegateForColumn(0, delegate)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())