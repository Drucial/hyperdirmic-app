from hyperdirmic.app import start_watcher
from hyperdirmic.tray import run_tray_app
import threading
import logging

logger = logging.getLogger(__name__)

def main():
    logger.info("🚀 Hyperdirmic started.")
    # Start the file watcher in a background thread
    watcher_thread = threading.Thread(target=start_watcher, daemon=True)
    watcher_thread.start()

    # Start the tray icon on the main thread
    run_tray_app()

if __name__ == "__main__":
    main()
