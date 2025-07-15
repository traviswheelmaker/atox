import os, random
import vlc



class Playback:
    def __init__(self) -> None:
        self.vlc_instance: vlc.Instance = vlc.Instance()
        self.vlc_player: vlc.MediaPlayer = self.vlc_instance.media_player_new()

        self.loopmode: bool = False
        self.loopmode_temp_off: bool = False

        self.is_paused: bool = False
        

    def play_song(self, song: str) -> None:
        if self.loopmode_temp_off:
            self.loopmode, self.loopmode_temp_off = True, False

        song_to_play: vlc.Media = self.vlc_instance.media_new(song)
        self.vlc_player.set_media(song_to_play)
        self.vlc_player.play()
    
    
    #DISPLAY FUNCTIONS
    def freeplay_ticker(self) -> bool:
        if bool(self.vlc_player.is_playing()) or self.is_paused:
            return False
        return True

    def get_position(self) -> float:
        return self.vlc_player.get_position()#returns as a percentage, from 0 to 100


    #CONTROL FUNCTIONS
    def skip(self) -> None:
        self.is_paused = False #unpausing automatically will make skip button feel more responsive
        self.vlc_player.set_pause(0)

        if self.loopmode:
            self.loopmode, self.loopmode_temp_off = False, True
        
        self.vlc_player.stop()

    def pause(self): #input: bool:   by default, we flip the pause from on-off or off-on
        self.is_paused = not self.is_paused
        self.vlc_player.set_pause(int(self.is_paused))

    def loop(self) -> None:
        self.loopmode = not self.loopmode

    def volume_adjust(self, volume: int) -> None:
        #volume from ui will range from ints 0-10. we will make custom adjustments with a dict
        volume_adjust_dict: dict[int, int] = {
            0: 0,
            1: 30,
            2: 45,
            3: 60,
            4: 70,
            5: 80,
            6: 90,
            7: 100,
            8: 110,
            9: 120, 
            10: 130
        }
        self.vlc_player.audio_set_volume(volume_adjust_dict[volume])
    
