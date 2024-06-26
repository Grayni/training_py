import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, \
                            QHeaderView, QPushButton, QItemDelegate, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator


class FloatDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super().__init__()

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setValidator(QDoubleValidator())
        return editor


class TableWidget(QTableWidget):
    def __init__(self, df):
        super().__init__()
        self.df = df
        self.setStyleSheet("font-size: 35px;")

        nRows, nCols = self.df.shape
        self.setColumnCount(nCols)
        self.setRowCount(nRows)

        self.setHorizontalHeaderLabels(('Col X', 'Col Y'))
        self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.setItemDelegateForColumn(1, FloatDelegate())

        # data insertion
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                self.setItem(i, j, QTableWidgetItem(str(self.df.iloc[i, j])))

    def updateDF(self, row, column):
        text = self.item(row, column).text()
        self.df.iloc[row, column] = text


class MainWindow(QWidget):
    data = {
        'Col X': list('ABCD'),
        'Col Y': [10, 20, 30, 40]
    }

    df = pd.DataFrame(data)

    def __init__(self):
        super().__init__()
        self.resize(1000, 700)

        mainLayout = QVBoxLayout()

        table = TableWidget(MainWindow.df)
        mainLayout.addWidget(table)

        button_print = QPushButton('Display DF')
        button_print.setStyleSheet('font-size: 30px;')
        button_print.clicked.connect(self.print_DF_Values)
        mainLayout.addWidget(button_print)

        button_export = QPushButton('Export to CSV file')
        button_export.setStyleSheet('font-size: 30px;')
        button_export.clicked.connect(self.export_to_csv)
        mainLayout.addWidget(button_export)

        self.setLayout(mainLayout)

    def print_DF_Values(self):
        print(self.df)

    def export_to_csv(self):
        self.df.to_csv('Data export.csv', index=False)
        print('CSV file exported.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
