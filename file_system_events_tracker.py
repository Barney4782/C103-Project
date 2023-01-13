import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/Arnel/Downloads/From2"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"The file {event.src_path} has been created!")
    
    def on_deleted(self, event):
        print(f"Someone has deleted {event.src_path}")
    
    def on_modified(self, event):
        print(f"The file {event.src_path} has been modified!")
    
    def on_moved(self, event):
        print(f"The file {event.src_path} has been moved or renamed!")
    
eventHandler = FileEventHandler()

observer = Observer()

observer.schedule(eventHandler, from_dir, recursive= True)

observer.start()

try:
    while True:
        time.sleep(1)
        print("running...")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()

