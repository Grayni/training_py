import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class HyperlinkLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__()
        self.setStyleSheet('font-size: 35px;')
        self.setOpenExternalLinks(True)
        self.setParent(parent)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(255, 65)
        self.setStyleSheet('padding: 10px;')
        linkTemplate = '<a href="{0}">{1}</a>'

        label1 = HyperlinkLabel(self)
        label1.setText(linkTemplate.format('https://google.com', 'Google'))

        label2 = HyperlinkLabel(self)
        label2.setText(linkTemplate.format('https://github.com', 'Github'))
        label2.move(120, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
