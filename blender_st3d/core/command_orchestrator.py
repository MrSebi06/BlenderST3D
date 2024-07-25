from blender_st3d.core.blender_commands import extrude_function
from blender_st3d.core.microphone import change_microphone


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
