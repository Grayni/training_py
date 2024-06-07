import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QComboBox, QVBoxLayout, QHBoxLayout


class comboCompanies(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet('font-size: 25px;')
        self.addItems(['Microsoft', 'Facebook', 'Apple', 'Google'])
        self.currentIndexChanged.connect(self.getComboValue)

    def getComboValue(self):
        print(self.currentText())


class TableWidget(QTableWidget):
    def __init__(self):
        super().__init__(1, 5)
        self.setHorizontalHeaderLabels(list('ABCDE'))
        self.setColumnWidth(4, 200)
        self.verticalHeader().setDefaultSectionSize(50)
        self.horizontalHeader().setDefaultSectionSize(250)

        combo = comboCompanies(self)
        self.setCellWidget(0, 4, combo)


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1600, 600)

        main_layout = QVBoxLayout()
        table = TableWidget()
        main_layout.addWidget(table)

        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()

    sys.exit(app.exec_())
