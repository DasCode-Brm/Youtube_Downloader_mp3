# Libraries
from time import sleep
import clipboard
import pytube
import keyboard
import os
from getpass import getuser

# obtain name user of windows
user = getuser()
path = rf'C:\Users\{user}\Downloads'

print("Welcome to music downloader, press ctrl+2 for exit ")

while True:

    if keyboard.is_pressed("ctrl+c"):
        text = clipboard.paste()

        try:
            yt = pytube.YouTube(text)
            video = yt.streams.filter(only_audio=True).get_by_itag(251)
            print(f"Starting download: {video}")
            file = video.download(path)
            base, ext = os.path.splitext(file)
            new_file = base + '.mp3'
            os.rename(file, new_file)
            print(f"Done, {new_file}")
            print("--------------------")

        except FileExistsError:
            print("This file is existing")
            print("--------------------")

        except pytube.exceptions.RegexMatchError:
            print("Format the link is not valid")
            sleep(1)
    if keyboard.is_pressed("ctrl+2"):
        print("Thanks for use my program")
        exit()

