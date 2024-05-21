import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout, QSizePolicy, QApplication


class GridDemo(QWidget):
    def __init__(self):
        super().__init__()

        values = ['1', '2', '3',
                  '4', '5', '6',
                  '7', '8', '9']

        positions = [(r, c) for r in range(3) for c in range(3)]

        layoutGrid = QGridLayout()
        self.setLayout(layoutGrid)

        for positions, value in zip(positions, values):
            print(f'Coordinate: {positions} with value of {value}')
            button = QPushButton(value)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            layoutGrid.addWidget(button, *positions)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    gridButtons = GridDemo()
    gridButtons.show()

    sys.exit(app.exec_())
