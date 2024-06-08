import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, \
                            QStackedWidget, QRadioButton, QHBoxLayout, QVBoxLayout


class WidgetButtons(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        for i in range(4):
            layout.addWidget(QPushButton(f'Button #{i}'))

        self.setLayout(layout)


class WidgetLineEdits(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        for i in range(4):
            layout.addWidget(QLineEdit(f'LineEdit #{i}'))

        self.setLayout(layout)


class WidgetRadionButtons(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        for i in range(4):
            layout.addWidget(QRadioButton(f'RadioButton #{i}'))

        self.setLayout(layout)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        mainLayout = QVBoxLayout()
        self.stackedWidget = QStackedWidget()

        self.stackedWidget.addWidget(WidgetButtons())  # index 0
        self.stackedWidget.addWidget(WidgetLineEdits())  # index 1
        self.stackedWidget.addWidget(WidgetRadionButtons())  # index 2

        buttonPrevious = QPushButton('Previous')
        buttonPrevious.clicked.connect(self.previousWidget)

        buttonNext = QPushButton('Next')
        buttonNext.clicked.connect(self.nextWidget)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(buttonPrevious)
        buttonLayout.addWidget(buttonNext)

        mainLayout.addWidget(self.stackedWidget)
        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)

    def nextWidget(self):
        self.stackedWidget.setCurrentIndex((self.stackedWidget.currentIndex() + 1) % 3)

    def previousWidget(self):
        self.stackedWidget.setCurrentIndex((self.stackedWidget.currentIndex() - 1) % 3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
