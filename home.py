from ytmusicapi import YTMusic
import time
import curses

class NavButton():
    def __init__(self, window, length, name, place, navs, padding):
        self.selected = False
        self.window = window
        self.length = length
        self.name = name
        self.place = place
        self.padding = padding
        h, w = self.window.getmaxyx()


        total_length = sum(len(nav) for nav in navs) + padding * (len(navs) - 1)

        start_x = (w - total_length) // 2 + (length + padding) * place

        self.x = start_x
        self.y = h - 1
        self.window.addstr(self.y, self.x, self.name)

    def selected(self, buttons):
        self.window.addstr(self.y, self.x, ' ' * self.length)
        self.window.addstr(self.y, self.x, self.name, curses.A_STANDOUT)
        self.selected = True
        for button in buttons:
            if button.selected:
                button.deselect()
    
    def deselect(self):
        self.window.addstr(self.y, self.x, ' ' * self.length)
        self.window.addstr(self.y, self.x, self.name)
        self.selected = False
        

def home(window, user_data, color_pairs, yt):

    window.clear()

    navs = ["Home", "Explore", "Search", "Library"]

    buttons = [NavButton(window, len(nav), nav, id, navs, 20) for id, nav in enumerate(navs)]

    selected_button = buttons[0]
    selected_button.selected(buttons)

    window.refresh()

    window.getch()

