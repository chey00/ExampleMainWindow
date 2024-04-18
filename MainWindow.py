from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QMainWindow, QStatusBar, QProgressBar

from CentralWidget import CentralWidget

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Meine erste GUI")

        centralWidget = CentralWidget(self)
        centralWidget.set_value.connect(self.set_value_progress_bar)
        self.setCentralWidget(centralWidget)

        self.setStatusBar(QStatusBar())

        layout_status_bar = self.statusBar().layout()

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 10)

        layout_status_bar.addWidget(self.progress_bar)

    @pyqtSlot(int)
    def set_value_progress_bar(self, value: int):
        self.progress_bar.setValue(value)
