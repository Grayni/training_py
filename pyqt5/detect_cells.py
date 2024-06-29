import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 800, 600
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        tableWidget = QTableWidget(6, 6)
        layout.addWidget(tableWidget)

        tableWidget.selectionModel().selectionChanged.connect(self.on_selectionChanged)

    def on_selectionChanged(self, selected, deselected):

        for ix in selected.indexes():
            print(f'Selected Cell Location Row: {ix.row()}, Column: {ix.column()}')

        for ix in deselected.indexes():
            print(f'Deselected Cell Location Row: {ix.row()}, Column: {ix.column()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
