import os
import shutil
from pathlib import Path
# from win10toast import ToastNotifier


documents = ['pdf', 'doc', 'docx', 'txt', 'pptx', 'csv']
images = ['jpg', 'jpeg', 'png', 'ico']
compressed = ['zip', 'rar', 'bz2', '7z']
videos = ['mp4', 'mkv']
music = ['mp3', 'm3u8']
setup = ['exe', 'msi']
iso = ['iso']
key = ['pem', 'ppk']
shortcuts = ["lnk"]
# toaster = ToastNotifier()


def movefiles(srcpath, file, foldername):
    """Utility Function to move files"""
    print(srcpath, file, foldername)

    # # Make Sure the path exists
    Path(os.path.join(srcpath, foldername)).mkdir(exist_ok=True)

    move_from = os.path.join(srcpath, file)
    move_to = os.path.join(srcpath, foldername)
    shutil.move(move_from, move_to)


def segragete(srcpath):
    """Specify the path to be segregated"""
    print(srcpath)
    try:
        for file in os.listdir(srcpath):

            if os.path.isfile(os.path.join(srcpath, file)):

                """"Reversing File String to get last ."""
                fileReverse = file[::-1].split(".")[0]

                """Reversing the extension back to correct"""
                fileReverse = fileReverse[::-1].lower()

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
                elif fileReverse in shortcuts:
                    movefiles(srcpath, file, "Shortcut's")
                else:
                    movefiles(srcpath, file, "Others")
                return True
    except Exception as e:
        print(e)
        print("Failed !")
        return False
        # toaster.show_toast("Status", "Segregation failed")
    # finally:
        # print("Segregation Comlete")
        # toaster.show_toast("Status", "Segregation completed successfully")


"""Edit main path accordingly"""
# mainPath = "/home/paritosh/PycharmProjects/test_downloads"

# Nakul main path
mainPath = "c://Users//nakul//Desktop//android"

# give any path you want
# segragete(mainPath)
