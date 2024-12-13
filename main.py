from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon
from main_window import Ui_melodify
from app_logic import SongTracker
import sys
import os

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_melodify()
        self.ui.setupUi(self)

        self.setFixedSize(496, 194)

        # linked list logic
        self.song_tracker = SongTracker()
        self.is_playing = False
        self.valid_directory = False

        # media player logic
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.song = ''

        # connect signals
        self.ui.play_button.clicked.connect(self.play)
        self.ui.play_button.clicked.connect(self.show_pause_icon)
        self.ui.next_button.clicked.connect(self.next)
        self.ui.prev_button.clicked.connect(self.prev)
        self.ui.file_button.clicked.connect(self.open_song_directory)
        self.player.positionChanged.connect(self.update_progress_bar)

        self.update_buttons() # initially disables the buttons until a valid directory is selected

    def play(self):
        if self.is_playing:
            self.player.pause()
            self.is_playing = False
        else:
            if self.song == '':
                self.load_file()
            self.player.play()
            self.is_playing = True

    def next(self):
        self.song_tracker.next_song()
        self.load_song()
        self.show_pause_icon()

    def prev(self):
        self.song_tracker.prev_song()
        self.load_song()
        self.show_pause_icon()

    def load_song(self):
        self.is_playing = False
        self.load_file()
        self.play()

    def load_file(self):
        self.song = self.song_tracker.current_song.data
        self.player.setSource(QUrl.fromLocalFile(self.song))
        song_title = os.path.splitext(os.path.basename(self.song))[0]
        self.ui.title_label.setText(song_title)

    def show_pause_icon(self):
        if self.is_playing:
            self.ui.play_button.setIcon(QIcon("graphics/pause_button.png"))
        else:
            self.ui.play_button.setIcon(QIcon("graphics/play_button.png"))

    def open_song_directory(self):
        directory_path = QFileDialog.getExistingDirectory(self, "Select Directory")

        # if the user cancels the dialog, return
        if directory_path == '':
            return

        self.song_tracker.add_song_directory(directory_path)

        self.reset_music_player()   # resets the music player when a new directory is selected

        if self.song_tracker.head is None:
            self.ui.title_label.setText("No song found in the directory")
            self.valid_directory = False
            self.update_buttons()
        else:
            self.valid_directory = True
            self.update_buttons()
            self.load_file()

    def update_progress_bar(self, position):
        duration = self.player.duration()
        progress = (position / duration) * 100
        self.ui.progress_bar.setValue(progress)

    def reset_music_player(self):
        self.player.stop()
        self.ui.progress_bar.setValue(0)
        self.is_playing = False
        self.show_pause_icon()

    def update_buttons(self):
        enabled = self.valid_directory
        for button in [self.ui.play_button, self.ui.next_button, self.ui.prev_button]:
            button.setEnabled(enabled)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
