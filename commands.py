from microphone import change_microphone

def extrude_function():
    print("Extrude function called")

def execute_command(command, current_mic_index):
    if "extrude" in command:
        extrude_function()
    elif "change microphone" in command:
        current_mic_index = change_microphone()
    else:
        print("Command not recognized")
    return current_mic_index
