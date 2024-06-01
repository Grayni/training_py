from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5 import QtWidgets, QtGui  # crutch


class MainContent(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName('contentWidgets')
        self.setStyleSheet('#contentWidgets {background-color: green;}')
        layout = QVBoxLayout()
        label = QLabel("Main Content")
        layout.addWidget(label)
        self.setLayout(layout)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        opt = QtWidgets.QStyleOption()
        opt.initFrom(self)
        painter = QtGui.QPainter(self)
        self.style().drawPrimitive(QtWidgets.QStyle.PE_Widget, opt, painter, self)