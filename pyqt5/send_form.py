import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic


class SendForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('objects/send_form.ui', self)

        self.button.clicked.connect(self.printValue)

    def printValue(self):
        print(self.lineEdit_Entry.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = SendForm()
    form.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing window...')
