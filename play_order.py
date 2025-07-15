import random
import constants as c

class playOrder:
    def __init__(self):
        self.playlist: list[str] = []
        self.play_order: list[str] = []
        self.current_song: str = ""

    def load_playlist(self, playlist: list[str]) -> None:
        if len(playlist) == 0:
            raise ValueError("Cannot input empty playlist into playOrder")
        self.playlist = playlist

        [self.play_order.append(self.random_song()) for q in range(0, 10)]
        self.current_song = self.play_order[0]


    def random_song(self) -> str:
        i: int = random.randint(0, len(self.playlist)-1)
        return self.playlist[i]
    
    def forward(self) -> None:
        self.play_order.pop(0) 
        self.play_order.append(self.random_song())
        self.current_song = self.play_order[0]

    def get_play_display(self) -> list[str]:
        return [song[6:-4] for song in self.play_order] #splices the unnecessary parts of the file name off
    
    def get_playlist_display(self) -> list[str]:
        return [song[6:-4] for song in self.playlist] #splices the unnecessary parts of the file name off
    
    def get_path_from_display(self, song_display_name: str) -> str:
        return f"songs/{song_display_name}.mp3" #WARNING: WONT WORK FOR WAVE FILES
    
    def update_current_song(self, song_name: str) -> None:
        self.current_song = song_name
        self.play_order[0] = song_name
