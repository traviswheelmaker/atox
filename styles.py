import constants as c

#NOTES
#Sidebar highlighting was done within the sidebar file, so we define that separately
def main() -> str:
    
    #{'{'} {'}'}
    stylesheet: str = f"""
    QWidget {'{'} 
        font-size: 20px;
    {'}'}
    
    QWidget#main_widget {'{'} 
        background-color: {c.BACKGROUND_COLOR}
    {'}'}

    QPushButton {'{'} 
        background-color: {c.MAIN_COLOR};
        border: 4px solid {c.ACCENT_COLOR};
        border-radius: 20px;
    {'}'}

    QPushButton::hover {'{'}
        background-color: {c.MAIN_COLOR_SAT};
    {'}'}

    QPushButton::pressed {'{'}
        background-color: {c.MAIN_COLOR_DARK};
    {'}'}

    QSlider::groove {'{'} 
        background-color: {c.DARK_COLOR};
    {'}'}

    QSlider::handle {'{'} 
        background-color: {c.ACCENT_COLOR_SAT};
        height: 10px;
        border: 2px solid {c.ACCENT_COLOR_DARK};
    {'}'}

    QSlider::add-page:vertical {'{'} 
        background-color: {c.MAIN_COLOR};
        border: 4px solid {c.ACCENT_COLOR};
        border-top: 0px;
    {'}'}

    QSlider::sub-page:vertical {'{'} 
        background-color: {c.DARK_COLOR};
        border: 4px solid {c.ACCENT_COLOR};
        border-bottom: 0px;
    {'}'}
    
    QWidget#volume_widget {'{'} 
        background-color: {c.MAIN_COLOR_SAT};
        border: 2px solid {c.ACCENT_COLOR};
    {'}'}

    QProgressBar {'{'} 
        border: 4px solid {c.ACCENT_COLOR};
        border-radius: 10px;
        background-color: {c.DARKER_COLOR};
    {'}'}

    QProgressBar::chunk {'{'} 
        background-color: {c.HIGHLIGHT_COLOR};
        border: 1px solid {c.HIGHLIGHT_COLOR};
        border-radius: 5px;
    {'}'}
    
    QPushButton#sidebar_button {'{'}
        border-radius: 30px;
    {'}'}

    QLabel#song_label {'{'} 
        background-color: {c.MAIN_COLOR_SAT};
        border: 3px solid {c.ACCENT_COLOR};
        border-radius: 5px;
    {'}'}

    QLabel#playview_label {'{'} 
        background-color: {c.DARK_COLOR};
        border: 2px solid {c.ACCENT_COLOR};
        border-radius: 5px;
    {'}'}

    QWidget#playlist_button_holder {'{'} 
        background-color: {c.BACKGROUND_COLOR};
        border: 2px solid {c.ACCENT_COLOR};
        border-radius: 2px;
    {'}'}

    QScrollArea#playlist_scroll {'{'} 
        background-color: {c.DARK_COLOR};
        border: 2px solid {c.ACCENT_COLOR};
        border-radius: 2px;
    {'}'}
    """ 
    return stylesheet

#this is applied within the sidebar file, separately
def button_highlight() -> str:
    #{'{'} {'}'}
    stylesheet: str = f"""
    border-color: {c.HIGHLIGHT_COLOR}
    """
    return stylesheet

