from ytmusicapi import YTMusic
import subprocess
import os
import time
import sys


def main():
    if not os.path.exists("oauth.json"):
        print("""Hi there, looks like it's your first time! 
You'll be redirected to Google's website to log in, and then we can get started.""")
        time.sleep(3)
        try:
            subprocess.run(["ytmusicapi", "oauth"])
        except Exception:
            print("Sorry, we couldn't log you in. Make sure you installed ytmusicapi.")
            sys.exit()

    yt = YTMusic("oauth.json")


if __name__ == "__main__":
    main()
