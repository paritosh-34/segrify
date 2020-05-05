import os
import shutil
from pathlib import Path

documents = ['pdf', 'doc', 'docx', 'txt']
images = ['jpg', 'jpeg', 'png', 'ico']
compressed = ['zip', 'rar', 'bz2']
videos = ['mp4', 'mkv']
music = ['mp3', 'm3u8']


def movefiles(srcpath, file, foldername):
    """Utility Function to move files"""
    print(srcpath, file, foldername)

    # Make Sure the path exists
    Path(os.path.join(srcpath, foldername)).mkdir(exist_ok=True)

    move_from = os.path.join(srcpath, file)
    move_to = os.path.join(srcpath, foldername)
    shutil.move(move_from, move_to)


def segragete(srcpath):
    """Specify the path to be segregated"""
    for file in os.listdir(srcpath):
        if os.path.isfile(os.path.join(srcpath, file)):
            if file.split(".")[1] in documents:
                movefiles(srcpath, file, "Documents")
            elif file.split(".")[1] in images:
                movefiles(srcpath, file, "Images")
            elif file.split(".")[1] in compressed:
                movefiles(srcpath, file, "Compressed")
            elif file.split(".")[1] in music:
                movefiles(srcpath, file, "Music")
            elif file.split(".")[1] in videos:
                movefiles(srcpath, file, "Videos")
            else:
                movefiles(srcpath, file, "Others")


# The parent directory of this file
parent_dir = os.getcwd()
# The folder that is to be segregated in this directory
folder_to_be_segregated = "testing_folder"

# Use path.join to work on all OS's
srcpath = os.path.join(parent_dir, folder_to_be_segregated)

# give any path you want
segragete(srcpath)
