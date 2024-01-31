from ytmusicapi import YTMusic
import curses

class Item:
    def __init__(self, item, output, window):
        self.title = item['title']
        self.artists = [item['artists'][i]['name'] for i, artist in enumerate(item['artists'])]
        

class Category:
    def __init__(self, category, i, output, window):
        self.title = category['title']
        window.addstr(3*i, 5, self.title, curses.A_STANDOUT)
        self.items = [Item(item, output, window) for j, item in enumerate(category['contents'])]
        


def home_page(yt, window):
    output = yt.get_home()
    categories = [Category(category, i, output, window) for i, category in enumerate(output)]




