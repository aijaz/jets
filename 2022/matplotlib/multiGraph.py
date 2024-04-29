import sys
import random
import matplotlib
matplotlib.use('Qt5Agg')

from PySide6 import QtCore, QtWidgets, QtWebSockets
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QFontDialog
from PySide6.QtGui import QPalette, QColor, QPixmap, QFont, QFontDatabase
from PySide6.QtCore import QSize, Qt, QEvent
from PySide6.QtCore import QTimer

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from websockets.server import serve

class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class AlertWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(AlertWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("My App")

        self.main_image = QLabel()

        self.setCentralWidget(self.main_image)

        self.pixmap = QPixmap("./alert.png").scaled(224, 282)
        self.main_image.installEventFilter(self)
        self.main_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_image.setPixmap(self.pixmap)
        self.setMinimumSize(224, 282)
        QTimer.singleShot(1, self.topLeft)

    def topLeft(self):
        # no need to move the point of the geometry rect if you're going to use
        # the reference top left only
        self.move(0, 0)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.alert_window = AlertWindow(*args, **kwargs)


        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(self.canvas)

        n_data = 700
        self.xdata = list(range(n_data))
        self.ydata = [10 for i in range(n_data)]
        self.ydata2 = [-10 for i in range(n_data)]
        self.ydata3 = [0 for i in range(n_data)]

        # We need to store a reference to the plotted line
        # somewhere, so we can apply the new data to it.
        self._plot_ref1 = None
        self._plot_ref2 = None
        self._plot_ref3 = None
        self.update_plot()

        self.setMinimumSize(1024, 800)
        self.show()

        # Setup a timer to trigger the redraw by calling update_plot.
        # self.timer = QtCore.QTimer()
        # self.timer.setInterval(20)
        # self.timer.timeout.connect(self.update_plot)
        # self.timer.start()

        self.server = QtWebSockets.QWebSocketServer("", QtWebSockets.QWebSocketServer.NonSecureMode)
        self.server.listen(port=8765)
        self.server.newConnection.connect(self.onNewConnection)

        self.clientConnection = None
        self.clients = []
        self.message_num = 0



    def onNewConnection(self):
        self.clientConnection = self.server.nextPendingConnection()
        self.clientConnection.textMessageReceived.connect(self.processTextMessage)
        self.clientConnection.disconnected.connect(self.socketDisconnected)
        self.clients.append(self.clientConnection)

    def call_hospital(self):
        self.alert_window.show()

    def processTextMessage(self,  message):
        pitch,roll,yaw,gx,gy,gz,ax,ay,az,rx,ry,rz = message.split(",")
        self.ydata = self.ydata[1:] +   [float(ax)]
        self.ydata2 = self.ydata2[1:] + [float(ay)]
        self.ydata3 = self.ydata3[1:] + [float(az)]
        self.message_num += 1
        threshold = 5

        if float(ay) > threshold or \
                float(ay) < -threshold or \
                float(ax) > threshold or \
                float(ax) < -threshold or \
                float(az) > threshold or \
                float(az) < -threshold:
            self.call_hospital()

        if self.message_num % 4 == 0:
            self.update_plot()
        # if (self.clientConnection):
        #     self.clientConnection.sendTextMessage(message)


    def socketDisconnected(self):
        if (self.clientConnection):
            self.clients.remove(self.clientConnection)
            self.clientConnection.deleteLater()


    def update_plot(self):
        # Drop off the first y element, append a new one.

        # Note: we no longer need to clear the axis.
        if self._plot_ref1 is None:
            # First time we have no plot reference, so do a normal plot.
            # .plot returns a list of line <reference>s, as we're
            # only getting one we can take the first element.
            plot_refs1 = self.canvas.axes.plot(self.xdata, self.ydata, color='blue', label="X", linewidth=4)
            plot_refs2 = self.canvas.axes.plot(self.xdata, self.ydata2, color='red', label="Y", linewidth=4)
            plot_refs3 = self.canvas.axes.plot(self.xdata, self.ydata3, color='green', label="Z", linewidth=4)
            self.canvas.axes.legend(loc="upper left")

            self._plot_ref1 = plot_refs1[0]
            self._plot_ref2 = plot_refs2[0]
            self._plot_ref3 = plot_refs3[0]
        else:
            # We have a reference, we can use it to update the data for that line.
            self._plot_ref1.set_ydata(self.ydata)
            self._plot_ref2.set_ydata(self.ydata2)
            self._plot_ref3.set_ydata(self.ydata3)

        # Trigger the canvas to update and redraw.
        self.canvas.draw()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()

