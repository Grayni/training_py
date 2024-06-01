import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView
from PyQt5.Qt import QStandardItemModel, QStandardItem
from PyQt5.QtGui import QFont, QColor


class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setFont(fnt)
        self.setText(txt)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tree')
        self.resize(500, 700)

        treeView = QTreeView(self)
        treeView.setHeaderHidden(True)

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()

        '-----------------------------------------'
        # America

        america = StandardItem('America', 16, True)
        california = StandardItem('California', 14)
        america.appendRow(california)

        oakland = StandardItem('Oakland', 12, color=QColor(155, 0, 0))
        sanfrancisco = StandardItem('San Francisco', 12, color=QColor(155, 0, 0))
        sanjose = StandardItem('San Jose', 12, color=QColor(155, 0, 0))

        california.appendRow(oakland)
        california.appendRow(sanfrancisco)
        california.appendRow(sanjose)

        texas = StandardItem('Texas', 14)
        america.appendRow(texas)

        austin = StandardItem('Austin', 12, color=QColor(155, 0, 0))
        houston = StandardItem('Houston', 12, color=QColor(155, 0, 0))
        dallas = StandardItem('Dallas', 12, color=QColor(155, 0, 0))

        texas.appendRow(austin)
        texas.appendRow(houston)
        texas.appendRow(dallas)

        # Canada

        canada = StandardItem('Canada', 16, True)

        alberta = StandardItem('Alberta', 14)
        bc = StandardItem('British Columbia', 14)
        ontario = StandardItem('Ontario', 14)

        canada.appendRows([alberta, bc, ontario])

        rootNode.appendRows([america, canada])

        treeView.setModel(treeModel)

        treeView.doubleClicked.connect(self.getValue)

        self.setCentralWidget(treeView)

    def getValue(self, val):
        print(val.data())
        print(val.row())
        print(val.column())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
