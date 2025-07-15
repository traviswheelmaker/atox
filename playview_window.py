from PySide6.QtWidgets import QPushButton, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy
from PySide6.QtCore import Qt
import constants as c



class playView(QWidget):
    def __init__(self):
        super().__init__()
        self.layout: QVBoxLayout = QVBoxLayout(self)

        #temp qlabels used as stacked widgets
        self.playlist_label: QLabel = QLabel("Total Song Library (Default)")
        self.play_order_widget = QWidget()
        self.play_order_layout = QVBoxLayout(self.play_order_widget)

        self.song_labels_list: list[QLabel] = []

        def row_setup(index: str) -> QLabel:
            row_widget: QWidget = QWidget()
            row_layout: QHBoxLayout = QHBoxLayout(row_widget)

            index_label: QLabel = QLabel(f"{index}")
            index_label.setFixedWidth(60)
            index_label.setAlignment(Qt.AlignmentFlag.AlignCenter)


            song_label: QLabel = QLabel()

            row_layout.addWidget(index_label)
            row_layout.addWidget(song_label)

            row_layout.setSpacing(5)
            #row_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)



            index_label.setObjectName("playview_label")
            song_label.setObjectName("playview_label")

            self.play_order_layout.addWidget(row_widget)
            self.song_labels_list.append(song_label)
        
        row_setup("Now")
        [row_setup(i) for i in range(1, 10)]


        self.widget_list: list[QWidget] = [self.playlist_label, self.play_order_widget]
    
        [self.layout.addWidget(widget) for widget in self.widget_list]

        self.layout.setSpacing(10)
        self.play_order_layout.setSpacing(0)

    
    def update_play_order(self, new_play_order: list[str]) -> None:
        [widget.setText(song) for widget, song in zip(self.song_labels_list, new_play_order)]
