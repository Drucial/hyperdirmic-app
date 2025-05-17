from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

from hyperdirmic.utils import get_destination_folder, safe_move_file

DOWNLOADS_DIR = Path.home() / "Downloads"


class DownloadsHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        time.sleep(1)
        file_path = Path(event.src_path)

        if not file_path.exists() or file_path.is_dir():
            return

        dest_folder = get_destination_folder(file_path)
        safe_move_file(file_path, dest_folder)


def start_watcher():
    print("📂 Watching Downloads folder...")

    event_handler = DownloadsHandler()
    observer = Observer()
    observer.schedule(event_handler, str(DOWNLOADS_DIR), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
