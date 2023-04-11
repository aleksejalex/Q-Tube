"""
Question:
Answer:

20230321
"""

import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit, QFileDialog
from PySide6.QtWebEngineWidgets import QWebEngineView
from pytube import extract
import pytube as pt


class YouTubePlayer(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("My Own YouTube Player")
        self.setWindowIcon(QIcon("youtube.png"))
        self.setMinimumSize(640, 480)

        self.curr_video_link = ""

        # Create web engine view widget
        self.webview = QWebEngineView(self)
        # self.webview.setUrl(QUrl("https://www.youtube.com/embed/nE_MF2fwbA4"))  # Khrennikov video
        self.webview.setUrl(QUrl("https://www.youtube.com/embed/9AxYOmYKpZg"))

        # Create 'address bar'
        self.address_bar = QLineEdit()
        # Create buttons
        self.btn_download = QPushButton(text="Download")
        self.btn_show = QPushButton(text="Show")
        self.btn_quit = QPushButton(text="Quit")
        self.btn_some = QPushButton(text="Download")
        self.btn_about = QPushButton(text="About...")

        # Connect events to buttons
        self.btn_download.clicked.connect(self.download_video)
        self.btn_show.clicked.connect(self.show_video)
        self.btn_about.clicked.connect(self.about_qtube)
        self.btn_quit.clicked.connect(self.quit_qtube)

        # Create layout(s)
        layout = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout2.addWidget(self.address_bar)
        layout2.addWidget(self.webview)

        layout3.addWidget(self.btn_download)
        layout3.addWidget(self.btn_show)
        layout3.addWidget(self.btn_about)
        layout3.addWidget(self.btn_quit)
        # layout3.addWidget(self.btn_some)

        # Connect and fill layouts in correct order
        layout.addLayout(layout2)
        layout.addLayout(layout3)

        self.setLayout(layout)

    def offer_streams(self, video_obj):
        # todo impl 'offer_streams'
        id_of_stream = 0

        return id_of_stream

    def download_video(self):
        """
            tba
        """
        if self.curr_video_link is None or self.curr_video_link == "":
            # raise BaseException("No link provided!")
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("No link provided!")
            msgBox.exec()
        else:
            # Get video with stream
            # Download file
            # url_chameleon = 'https://www.youtube.com/watch?v=VtFRWaC-aU4'
            print(type(self.curr_video_link))
            video_obj = pt.YouTube(self.curr_video_link)
            # this will print out all possibilities, select that stream, which suits you and identify it by its index
            # number
            id_of_stream = self.offer_streams(video_obj)
            video_stream = video_obj.streams.get_by_itag(134)  # that number you can get with previous line of the code
            # video_stream.download(filename="title_of_the_video.mp4")
            print(video_obj.title)
            # Choose where to save it
            # Open a file dialog to get the filename and path to save the file
            filename, _ = QFileDialog.getSaveFileName(self, "Save File", ".mp4")
            # todo progress bar in window
            video_stream.download(filename=filename)
            pass
        pass

    pass

    def show_video(self):
        """

        """
        video_link = self.address_bar.text()
        print(f"User entered link >>>{video_link}<<<")
        self.webview.setUrl(QUrl(video_link))
        id = extract.video_id(video_link)
        print(f"id of inputed video is: {id}")
        emb_video_link = "https://www.youtube.com/embed/" + str(id)
        self.webview.setUrl(QUrl(emb_video_link))
        self.curr_video_link = video_link

    def about_qtube(self):
        """shows info about Q-Tube"""
        msgBox = QtWidgets.QMessageBox()
        # self.text = QtWidgets.QLabel("Hello World")
        # self.text.setAlignment(QtCore.Qt.AlignCenter)
        # todo add nice format in msgBox
        msgBox.setWindowTitle("Aboout Q-Tube")
        msgBox.setText("Q-Tube \n Created by @aleksejalex \n Copyright AG 2023")
        msgBox.exec()

    def quit_qtube(self):
        """Safely quits."""
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    player = YouTubePlayer()
    player.show()

    sys.exit(app.exec())
