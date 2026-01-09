def extract_city(command: str, default_city="Jamshedpur"):
    command = command.lower()

    triggers = [
        "weather in",
        "forecast in",
        "weather for",
        "forecast for"
    ]

    stop_words = [
        "today",
        "tomorrow",
        "now",
        "right now",
        "please"
    ]

    for trigger in triggers:
        if trigger in command:
            city = command.split(trigger)[-1].strip()

            for word in stop_words:
                city = city.replace(word, "")

            city = city.strip()

            if city:
                return city.title()

    return default_city
