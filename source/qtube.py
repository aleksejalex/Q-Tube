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
from PySide6.QtWidgets import QListWidget, QListWidgetItem  # for show_list() via msgBox
from PySide6.QtWebEngineWidgets import QWebEngineView
from pytube import extract
import pytube as pt


class YouTubePlayer(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Q-Tube - your friendly YouTube player and downloader")
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

    def download_video(self):
        """
        gets provided link from `address_bar` and if its valid link, the video (in the best
        available quality) is downloaded. Location and name dialog is raised.
        """
        self.curr_video_link = self.address_bar.text()
        if self.curr_video_link is None or self.curr_video_link == "":
            # raise BaseException("No link provided!")
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowIcon(QIcon("warning.png"))
            msgBox.setText("No link provided!")
            msgBox.exec()
        else:
            video_obj = pt.YouTube(self.curr_video_link)
            video_stream = video_obj.streams.get_highest_resolution()
            print(video_obj.title)
            # Open a file dialog to get the filename and path to save the file
            filename, _ = QFileDialog.getSaveFileName(self, "Save File", ".mp4")
            # todo progress bar in window
            msgDownloading = QtWidgets.QMessageBox()
            msgDownloading.setWindowIcon(QIcon("youtube.png"))
            msgDownloading.setText("Your video is downloading... \n \a\a\a Please be patient! \a\a\a")
            msgDownloading.exec()
            video_stream.download(filename=filename)  # saves the video to chosen location with choosen name
            msgDownloading.close()
            #sys.exit(msgDownloading.exec())

    def show_video(self):
        """
        Gets the content of `address_bar` and if there's something, it converts any youtube link to
        YouTube embed link a nd shows the video in window.
        """
        self.curr_video_link = self.address_bar.text()
        if self.curr_video_link is None or self.curr_video_link == "":
            # raise BaseException("No link provided!")
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("No link provided!")
            msgBox.exec()
        else:
            print(f"User entered link >>>{self.curr_video_link}<<<")
            self.webview.setUrl(QUrl(self.curr_video_link))
            id = extract.video_id(self.curr_video_link)
            print(f"id of inputed video is: {id}")
            emb_video_link = "https://www.youtube.com/embed/" + str(id)
            self.webview.setUrl(QUrl(emb_video_link))

    def about_qtube(self):
        """shows info about Q-Tube"""
        msgBox = QtWidgets.QMessageBox()
        # self.text = QtWidgets.QLabel("Hello World")
        # self.text.setAlignment(QtCore.Qt.AlignCenter)
        # todo add nice format in msgBox
        msgBox.setWindowTitle("About Q-Tube")
        msgBox.setWindowIcon(QIcon("youtube.png"))
        msgBox.setText('<h1 style="text-align:center"><span style="font-family:Georgia,serif">Q-Tube</span></h1><p>(read as something in between of &quot;YouTube&quot; and &quot;Cute Tube&quot;)<br /><br />By&nbsp;<a href="https://github.com/aleksejalex">@aleksejalex</a>&nbsp;in 2023<br /><br />YouTube video downloader with GUI written in PyQt6</p>')
        #msgBox.setText("<center><b> <font color='red'>Q-Tube</font></b></center> <br><br> Created by @aleksejalex \n Copyright AG 2023")

        #msgBox.setText("<h3>Formatted Text Example</h3>"
        #         "<p>This is an example of <b>bold text</b> and <i>italic text</i> in a QMessageBox.</p>"
        #         "<p>You can also use <font color='red'>different colors</font> and <u>underlined text</u>.</p>")

        msgBox.exec()

    def quit_qtube(self):
        """Safely quits."""
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    player = YouTubePlayer()
    player.show()

    sys.exit(app.exec())
