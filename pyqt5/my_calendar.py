import sys
from datetime import datetime
import calendar
from PyQt5.QtWidgets import QCalendarWidget, QApplication, QWidget
from PyQt5.QtCore import QDate


class CalendarDemo(QWidget):
    global currentYear, currentMonth

    currentMonth = datetime.now().month
    currentYear = datetime.now().year

    def __init__(self):
        super().__init__()
        self.mini_calendar = None
        self.setWindowTitle('Calendar')
        self.setGeometry(300, 300, 450, 300)
        self.initUI()

    def initUI(self):
        self.mini_calendar = QCalendarWidget(self)
        self.mini_calendar.move(20, 20)
        self.mini_calendar.setGridVisible(True)
        print(currentMonth)
        self.mini_calendar.setMinimumDate(QDate(currentYear, currentMonth - 1, 1))
        self.mini_calendar.setMaximumDate(QDate(currentYear, currentMonth + 1, calendar.monthrange(currentYear, currentMonth+1)[1]))

        self.mini_calendar.setSelectedDate(QDate(currentYear, currentMonth, 9))  # year;month;select_day
        # self.mini_calendar.clicked.connect(lambda dateval: print(dateval.toString()))
        self.mini_calendar.clicked.connect(self.printDateInfo)

    def printDateInfo(self, qDate):
        print(f'{qDate.month()}/{qDate.day()}/{qDate.year()}')
        print(f'Day Number of the year: {str(qDate.dayOfYear())}')
        print(f'Day Number of the week: {str(qDate.dayOfWeek())}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cal = CalendarDemo()
    cal.show()

    sys.exit(app.exec_())


