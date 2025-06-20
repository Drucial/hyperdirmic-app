from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

from hyperdirmic.utils import get_destination_folder, safe_move_file, is_temp_file, logger

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

    def on_moved(self, event):
        if not event.is_directory:
            file_path = Path(event.dest_path)
            if is_temp_file(file_path):
                logger.info(f"⏳ Skipping moved temp file: {file_path.name}")
                return
            
            # Check if the file is already in its correct destination
            dest_folder = get_destination_folder(file_path)
            if file_path.parent.resolve() == dest_folder.resolve():
                logger.info(f"✅ File {file_path.name} already in correct location, skipping")
                return
                
            logger.info(f"📦 Detected file move/rename: {file_path.name}")
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
