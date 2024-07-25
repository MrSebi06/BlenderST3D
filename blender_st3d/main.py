from blender_st3d.core.command_orchestrator import execute_command
from blender_st3d.core.microphone import list_microphones, change_microphone
from blender_st3d.core.speech_recognition import recognize_speech

from config import load_microphone_config


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

    # while True:
    #     command, mic_name = recognize_speech(mic_index, duration=5)
    #     print(f"Microphone used: {mic_name}")

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
