import os
import shutil
from pathlib import Path

documents = ['pdf', 'doc', 'docx', 'txt', 'pptx', 'csv']
images = ['jpg', 'jpeg', 'png', 'ico', 'PNG']
compressed = ['zip', 'rar', 'bz2', '7z']
videos = ['mp4', 'mkv']
music = ['mp3', 'm3u8']
setup = ['exe', 'msi']
iso = ['iso']
key = ['pem', 'ppk']


def movefiles(srcpath, file, foldername):
    """Utility Function to move files"""
    print(srcpath, file, foldername)

    # # Make Sure the path exists
    Path(os.path.join(srcpath, foldername)).mkdir(exist_ok=True)

    move_from = os.path.join(srcpath, file)
    move_to = os.path.join(srcpath, foldername)
    shutil.move(move_from, move_to)


def segragete(srcpath):
    print(srcpath)
    """Specify the path to be segregated"""

    for file in os.listdir(srcpath):

        if os.path.isfile(os.path.join(srcpath, file)):

            """"Reversing File String to get last ."""
            fileReverse = file[::-1].split(".")[0]

            """Reversing the extension back to correct"""
            fileReverse = fileReverse[::-1]
            
            if fileReverse in documents:
                movefiles(srcpath, file, "Documents")
            elif fileReverse in images:
                movefiles(srcpath, file, "Images")
            elif fileReverse in compressed:
                movefiles(srcpath, file, "Compressed")
            elif fileReverse in music:
                movefiles(srcpath, file, "Music")
            elif fileReverse in videos:
                movefiles(srcpath, file, "Videos")
            elif fileReverse in setup:
                movefiles(srcpath, file, "Setup's")
            elif fileReverse in iso:
                movefiles(srcpath, file, "Iso's")
            else:
                movefiles(srcpath, file, "Others")


# The parent directory of this file
parent_dir = os.getcwd()

# The folder that is to be segregated in this directory
folder_to_be_segregated = "testing_folder"

# Use path.join to work on all OS's
srcpath = os.path.join(parent_dir, folder_to_be_segregated)

"""Edit main path accordingly"""
mainPath = "c:\\Users\\nakul\\Downloads"

# srcpath = parent_dir
# give any path you want
segragete(mainPath)
