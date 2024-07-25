import pyaudio

from blender_st3d.config import save_microphone_config


def list_microphones():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get("deviceCount")
    microphones = []
    for i in range(0, numdevices):
        if p.get_device_info_by_host_api_device_index(0, i).get("maxInputChannels") > 0:
            microphones.append(
                (i, p.get_device_info_by_host_api_device_index(0, i).get("name"))
            )
    return microphones


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
