from ytmusicapi import YTMusic
import curses
import time

class Item:
    def __init__(self, y, item, output, window, j):
        self.title = item['title']
        self.length = len(self.title)
        try:
            self.artists = [item['artists'][i]['name'] for i, artist in enumerate(item['artists'])]
        except KeyError:
            self.artists = None

        


class Category:
    def __init__(self, category, i, output, window):
        self.y = 3*i
        self.title = category['title']
        window.addstr(self.y, 5, self.title, curses.A_STANDOUT)
        self.items = [Item(self.y, item, output, window, j) for j, item in enumerate(category['contents'])]
        


def home_page(yt, window):
    output = yt.get_home()
    categories = [Category(category, i, output, window) for i, category in enumerate(output)]



