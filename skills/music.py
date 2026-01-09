import pyautogui
import time
import os

def play_local():
    """
    Opens Spotify (if not already open) and toggles play/pause.
    """
    try:
        os.startfile("spotify")
        time.sleep(3)  # give Spotify time to open
    except Exception:
        pass

    pyautogui.press("playpause")

def pause_local():
    """
    Pauses music (toggle).
    """
    pyautogui.press("playpause")

def next_track():
    """
    Skips to next track.
    """
    pyautogui.press("nexttrack")

def previous_track():
    """
    Goes to previous track.
    """
    pyautogui.press("prevtrack")
