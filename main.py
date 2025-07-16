import sys
from collections.abc import Callable

from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
from PySide6.QtCore import QTimer

from playback import Playback
from file_handler import fileHandler
from play_order import playOrder

import constants as c
import styles as styles

from sidebar import sidebar
from playbar import playbar
from window_stack import windowStack


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        #first, we load up the file_handler, playback, and playorder classes
        self.player: Playback = Playback()
        self.file_handler: fileHandler = fileHandler()
        self.play_order: playOrder = playOrder()

        self.playlist_isnt_empty: bool = False

        self.load_new_playlist()

        
        self.main_widget: QWidget = QWidget()
        self.main_layout: QGridLayout = QGridLayout(self.main_widget)

        self.playbar: playbar = playbar()
        self.windowStack: windowStack = windowStack()
        self.sidebar: sidebar = sidebar(self.windowStack.sidebar_names_list)

        #the sidebar and window should soak up extra vertical space, and the window should also take up extra horizontal space
        self.main_layout.addWidget(self.sidebar, 0, 0)
        self.main_layout.addWidget(self.windowStack, 0, 1)
        self.main_layout.addWidget(self.playbar, 1, 0, 1, -1)
        
        self.main_layout.setColumnStretch(0, 1)
        self.main_layout.setColumnStretch(1, c.SIDEBAR_TO_WINDOW_RATIO)
        
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.main_widget.setObjectName("main_widget")

        stylesheet: str = styles.main()      
        self.main_widget.setStyleSheet(stylesheet)

        self.setGeometry(*c.STARTING_GEOMETRY)
        self.setWindowTitle(c.APPLICATION_NAME)

        self.setCentralWidget(self.main_widget)

        #assigning functions to buttons

        self.sidebar.link_to_window(self.windowStack.layout.setCurrentIndex)

        functions_dict: dict[str, Callable[[], None]] = {
            "play/pause": self.player.pause,
            "skip": self.player.skip,
            "loop": self.player.loop,
            "volume_adjust": self.player.volume_adjust
        }
        self.playbar.link_to_mixer(functions_dict)

        self.windowStack.playlist_window.load_playlist("Total Library", self.play_order.get_playlist_display(), self.song_request)

        self.main_widget.show()
        
        if self.playlist_isnt_empty:
            self.player.play_song(self.play_order.current_song)
            self.player.pause()
            self.display_update()   

            self.freeplay_timer: QTimer = QTimer()
            self.freeplay_timer.timeout.connect(self.new_song_update)
            self.freeplay_timer.start(400)


            self.position_timer: QTimer = QTimer()
            self.position_timer.timeout.connect(self.pos_update)
            self.position_timer.start(100)

    def song_request(self, song_display_name: str) -> None:
        self.play_order.update_current_song(self.play_order.get_path_from_display(song_display_name))

        if self.player.is_paused:
            self.player.is_paused = False
            self.playbar.play_and_pause_button.setStyleSheet(styles.button_highlight()) #similar to skip button, we have to make sure its highlighted 
        self.player.play_song(self.play_order.current_song)

        self.display_update()



    def new_song_update(self) -> None:
        if self.player.freeplay_ticker():
            if not self.player.loopmode:
                self.play_order.forward() 
            self.player.play_song(self.play_order.current_song)
            
            self.display_update()

    def display_update(self) -> None: #everything EXCEPT position is updated here
        play_order: list[str] = self.play_order.get_play_display()

        self.windowStack.playview_window.update_play_order(play_order)
        self.playbar.update_song_name_label(play_order[0])

            
    def pos_update(self) -> None:
        position: float = self.player.get_position()

        self.playbar.play_progress_bar.setValue(position * 10000) #position is percentage from 0 to 1, length of progress bar is 10000, so we multiply them to get pos
    
    def load_new_playlist(self) -> None:
        playlist: list[str] = self.file_handler.get_filepaths_from_dir()
        self.playlist_isnt_empty = bool(playlist) 
        if self.playlist_isnt_empty:
            self.play_order.load_playlist(playlist)
        
    
def start() -> None:
    app: QApplication = QApplication(sys.argv)
    window: Main = Main()
    window.show()
    app.exec()

