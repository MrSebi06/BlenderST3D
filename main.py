import bpy

import speech_recognition as sr
import pyaudio

import json
import os

CONFIG_FILE = "microphone_config.json"


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


def extrude_function():
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            with bpy.context.temp_override(area=area):
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.wm.tool_set_by_id(name="builtin.extrude_region")


def execute_command(command, current_mic_index):
    executed_command = False
    if "extrude" in command:
        extrude_function()
        executed_command = True
    elif "change microphone" in command:
        current_mic_index = change_microphone()
    else:
        print("Command not recognized")
    return current_mic_index, executed_command


def list_microphones():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    microphones = []
    for i in range(0, numdevices):
        if p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels') > 0:
            microphones.append((i, p.get_device_info_by_host_api_device_index(0, i).get('name')))
    return microphones


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
            return text.lower(), microphone_name  # Return the recognized text and microphone name
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    else:
        print("Invalid microphone index")
    return "", "No microphone"


def change_microphone():
    microphones = list_microphones()
    for i, mic in microphones:
        print(f"{i}: {mic}")

    try:
        mic_index = int(input("Enter the index of the microphone you want to use: "))
        save_microphone_config(mic_index)
    except ValueError:
        print("Invalid input. Using default microphone.")
        mic_index = 0

    return mic_index


def main():
    print()
    print("Available microphones:")
    print()
    microphones = list_microphones()

    for i, mic in microphones:
        print(f"{i}: {mic}")
    print()

    mic_index = load_microphone_config()
    if mic_index is not None:
        print(f"Loaded microphone index from config: {mic_index}")
        print()
    else:
        mic_index = change_microphone()

    executed_command = False
    while not executed_command:
        command, mic_name = recognize_speech(mic_index)
        print()
        if command == "stop listening":
            print("Stopping the program.")
            break
        elif command:
            mic_index, executed_command = execute_command(command, mic_index)
        else:
            print('Please repeat or say "stop listening" for the program to stop.')
            print()


if __name__ == "__main__":
    main()
