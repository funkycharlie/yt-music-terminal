from ytmusicapi import YTMusic
import time
import curses
from home_ui import home_page

global navs

navs = ["Home", "Explore", "Search", "Library"]

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

    def select(self, buttons):
        for button in buttons:
            if button.selected:
                button.deselect()
        self.window.addstr(self.y, self.x, ' ' * self.length)
        self.window.addstr(self.y, self.x, self.name, curses.A_STANDOUT)
        self.selected = True
        
    
    def deselect(self):
        self.window.addstr(self.y, self.x, ' ' * self.length)
        self.window.addstr(self.y, self.x, self.name)
        self.selected = False

def home(window, user_data, color_pairs, yt):

    window.clear()
    buttons = [NavButton(window, len(nav), nav, id, navs, 20) for id, nav in enumerate(navs)]
    selected_button = buttons[0]
    selected_button.select(buttons)

    # This is where the code goes for the home ui
    home_page(yt, window)
    window.refresh()

    input_key = window.getkey()

    if input_key == "KEY_LEFT":
        library(window, buttons, user_data, color_pairs, yt)

    elif input_key == "KEY_RIGHT":
        explore(window, buttons, user_data, color_pairs, yt)

def explore(window, buttons, user_data, color_pairs, yt):

    window.clear()

    # Creates NavButton objects for each string in navs.
    buttons = [NavButton(window, len(nav), nav, id, navs, 20) for id, nav in enumerate(navs)]
    selected_button = buttons[1]
    selected_button.select(buttons)

    window.addstr(0, 0, "explore")
    window.refresh()
    
    input_key = window.getkey()

    if input_key == "KEY_LEFT":
        home(window, user_data, color_pairs, yt)
    elif input_key == "KEY_RIGHT":
        search(window, buttons, user_data, color_pairs, yt)

def search(window, buttons, user_data, color_pairs, yt):

    window.clear()
    buttons = [NavButton(window, len(nav), nav, id, navs, 20) for id, nav in enumerate(navs)]
    selected_button = buttons[2]
    selected_button.select(buttons)

    window.addstr(0, 0, "search")
    window.refresh()

    
    input_key = window.getkey()

    if input_key == "KEY_LEFT":
        explore(window, buttons, user_data, color_pairs, yt)
    elif input_key == "KEY_RIGHT":
        library(window, buttons, user_data, color_pairs, yt)



def library(window, buttons, user_data, color_pairs, yt):
    
    window.clear()
    buttons = [NavButton(window, len(nav), nav, id, navs, 20) for id, nav in enumerate(navs)]
    selected_button = buttons[3]
    selected_button.select(buttons)

    window.addstr(0, 0, "library")
    window.refresh()

    input_key = window.getkey()

    if input_key == "KEY_LEFT":
        search(window, buttons, user_data, color_pairs, yt)
    elif input_key == "KEY_RIGHT":
        home(window, user_data, color_pairs, yt)

