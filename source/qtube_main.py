"""



"""




import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from qtube_app_gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.pushButton_download.clicked.connect(self.button_was_clicked)

        self.ui.setupUi(self)

    def button_was_clicked(self):
        """ testing function """
        print("button as clicked")



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
