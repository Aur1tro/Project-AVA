from speech.listener import listen
from speech.speaker import speak
import time

def main():
    speak("AVA is online.")
    print("AVA is ONLINE")

    while True:
        command = listen()
        print("You said:", command)

        if command.startswith("["):
            continue

        time.sleep(0.4)   # allow mic to fully release
        speak(command)    # say EXACTLY what you said
        time.sleep(0.4)

if __name__ == "__main__":
    main()
