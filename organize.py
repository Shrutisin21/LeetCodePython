import os
import pathlib

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickCategory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if value == suffix:
                return category


def organizeDirectory():
    for item in os.scandir():
        print item

##print(pickCategory('.pdf'))
organizeDirectory()


