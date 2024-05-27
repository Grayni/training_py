import sys

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox


class ComboBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        lstCompany = ['Google', 'Facebook', 'Microsoft', 'Twitter', 'Yahoo']

        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(50, 50, 400, 35)

        self.comboBox.addItems(lstCompany)

        self.btn = QPushButton('Click', self)
        self.btn.setGeometry(170, 120, 120, 35)
        self.btn.clicked.connect(self.getComboValue)

    def getComboValue(self):
        print(self.comboBox.currentText(), self.comboBox.currentIndex())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ComboBoxDemo()
    demo.show()

    sys.exit(app.exec_())
