import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QHBoxLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QHBoxLayout()

        self.model = QStandardItemModel()

        # states
        self.combo_states = QComboBox()
        self.combo_states.setFixedSize(325, 50)
        self.combo_states.setFont(QFont('', 12))
        self.combo_states.setModel(self.model)

        self.combo_cities = QComboBox()
        self.combo_cities.setFixedSize(325, 50)
        self.combo_cities.setFont(QFont('', 12))
        self.combo_cities.setModel(self.model)

        # add data
        for k, v in data.items():
            state = QStandardItem(k)
            self.model.appendRow(state)
            for value in v:
                city = QStandardItem(value)
                state.appendRow(city)

        self.combo_states.currentIndexChanged.connect(self.updateStateCombo)
        self.updateStateCombo(0)

        main_layout.addWidget(self.combo_states)
        main_layout.addWidget(self.combo_cities)

        self.setLayout(main_layout)

    def updateStateCombo(self, index):
        index = self.model.index(index, 0, self.combo_states.rootModelIndex())
        self.combo_cities.setRootModelIndex(index)
        self.combo_cities.setCurrentIndex(0)



data = {
    'California': ['San Francisco', 'Oakland', 'Los Angeles'],
    'Illinois': ['Chicago', 'Springfield', 'Evanston'],
    'Texas': ['Austin', 'Houston', 'San Antonio']
}


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
