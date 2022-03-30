from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


from pytube import YouTube

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setIU()

    def setIU(self):
        self.topSettings()
        self.mainMenu()

        self.show()

    def mainMenu(self):
        widget = QWidget()

        h_box = QHBoxLayout()

        write = QLabel("<b>Enter the YouTube URL:</b> ")
        self.link = QLineEdit()
        self.link.setPlaceholderText("Paste the URL here")
        downloadButton = QPushButton("Download")
        pasteButton = QPushButton("Paste")

        downloadButton.clicked.connect(self.download)
        pasteButton.clicked.connect(self.paste)

        h_box.addWidget(write)
        h_box.addWidget(self.link)
        h_box.addWidget(downloadButton)
        h_box.addWidget(pasteButton)

        widget.setLayout(h_box)

        self.setCentralWidget(widget)

    def download(self):
        url = self.link.text()
        YouTube(url).streams.first().download()

    def paste(self):
        self.link.setText(QApplication.clipboard().text())


    def topSettings(self):
        self.setWindowTitle("YouTube Video Downloader - @omeredk")
        self.setWindowIcon(QIcon("logo.png"))

        #Size Settings
        self.setGeometry(250, 250, 700, 100)
        self.setMaximumSize(1050, 100)
        self.setMinimumSize(700, 100)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())