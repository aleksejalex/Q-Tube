"""
Pozor: problem!
stoji to na tom, ze worker (to, co odvadi praci) behem prace vysle signal o tom, ze prace pokrocila. Bez toho to nejde.


"""

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QProgressBar, QVBoxLayout, QWidget
import sys
import time

class Worker(QThread):
    """Worker thread that performs the work"""
    progress_changed = Signal(int)

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(101):
            self.progress_changed.emit(i)
            time.sleep(0.1)

class loading_bar_MaWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Loading Bar")
        self.setGeometry(100, 100, 300, 100)

        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)

        central_widget = QWidget()
        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(self.progress_bar)
        central_widget.setLayout(vbox_layout)
        self.setCentralWidget(central_widget)

        self.worker = Worker()
        self.worker.progress_changed.connect(self.update_progress)

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def start(self):
        self.progress_bar.setValue(0)
        self.worker.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = loading_bar_MaWin()
    window.show()
    window.start()
    sys.exit(app.exec())
