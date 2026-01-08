from speech.listener import listen
from speech.speaker import speak
from memory.memory import save_memory, recall_memory
import time

WAKE_WORDS = ["ava", "eva", "ever"]

def main():
    speak("AVA is online.")
    print("AVA is ONLINE")

    try:
        while True:
            command = listen()
            print("Heard:", command)

            if command.startswith("["):
                continue

            command_lower = command.lower()

            if not any(wake in command_lower for wake in WAKE_WORDS):
                continue

            cleaned_command = command_lower
            for wake in WAKE_WORDS:
                cleaned_command = cleaned_command.replace(wake, "")
            cleaned_command = cleaned_command.strip()

            if cleaned_command in ["stop", "exit", "shutdown", "bye"]:
                speak("Shutting down.")
                break

            if "what do you remember" in cleaned_command:
                memories = recall_memory()
                if not memories:
                    speak("I don't remember anything yet.")
                else:
                    speak("Here is what I remember.")
                    for memory in memories:
                        speak(memory.strip())
                continue

            if cleaned_command and len(cleaned_command.split()) > 2:
                save_memory(cleaned_command)
                speak("I will remember that.")

            time.sleep(0.3)

    except KeyboardInterrupt:
        print("Keyboard interrupt received. Exiting AVA.")
        speak("Shutting down.")
        time.sleep(0.5)

if __name__ == "__main__":
    main()
