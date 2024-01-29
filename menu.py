from ytmusicapi import YTMusic
import time
import curses
from classes import NavButton


def home(window, user_data, color_pairs, yt):

    navs = ["Home", "Explore", "Search", "Library"]
    

    window.clear()
    buttons = [NavButton(window, len(nav), nav, id, navs, 20) for id, nav in enumerate(navs)]
    selected_button = buttons[0]
    selected_button.select(buttons)

    window.addstr(0, 0, "home")
    window.refresh()

    input_key = window.getkey()

    if input_key == "KEY_LEFT":
        selected_button = buttons[3]
        selected_button.select(buttons)
        library(window, buttons, user_data, color_pairs, yt)

    elif input_key == "KEY_RIGHT":
        selected_button = buttons[1]
        selected_button.select(buttons)
        explore(window, buttons, user_data, color_pairs, yt)

def explore(window, buttons, user_data, color_pairs, yt):

    navs = ["Home", "Explore", "Search", "Library"]

    window.clear()
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

    navs = ["Home", "Explore", "Search", "Library"]

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

    navs = ["Home", "Explore", "Search", "Library"]
    
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

