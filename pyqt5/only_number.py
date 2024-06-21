import sys
from PyQt5.QtWidgets import QApplication, QLineEdit
from PyQt5.QtGui import QDoubleValidator, QValidator


class MainWindow(QLineEdit):
    def __init__(self):
        super().__init__()
        self.resize(500, 120)
        self.setStyleSheet("font-size: 20px;")

        self.editingFinished.connect(self.validating)

    def validating(self):
        validation_rule = QDoubleValidator(-100, 100, 0)

        if validation_rule.validate(self.text(), 14)[0] == QValidator.Acceptable:
            self.setFocus()
        else:
            self.setText('no no no!!!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
