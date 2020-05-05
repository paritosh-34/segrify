"""This file is for test coding and checking output of different libraries"""

from win10toast import ToastNotifier
import os
toaster = ToastNotifier()
toaster.show_toast("Sample Notification","Python is awesome!!!")
print(os.getcwd())