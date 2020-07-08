#  Organize files into different folders based on the file extension.
import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "AUDIO": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png']
}


def pick_directory(value):
    for category, extensions in SUBDIRECTORIES.items():
        for extension in extensions:
            if extension == value:
                return category
    return 'MISC'


print(pick_directory('.pdf'))


def organize_directory():
    for item in os.scandir():
        if Path.is_dir(item):
            continue
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pick_directory(fileType)
        directoryPath = Path(directory)
        if directoryPath.is_dir != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))


organize_directory()
