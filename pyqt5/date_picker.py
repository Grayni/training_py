import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget
import win32com.client as win32

xlApp = win32.Dispatch('Excel.Application')
xlApp.visible = True


class CalendarApp(QCalendarWidget):
    def __init__(self):
        super().__init__()
        self.clicked.connect(self.insert_date)

    def insert_date(self, date):
        try:
            xlApp.Selection.value = date.toPyDate().strftime('%d/%m/%Y')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cal = CalendarApp()
    cal.show()

    sys.exit(app.exec_())
