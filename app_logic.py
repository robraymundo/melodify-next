import os

class SongNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class SongTracker:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_song = None

    def add_song_directory(self, music_folder):
        self.clear() # clears the songs from the previous directory

        for file_name in os.listdir(music_folder):
            if file_name.endswith((".mp3", ".wav")):
                new_song = SongNode(os.path.join(music_folder, file_name))
                if not self.head:
                    self.head = new_song
                else:
                    current = self.head
                    while current.next:
                        current = current.next
                    current.next = new_song
                    new_song.prev = current

                    self.tail = new_song
                    self.head.prev = self.tail

        if self.head is None:
            return

        self.current_song = self.head

    def next_song(self):
        if self.current_song.next:
            self.current_song = self.current_song.next
        else:
            self.current_song = self.head

    def prev_song(self):
        if self.current_song.prev:
            self.current_song = self.current_song.prev

    def clear(self):
        self.head = None

