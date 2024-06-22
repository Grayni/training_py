import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextBrowser
from PyQt5.QtGui import QTextCursor


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        layout = QVBoxLayout()

        self.button = QPushButton('Demo', clicked=self.generateContent)
        layout.addWidget(self.button)

        self.textBrowser = QTextBrowser()
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setStyleSheet('font-size; 20px')
        layout.addWidget(self.textBrowser)

        self.setLayout(layout)

    def generateContent(self):
        self.textBrowser.moveCursor(QTextCursor.Start)
        self.textBrowser.append('Hello World')
        self.textBrowser.append('<a href=https://google.com>google.com</a>')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
