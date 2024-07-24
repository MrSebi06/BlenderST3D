import bpy
import speech_recognition as sr
import pyaudio


def list_microphones():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    microphones = []
    for i in range(0, numdevices):
        if p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels') > 0:
            microphones.append((i, p.get_device_info_by_host_api_device_index(0, i).get('name')))
    return microphones


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
    microphones = list_microphones()
    print("Available microphones:")
    for i, mic in microphones:
        print(f"{i}: {mic}")

    try:
        mic_index = int(input("Enter the index of the microphone you want to use: "))
    except ValueError:
        print("Invalid input. Using default microphone.")
        mic_index = 0

    while True:
        command, mic_name = recognize_speech(mic_index)
    
    print(f"Microphone used: {mic_name}")
    execute_command(command)


if __name__ == "__main__":
    main()