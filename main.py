from ytmusicapi import YTMusic
import subprocess
import os
import time
import sys
import json


def main():
    if not os.path.exists("oauth.json"):
        print("""Hi there, looks like it's your first time, or your log in expired.
You'll be redirected to Google's website to log in, and then we can get started!""")
        time.sleep(3)
        try:
            subprocess.run(["ytmusicapi", "oauth"])
        except Exception:
            print("Sorry, we couldn't log you in. Make sure you installed ytmusicapi.")
            sys.exit()

    yt = YTMusic("oauth.json")

    def get_user_details():
        try:
            with open('user_data.json', 'r') as file:
                user_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            user_data = {}
            user_name = input("I don't think we've met. What's your name? ")
            user_data['name'] = user_name
            with open('user_data.json', 'w') as file:
                json.dump(user_data, file)
        return user_data

    user_data = get_user_details()
    print(f"Hey there, {user_data['name']}! Ready for some music?")


if __name__ == "__main__":
    main()
