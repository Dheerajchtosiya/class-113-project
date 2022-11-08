import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = r"C:\Users\chito\OneDrive\Desktop\python\class 113"
to_dir = r"C:\Users\chito\OneDrive\Desktop\python\class 113"



class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print("file created!!!!")
    def on_deleted(self, event):
        print("oh! a file deleted!!!")
    def on_modified(self, event):
        print("oh there is some change!!!!!")
    def on_moved(self, event):
        print("something moved!!")

    

    

event_handler = FileMovementHandler()



observer = Observer()


observer.schedule(event_handler, from_dir, recursive=True)


observer.start()

while True:
    time.sleep(2)
    print("running...")

    