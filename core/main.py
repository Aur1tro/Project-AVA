from speech.listener import listen #Listening Ability
from speech.speaker import speak #Speaking Ability
from memory.memory import save_memory, recall_memory #Memory Handler
from skills.music import play_local, pause_local, next_track #Music Controls
from skills.weather_parser import extract_city #Weather Parsing
from skills.weather import get_weather, get_forecast #Weather status and forecasting

import time

WAKE_WORDS = ["ava", "eva", "ever"]
EXIT_WORDS = ["stop", "exit", "shutdown", "bye"]

def main():
    speak("AVA is online.")
    print("AVA is ONLINE")

    try:
        while True:
            command = listen()
            print("Heard:", command)

            # Ignore recognition errors
            if not command or command.startswith("["):
                continue

            command_lower = command.lower()

            # Require wake word
            if not any(wake in command_lower for wake in WAKE_WORDS):
                continue

            # Remove wake words
            cleaned_command = command_lower
            for wake in WAKE_WORDS:
                cleaned_command = cleaned_command.replace(wake, "")
            cleaned_command = cleaned_command.strip()

            # ---- MUSIC CONTROLS ----
            if "play" in cleaned_command:
                speak("Playing music on this device.")
                play_local()
                continue

            if "pause" in cleaned_command:
                speak("Pausing music.")
                pause_local()
                continue

            if "next" in cleaned_command:
                speak("Skipping track.")
                next_track()
                continue

            # ---- EXIT ----
            if cleaned_command in EXIT_WORDS:
                speak("Shutting down.")
                break

            #Weather Part Start
            if "weather" in cleaned_command:
                city = extract_city(cleaned_command)
                weather = get_weather(city)

                if weather:
                    speak(weather)
                else:
                    speak("I couldn't get the weather right now.")

                continue

            if "forecast" in cleaned_command:
                city = extract_city(cleaned_command)
                forecast = get_forecast(city)

                if forecast:
                    speak(forecast)
                else:
                    speak("I couldn't get the forecast right now.")

                continue

            #Weather End

            # ---- MEMORY RECALL ----
            if "what do you remember" in cleaned_command:
                memories = recall_memory()
                if not memories:
                    speak("I don't remember anything yet.")
                else:
                    speak("Here is what I remember.")
                    for memory in memories:
                        speak(memory.strip())
                continue

            # ---- MEMORY SAVE (statements only) ----
            if (
                cleaned_command
                and len(cleaned_command.split()) > 2
                and not cleaned_command.endswith("?")
            ):
                save_memory(cleaned_command)
                speak("I will remember that.")

            time.sleep(0.3)

    except KeyboardInterrupt:
        print("Keyboard interrupt received. Exiting AVA.")
        speak("Shutting down.")
        time.sleep(0.5)

if __name__ == "__main__":
    main()
