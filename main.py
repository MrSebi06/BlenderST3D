import bpy
import speech_recognition as sr
import pyaudio
import json
import os

CONFIG_FILE = "microphone_config.json"


def list_microphones():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    microphones = []
    for i in range(0, numdevices):
        if p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels') > 0:
            microphones.append((i, p.get_device_info_by_host_api_device_index(0, i).get('name')))
    return microphones


def save_microphone_config(mic_index):
    config = {"microphone_index": mic_index}
    with open(CONFIG_FILE, 'w') as config_file:
        json.dump(config, config_file)
    print(f"Microphone index {mic_index} saved to {CONFIG_FILE}")


def load_microphone_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as config_file:
            config = json.load(config_file)
            return config.get("microphone_index", None)
    return None


def recognize_speech(mic_index):
    recognizer = sr.Recognizer()
    microphone_list = sr.Microphone.list_microphone_names()
    if microphone_list and mic_index < len(microphone_list):
        microphone_name = microphone_list[mic_index]
        print(f"Using microphone: {microphone_name}")
        with sr.Microphone(device_index=mic_index) as source:
            print("Say a command!")
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower(), microphone_name  # Return the recognized text and microphone name
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    else:
        print("Invalid microphone index")
    return "", "No microphone"


def extrude_function():
    print("Extrude function called")


def execute_command(command):
    if "extrude" in command:
        extrude_function()
    else:
        print("Command not recognized")


def main():
    print()
    print("Available microphones:")
    microphones = list_microphones()
    for i, mic in microphones:
        print(f"{i}: {mic}")
    print()
    mic_index = load_microphone_config()
    if mic_index is not None:
        print(f"Loaded microphone index from config: {mic_index}")
        print()
    else:
        try:
            mic_index = int(input("Enter the index of the microphone you want to use: "))
            print()
            save_microphone_config(mic_index)
        except ValueError:
            print("Invalid input. Using default microphone.")
            print()
            mic_index = 0

    command, mic_name = recognize_speech(mic_index)
    print(f"Microphone used: {mic_name}")
    print()
    execute_command(command)


if __name__ == "__main__":
    main()
