from PySide6.QtWidgets import QPushButton, QLabel, QWidget, QGridLayout, QSlider, QProgressBar, QSizePolicy, QVBoxLayout
from PySide6.QtCore import Qt, QTimer
from collections.abc import Callable

import constants as c
from styles import button_highlight


class playbar(QWidget):
    def __init__(self):
        super().__init__()
        self.layout: QGridLayout = QGridLayout(self)

        self.song_name_label = QLabel()
        self.play_progress_bar: QProgressBar = QProgressBar()
        self.volume_slider: QSlider = QSlider(Qt.Orientation.Vertical)
        self.volume_label: QLabel = QLabel("Vol")
        self.play_and_pause_button: QPushButton = QPushButton("Play   |   Pause")
        self.loop_button: QPushButton = QPushButton("Loop")
        self.skip_button: QPushButton = QPushButton("Skip")
        self.widget_list: list[QWidget] = [self.song_name_label, self.play_progress_bar, self.volume_slider, self.play_and_pause_button, self.loop_button, self.skip_button, self.volume_label]

        self.button_highlight_stylesheet = button_highlight()

        self.song_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.song_name_label.setObjectName("song_label")

        self.play_progress_bar.setRange(0, 10000)
        self.play_progress_bar.setValue(0)
        self.play_progress_bar.setObjectName("play_slider")
        self.play_progress_bar.setTextVisible(False)

        self.volume_slider.setRange(0, 10)
        self.volume_slider.setValue(8)
        self.volume_slider.setFixedWidth(70)
        self.volume_slider.setObjectName("volume_slider")
        self.volume_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.volume_label.setMaximumHeight(60)
        volume_widget: QWidget = QWidget()
        volume_layout: QGridLayout = QGridLayout(volume_widget)
        volume_layout.addWidget(self.volume_slider, 0, 0)
        volume_layout.addWidget(self.volume_label, 1, 0)
        volume_layout.setSpacing(0)
        volume_layout.setContentsMargins(0, 0, 0, 0)
        volume_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        volume_widget.setObjectName("volume_widget")
        volume_widget.setFixedWidth(70) #same as volume slider



        def widget_size_setup(widget: QWidget) -> None:
            widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        [widget_size_setup(widget) for widget in [self.song_name_label, self.play_progress_bar, self.play_and_pause_button, self.loop_button, self.skip_button, self.volume_slider]]

        self.layout.addWidget(self.song_name_label, 0, 0, 1, -1)
        self.layout.addWidget(self.play_progress_bar, 1, 0, 1, -1)
        self.layout.addWidget(self.skip_button, 2, 0, 1, 1)
        self.layout.addWidget(self.loop_button, 2, 1, 1, 1)
        self.layout.addWidget(self.play_and_pause_button, 2, 2, 1, 1)
        self.layout.addWidget(volume_widget, 2, 3, 1, 1)

        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 2)
        self.layout.setRowStretch(2, 5)
        self.layout.setColumnStretch(0, 3)
        self.layout.setColumnStretch(1, 3)
        self.layout.setColumnStretch(2, 8)
        self.layout.setColumnStretch(3, 1)

        #self.layout.setContentsMargins(50, 30, 50, 30)
        self.layout.setContentsMargins(50, 15, 50, 15)
        self.layout.setHorizontalSpacing(35)
        self.layout.setVerticalSpacing(20)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        super().setMaximumHeight(c.PLAYBAR_MAX_HEIGHT)
        super().setMinimumHeight(c.PLAYBAR_MINIMUM_HEIGHT)

    def link_to_mixer(self, function_dict: dict[str, Callable[[], None]]) -> None:
        def play_func() -> None:
            function_dict["play/pause"]()
            if self.play_and_pause_button.styleSheet() == "":
                self.play_and_pause_button.setStyleSheet(self.button_highlight_stylesheet)
            else:
                self.play_and_pause_button.setStyleSheet("")
        
        self.play_and_pause_button.clicked.connect(play_func)

        def skip_func() -> None:
            function_dict["skip"]()
            if self.play_and_pause_button.styleSheet() == "":
                self.play_and_pause_button.setStyleSheet(self.button_highlight_stylesheet) #skip unpauses

        self.skip_button.clicked.connect(skip_func)

        self.volume_slider.valueChanged.connect(function_dict["volume_adjust"])

        def loop_func() -> None:
            function_dict["loop"]()
            if self.loop_button.styleSheet() == "":
                self.loop_button.setStyleSheet(self.button_highlight_stylesheet)
            else:
                self.loop_button.setStyleSheet("")
        
        self.loop_button.clicked.connect(loop_func)
        

    def update_song_name_label(self, new_name: str) -> None:
        self.song_name_label.setText(new_name)