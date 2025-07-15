from PySide6.QtWidgets import QPushButton, QLabel, QWidget, QStackedLayout

import constants as c


from playlist_window import playlist
from playview_window import playView


class windowStack(QWidget):
    def __init__(self):
        super().__init__()
        self.layout: QStackedLayout = QStackedLayout(self)

        #temp qlabels used as stacked widgets
        self.playview_window: QWidget = playView()
        self.playlist_window: QWidget = playlist()


        
        self.widget_list: list[QWidget] = [self.playview_window, self.playlist_window]
        self.sidebar_names_list: list[str] = ["Song Queue", "Pick Song"]
        
        def window_setup(widget: QWidget) -> None:
            self.layout.addWidget(widget)

        [window_setup(widget) for widget in self.widget_list]

        self.setContentsMargins(10, 10, 50, 10)
    
