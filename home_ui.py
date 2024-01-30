from ytmusicapi import YTMusic
import curses

class HomePage():
    def __init__(self, yt, window):

        output = yt.get_home()
        for i, category in enumerate(output):
            title = output[i]['title']
            window.addstr(i, 5, title, curses.A_STANDOUT)

def home_ui(yt, window):
    home_page = HomePage(yt, window)

