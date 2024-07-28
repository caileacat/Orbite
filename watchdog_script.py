import os
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RestartHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = None
        self.restart_bot()

    def restart_bot(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
        self.process = subprocess.Popen(["python", self.script])

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"{event.src_path} has been modified. Rebooting Orbite...")
            self.restart_bot()

if __name__ == "__main__":
    script = "main.py"  # Change this if your bot's main file is named differently
    event_handler = RestartHandler(script)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()
    print(f"Watching for changes in {script}...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
