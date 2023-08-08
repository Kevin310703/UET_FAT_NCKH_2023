import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1200, 300, 1200, 1200) 
        self.setWindowTitle('Play Video ')   #tiêu đề của cửa sổ
        self.setToolTip(' Play Video')
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'FAT.ico')
        self.setWindowIcon(QIcon(icon_path))
        
        p = self.palette()
        p.setColor(QPalette.Window, Qt.gray ) #màu cho cửa sổ
        self.setPalette(p)

        self.creat_player()


    def creat_player(self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()
        
        self.openBtn = QPushButton('Open Video')  #nút ấn video
        self.openBtn.clicked.connect(self.open_file)

        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)



        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,0)
        self.slider.sliderMoved.connect(self.set_position)
        
        hbox = QHBoxLayout()             #tạo hộp(căn chỉnh các tiện ích theo chiều ngang)
        hbox.setContentsMargins(0,0,0,0) #đặt lề về 0

        hbox.addWidget(self.openBtn)  #openvideo
        hbox.addWidget(self.playBtn)  #play
        hbox.addWidget(self.slider) #thanh trượt

        vbox = QVBoxLayout()    #căn chỉnh tiện ích theo chiều dọc
        vbox.addWidget(videowidget)

        vbox.addLayout(hbox)

        self.mediaPlayer.setVideoOutput(videowidget)

        self.setLayout(vbox)

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)


    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self,'Open Video')

        if filename != '' :
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)


    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState :
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    
    def mediastate_changed(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
             self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))


    def position_changed(self,position):
        self.slider.setValue(position)

    
    def duration_changed(self,duration):
        self.slider.setRange(0,duration)


    def set_position(self,position):
        self.mediaPlayer.setPosition(position)



def window(): 
    app = QApplication(sys.argv)   
    win = Window()
    win.show()
    sys.exit(app.exec_())

window()