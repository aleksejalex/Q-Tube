"""
Question:
Answer:

20230321
"""

import sys
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit, QFileDialog
from PySide6.QtWebEngineWidgets import QWebEngineView
from pytube import extract


class YouTubePlayer(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("My Own YouTube Player")
        self.setWindowIcon(QIcon("youtube.png"))
        self.setMinimumSize(640, 480)

        self.curr_video_link = None

        # Create web engine view widget
        self.webview = QWebEngineView(self)
        self.webview.setUrl(QUrl("https://www.youtube.com/embed/nE_MF2fwbA4"))  # Khrennikov video
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
        #layout3.addWidget(self.btn_some)

        # Connect and fill layouts in correct order
        layout.addLayout(layout2)
        layout.addLayout(layout3)

        self.setLayout(layout)

    def download_video(self):
        """
            tba
        """
        # Get video with stream

        # Download file
        
        # Choose where to save it
        # Open a file dialog to get the filename and path to save the file
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")

        # If a filename was selected, write the contents of the text area to the file
        # if filename:
        #     with open(filename, "w") as f:
        #         f.write(self.text_area.toPlainText())



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
        self.curr_video_link = id

    def about_qtube(self):

        pass


    def quit_qtube(self):
        """Safely quits."""
        self.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)

    player = YouTubePlayer()
    player.show()

    sys.exit(app.exec())
