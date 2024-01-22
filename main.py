from ytmusicapi import YTMusic
import subprocess
import os
import time
import sys
import json
import curses
from curses import wrapper
from curses.textpad import Textbox



# YT OAuth Workflow
if not os.path.exists("oauth.json"):
    print("""Hi there, looks like it's your first time, or your log in expired.
You'll be redirected to Google's website to log in, and then we can get started!""")
    time.sleep(3)
    try:
        subprocess.run(["ytmusicapi", "oauth"])
    except:
        print("Sorry, we couldn't log you in. Make sure you installed ytmusicapi.")
        sys.exit()


def main(window):

    # Init de YT Music
    yt = YTMusic("oauth.json")

    # Init de curses
    curses.noecho()
    curses.cbreak()
    window.keypad(True)

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
            window.addstr(y, x, text, curses.A_STANDOUT)
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


wrapper(main)
