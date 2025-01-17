﻿import json
import os

CONFIG_DIR = os.path.join(os.getenv("APPDATA"), "BlenderST3D")
CONFIG_FILE = os.path.join(CONFIG_DIR, "microphone_config.json")


def ensure_config_dir_exists():
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)


def save_microphone_config(mic_index):
    ensure_config_dir_exists()
    config = {"microphone_index": mic_index}
    with open(CONFIG_FILE, "w") as config_file:
        json.dump(config, config_file)
    print(f"Microphone index {mic_index} saved to {CONFIG_FILE}")


def load_microphone_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as config_file:
            config = json.load(config_file)
            return config.get("microphone_index", None)
    return None
