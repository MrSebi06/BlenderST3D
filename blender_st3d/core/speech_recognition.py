from fuzzywuzzy import process

import speech_recognition as sr

COMMANDS = ["extrude", "change microphone", "stop listening"]


def recognize_speech(mic_index, duration=5):
    recognizer = sr.Recognizer()
    microphone_list = sr.Microphone.list_microphone_names()
    if microphone_list and mic_index < len(microphone_list):
        microphone_name = microphone_list[mic_index]
        print(f"Using microphone: {microphone_name}")
        with sr.Microphone(device_index=mic_index) as source:
            print("Say a command!")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=duration)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

            # Find the closest matching command
            closest_match = process.extractOne(text.lower(), COMMANDS)
            if closest_match and closest_match[1] > 70:  # Threshold for matching
                print(f"Interpreted as: {closest_match[0]}")
                return closest_match[0], microphone_name
            else:
                print("Could not match the command to any known commands.")
                return "", microphone_name

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    else:
        print("Invalid microphone index")
    return "", "No microphone"
