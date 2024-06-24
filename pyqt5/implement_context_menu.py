import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMenu, QListWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QEvent


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 800, 600
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.listWidget = QListWidget()
        self.listWidget.addItems(('Facebook', 'Microsoft', 'Google'))
        self.listWidget.installEventFilter(self)
        layout.addWidget(self.listWidget)

    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu and source is self.listWidget:
            menu = QMenu()
            menu.addAction('Action 1')
            menu.addAction('Action 2')
            menu.addAction('Action 3')

            if menu.exec_(event.globalPos()):
                item = source.itemAt(event.pos())
                print(item.text())
            return True

        return super().eventFilter(source, event)


if __name__ == '__main__':
    QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    app.setStyleSheet('''QWidget {
                            font-size: 20px;
                         }''')
    demo = MainWindow()
    demo.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing window...')
