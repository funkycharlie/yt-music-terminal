from ytmusicapi import YTMusic
import subprocess
import os
import time
import sys
import json
import curses
from curses import wrapper
from curses.textpad import Textbox
from menu import home


if not os.path.exists("oauth.json"):
    print("""Hi there, looks like it's your first time, or your log in expired.
You'll be redirected to Google's website to log in, and then we can get started!""")
    time.sleep(3)
    try:
        subprocess.run(["ytmusicapi", "oauth"])
    except:
        print("Sorry, we couldn't log you in. Make sure you installed ytmusicapi.")
        sys.exit()


def print_center(window, text):
    window.clear()
    h, w = window.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    window.addstr(y, x, text, curses.color_pair(2))
    window.refresh()


def main(window):

    yt = YTMusic("oauth.json")

    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    window.keypad(True)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
    color_pairs = (curses.color_pair(1),
                   curses.color_pair(2))
    window.bkgd(' ', curses.color_pair(2) | curses.A_BOLD)

    def get_user_details():
        try:
            with open('user_data.json', 'r') as file:
                user_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            user_data = {}
            h, w = window.getmaxyx()
            text = "I don't think we've met. What's your name?"
            x = w // 2 - len(text) // 2
            y = h // 2
            window.addstr(y, x, text, curses.color_pair(2))
            namewin = curses.newwin(1, len(text), y + 4, x)
            window.refresh()
            box = Textbox(namewin)
            box.edit()
            user_name = box.gather()
            user_data['name'] = user_name
            with open('user_data.json', 'w') as file:
                json.dump(user_data, file)
        return user_data

    user_data = get_user_details()
    print_center(window, f"Hey there, {user_data['name']}! Ready for some music?")
    time.sleep(2)
    home(window, user_data, color_pairs, yt)

if __name__ == "__main__":
    wrapper(main)
