from PySide6.QtWidgets import QPushButton, QLabel, QWidget, QVBoxLayout, QSizePolicy
from collections.abc import Callable
from styles import button_highlight

import constants as c
import styles as styles


class sidebar(QWidget):
    def __init__(self, sidebar_names_list: list[str]):
        super().__init__()
        self.layout: QVBoxLayout = QVBoxLayout(self)

        self.sidebar_highlight_stylesheet: str = button_highlight()

        self.widget_list: list[QWidget] = []
        for name in sidebar_names_list:
            widget = QPushButton(name)
            widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            widget.setObjectName("sidebar_button") #for css
            self.widget_list.append(widget)
            self.layout.addWidget(widget)

        self.selected_button_index: int = 0
        self.widget_list[0].setStyleSheet(self.sidebar_highlight_stylesheet)


        super().setMaximumWidth(c.SIDEBAR_MAX_WIDTH)
        self.layout.setSpacing(40)
        self.layout.setContentsMargins(20, 50, 10, 10)
    
    def link_to_window(self, func: Callable[[int], None]) -> None:
        def connect_widget(widget: QWidget, i: int) -> None:
            def function_to_connect() -> None:
                func(i)
                self.widget_list[self.selected_button_index].setStyleSheet("")
                widget.setStyleSheet(self.sidebar_highlight_stylesheet)
                self.selected_button_index = i

            widget.clicked.connect(function_to_connect)
        [connect_widget(widget, i) for i, widget in enumerate(self.widget_list)]




