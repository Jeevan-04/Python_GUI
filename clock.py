# # importing libraries
# from PyQt5.QtWidgets import *
# from PyQt5 import QtCore, QtGui
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# import sys

# # creating a clock class
# class Clock(QMainWindow):

# 	# constructor
# 	def __init__(self):
# 		super().__init__()

# 		# creating a timer object
# 		timer = QTimer(self)

# 		# adding action to the timer
# 		# update the whole code
# 		timer.timeout.connect(self.update)

# 		# setting start time of timer i.e 1 second
# 		timer.start(1000)

# 		# setting window title
# 		self.setWindowTitle('Clock')

# 		# setting window geometry
# 		self.setGeometry(200, 200, 300, 300)

# 		# setting background color to the window
# 		self.setStyleSheet("background : black;")

# 		# creating hour hand
# 		self.hPointer = QtGui.QPolygon([QPoint(6, 7),
# 										QPoint(-6, 7),
# 										QPoint(0, -50)])

# 		# creating minute hand
# 		self.mPointer = QPolygon([QPoint(6, 7),
# 								QPoint(-6, 7),
# 								QPoint(0, -70)])

# 		# creating second hand
# 		self.sPointer = QPolygon([QPoint(1, 1),
# 								QPoint(-1, 1),
# 								QPoint(0, -90)])
# 		# colors
# 		# color for minute and hour hand
# 		self.bColor = Qt.green

# 		# color for second hand
# 		self.sColor = Qt.red

# 	# method for paint event
# 	def paintEvent(self, event):

# 		# getting minimum of width and height
# 		# so that clock remain square
# 		rec = min(self.width(), self.height())

# 		# getting current time
# 		tik = QTime.currentTime()

# 		# creating a painter object
# 		painter = QPainter(self)


# 		# method to draw the hands
# 		# argument : color rotation and which hand should be pointed
# 		def drawPointer(color, rotation, pointer):

# 			# setting brush
# 			painter.setBrush(QBrush(color))

# 			# saving painter
# 			painter.save()

# 			# rotating painter
# 			painter.rotate(rotation)

# 			# draw the polygon i.e hand
# 			painter.drawConvexPolygon(pointer)

# 			# restore the painter
# 			painter.restore()


# 		# tune up painter
# 		painter.setRenderHint(QPainter.Antialiasing)

# 		# translating the painter
# 		painter.translate(self.width() / 2, self.height() / 2)

# 		# scale the painter
# 		painter.scale(rec / 200, rec / 200)

# 		# set current pen as no pen
# 		painter.setPen(QtCore.Qt.NoPen)


# 		# draw each hand
# 		drawPointer(self.bColor, (30 * (tik.hour() + tik.minute() / 60)), self.hPointer)
# 		drawPointer(self.bColor, (6 * (tik.minute() + tik.second() / 60)), self.mPointer)
# 		drawPointer(self.sColor, (6 * tik.second()), self.sPointer)


# 		# drawing background
# 		painter.setPen(QPen(self.bColor))

# 		# for loop
# 		for i in range(0, 60):

# 			# drawing background lines
# 			if (i % 5) == 0:
# 				painter.drawLine(87, 0, 97, 0)

# 			# rotating the painter
# 			painter.rotate(6)

# 		# ending the painter
# 		painter.end()

# # Driver code
# if __name__ == '__main__':

#     app = QApplication(sys.argv)

# # creating a clock object
# win = Clock()

# # show
# win.show()

# exit(app.exec_())


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer, QPoint, QRectF
from PyQt5.QtGui import QPainter, QColor, QPen

class AnalogClock(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Panchang Clock')

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)  # Update every second

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawClock(qp)
        qp.end()

    def drawClock(self, qp):
        qp.setRenderHint(QPainter.Antialiasing)

        side = min(self.width(), self.height())
        qp.setViewport(0, 0, side, side)
        qp.setWindow(-50, -50, 100, 100)

        qp.translate(self.width() / 2, self.height() / 2)

        # Draw clock outline
        outerRadius = 40
        innerRadius = 38
        qp.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        qp.drawEllipse(QRectF(-outerRadius, -outerRadius, 2 * outerRadius, 2 * outerRadius))

        # Draw clock ticks
        for i in range(12):
            angle = i * 30 * 3.14159 / 180.0
            x1 = (outerRadius - 2) * 0.8 * round(100 * qCos(angle))
            y1 = (outerRadius - 2) * 0.8 * round(100 * qSin(angle))
            x2 = outerRadius * 0.95 * round(100 * qCos(angle))
            y2 = outerRadius * 0.95 * round(100 * qSin(angle))
            qp.drawLine(QPoint(x1, y1), QPoint(x2, y2))

        # Draw clock hands
        qp.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        qp.drawLine(0, 0, 20, 0)  # Hour hand

        qp.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        qp.drawLine(0, 0, 30, 0)  # Minute hand

        qp.setPen(QPen(Qt.blue, 1, Qt.SolidLine))
        qp.drawLine(0, 0, 40, 0)  # Second hand


def main():
    app = QApplication(sys.argv)
    clock = AnalogClock()
    clock.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
