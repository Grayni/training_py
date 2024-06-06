import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QPlainTextEdit, QVBoxLayout
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


class TextEdit(QPlainTextEdit):
    def __init__(self):
        super().__init__()

        regexp = QRegExp('^[A-Za-z]*$')
        self.validator = QRegExpValidator(regexp)

    def keyPressEvent(self, event):
        state = self.validator.validate(event.text(), 0)

        if state[0] == QRegExpValidator.Acceptable or state[1] in ('\x08', '\r'):
            super().keyPressEvent(event)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(1000, 600)
        mainLayout = QVBoxLayout()
        validatior = QRegExpValidator(QRegExp('^[0-9]+'))

        self.lineEdit = QLineEdit()
        self.lineEdit.setStyleSheet('''font-size: 30px; height: 50px; color: blue;''')

        self.lineEdit.setValidator(validatior)

        self.textEdit = TextEdit()
        self.textEdit.setStyleSheet('''font-size:30px;''')


        mainLayout.addWidget(self.lineEdit)
        mainLayout.addWidget(self.textEdit)

        self.setLayout(mainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
