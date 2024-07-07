import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDateEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QDate


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(500)
        self.setStyleSheet('''
            QWidget {
                font-size: 20px;
            }
        ''')

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.dateEdit = QDateEdit()
        self.dateEdit.setCalendarPopup(True)
        layout.addWidget(self.dateEdit)

        self._today_button = QPushButton('&Today', clicked=self.setToday)
        self.dateEdit.calendarWidget().layout().addWidget(self._today_button)

    def setToday(self):
        today = QDate.currentDate()
        self.dateEdit.calendarWidget().setSelectedDate(today)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()

    sys.exit(app.exec_())
