import os

class fileHandler:
    def __init__(self):
        self.selected_playlist: list[str] = []


    def get_filepaths_from_dir(self, selected_path="songs/") -> list[str]:
        self.selected_playlist = [f"{selected_path}{song_path}" for song_path in (os.listdir(selected_path)) if self.file_check(song_path)]
        return self.selected_playlist

    def file_check(self, song: str) -> bool:
        ending: str = song[len(song)-4:]
        if ending == ".mp3" or ending == ".wav":
            return True
        return False

    