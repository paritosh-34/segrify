import eel
import mainscript as m
import tkinter as tk
from tkinter import filedialog

eel.init("templates")
eel.start("index.html", block=False, size=(600, 600))


@eel.expose
def run(path):
    print(path)
    r = m.segragete(path)
    eel.result(r)


@eel.expose
def selectFolder():
    print("Here")
    root = tk.Tk()
    root.withdraw()

    directory_path = filedialog.askdirectory()
    print(directory_path)


while True:
    eel.sleep(10)

    
