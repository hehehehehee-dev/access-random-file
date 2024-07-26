import sys
import os
import random
import numpy as np
import subprocess

def get_files_in_directory(directory):
    file_paths = []
    for entry in os.listdir(directory):
        file_path = os.path.join(directory, entry)
        file_paths.append(file_path)
    return file_paths

def open_file(path):
    if sys.platform.startswith('darwin'):  # macOS
        subprocess.run(['open', path])
    elif sys.platform.startswith('win'):  # Windows
        subprocess.run(['explorer', path], check=True)
    elif sys.platform.startswith('linux'):  # Linux
        subprocess.run(['xdg-open', path])
    else:
        print(f"Unsupported platform: {sys.platform}")

directory = os.path.dirname(os.path.realpath(__file__))
file_paths = get_files_in_directory(directory)
path = random.choice(file_paths)
path = os.path.normpath(path)
print(path)
open_file(path)