import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QCategoryAxis
from PyQt5.QtCore import QPoint
from PyQt5.Qt import QPen, QFont, QSize, Qt
from PyQt5.QtGui import QColor, QBrush, QLinearGradient, QPainter, QGradient


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)

        self.initChart()

        self.setCentralWidget(self.chartView)


    def initChart(self):
        series = QLineSeries()

        data = [
            QPoint(0, 6),
            QPoint(9, 4),
            QPoint(15, 16),
            QPoint(18, 28),
            QPoint(22, 11),
            QPoint(30, 32)
        ]

        series.append(data)

        # creating chart object
        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)

        # lines color
        pen = QPen(QColor(200, 200, 200))
        pen.setWidth(5)
        series.setPen(pen)

        font = QFont('Open Sans')
        font.setPixelSize(40)
        font.setBold(True)
        chart.setTitleFont(font)
        chart.setTitleBrush(Qt.yellow)
        chart.setTitle('Custom Chart Demo')

        backgroundGradient = QLinearGradient()
        backgroundGradient.setStart(QPoint(0, 0))
        backgroundGradient.setFinalStop(QPoint(0, 1))
        backgroundGradient.setColorAt(0.0, QColor(175, 201, 182))
        backgroundGradient.setColorAt(1.0, QColor(51, 105, 66))
        backgroundGradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        chart.setBackgroundBrush(backgroundGradient)


        plotAreaGradient = QLinearGradient()
        plotAreaGradient.setStart(QPoint(0, 1))
        plotAreaGradient.setFinalStop(QPoint(1, 0))
        plotAreaGradient.setColorAt(0.0, QColor(222, 222, 222))
        plotAreaGradient.setColorAt(1.0, QColor(51, 105, 66))
        plotAreaGradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        chart.setPlotAreaBackgroundBrush(plotAreaGradient)
        chart.setPlotAreaBackgroundVisible(True)

        # custom axis

        axisX = QCategoryAxis()
        axisY = QCategoryAxis()

        labelFont = QFont('Open Sans')
        labelFont.setPixelSize(25)

        axisX.setLabelsFont(labelFont)
        axisY.setLabelsFont(labelFont)

        axisPen = QPen(Qt.white)
        axisPen.setWidth(2)

        axisX.setLinePen(axisPen)
        axisY.setLinePen(axisPen)

        axisBrush = QBrush(Qt.white)
        axisX.setLabelsBrush(axisBrush)
        axisY.setLabelsBrush(axisBrush)

        axisX.setRange(0, 35)
        axisX.append('low', 10)
        axisX.append('medium', 20)
        axisX.append('high', 30)

        axisY.setRange(0, 35)
        axisY.append('slow', 10)
        axisY.append('average', 20)
        axisY.append('fast', 30)

        axisX.setGridLineVisible(False)
        axisY.setGridLineVisible(False)

        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)

        series.attachAxis(axisX)
        series.attachAxis(axisY)


        self.chartView = QChartView(chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    chart_demo = MainWindow()
    chart_demo.show()

    sys.exit(app.exec_())
