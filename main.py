from microphone import list_microphones, recognize_speech, change_microphone
from config import load_microphone_config, save_microphone_config
from commands import execute_command


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

    while True:
        command, mic_name = recognize_speech(mic_index, duration=5)
        print()
        if command == "stop listening":
            print("Stopping the program.")
            break
        elif command:
            mic_index = execute_command(command, mic_index)
        else:
            print('Please repeat or say "stop listening" for the program to stop.')
            print()


if __name__ == "__main__":
    main()