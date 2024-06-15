import sys
from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem, QLabel, QDialog


class MainWindow(QListWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setStyleSheet('font-size: 40px;')

        companies = ['Apple', 'Google', 'Facebook', 'Yandex', 'Microsoft']

        for company in companies:
            self.addItem(company)

        self.itemDoubleClicked.connect(self.launchPopup)

    def launchPopup(self, item):
        popup = Popup(item.text(), self)
        popup.show()


class Popup(QDialog):
    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.resize(400, 200)
        self.label = QLabel(name, self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
