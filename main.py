"""This file is for test coding and checking output of different libraries"""

# from win10toast import ToastNotifier
# import os
# toaster = ToastNotifier()
# toaster.show_toast("Sample Notification","Python is awesome!!!")
# print(os.getcwd())
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()
print(file_path)
