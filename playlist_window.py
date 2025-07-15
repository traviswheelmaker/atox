from PySide6.QtWidgets import QPushButton, QLabel, QWidget, QVBoxLayout, QScrollArea
from PySide6.QtCore import Qt
from collections.abc import Callable
import constants as c



class playlist(QWidget):
    def __init__(self):
        super().__init__()
        self.layout: QVBoxLayout = QVBoxLayout(self)

        #temp qlabels used as stacked widgets
        self.title_label: QLabel = QLabel("")
        self.button_widget: QWidget = QWidget()
        self.button_layout: QVBoxLayout = QVBoxLayout(self.button_widget)
        self.scroll_area: QScrollArea = QScrollArea()
        self.scroll_area.setWidget(self.button_widget)

        self.button_layout.setContentsMargins(5, 10, 5, 10)
        self.button_layout.setSpacing(10)

        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.button_widget.setObjectName("playlist_button_holder")
        self.scroll_area.setObjectName("playlist_scroll")


        

        


        widget_list: list[QWidget] = [self.title_label, self.scroll_area]
        
        [self.layout.addWidget(widget) for widget in widget_list]

    def load_playlist(self, playlist_name: str, playlist: list[str], song_request_func: Callable[[str], None]) -> None:
        self.title_label.setText(playlist_name)

        def create_button(song_name: str) -> None:
            button = QPushButton(song_name)
            button.clicked.connect(lambda: song_request_func(song_name))
            self.button_layout.addWidget(button)
        


        [create_button(song) for song in playlist]

