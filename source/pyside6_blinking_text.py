import PySide6
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout
import sys


class BlinkingLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self._blinking = False
        self._timer = QTimer()
        self._timer.timeout.connect(self.toggle_color)

    def blink(self, interval):
        self._timer.start(interval)
        self._blinking = True

    def toggle_color(self):
        if self.palette().color(self.foregroundRole()) == self.palette().color(self.backgroundRole()):
            self.setPalette(self.palette().foreground())
        else:
            self.setPalette(self.palette().background())

    def stop_blinking(self):
        self._timer.stop()
        self._blinking = False


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = BlinkingLabel("Blinking text!")
        self.label.setAlignment(PySide6.QtCore.Qt.AlignVCenter)
        self.label.setStyleSheet("background-color: white")
        self.label.setFixedWidth(200)
        self.label.setFixedHeight(50)

        self.start_button = QPushButton("Start Blinking", clicked=self.start_blinking)
        self.stop_button = QPushButton("Stop Blinking", clicked=self.stop_blinking)
        self.stop_button.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        self.setLayout(vbox)

    def start_blinking(self):
        self.label.blink(500)
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_blinking(self):
        self.label.stop_blinking()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
