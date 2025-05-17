from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw
import sys
import threading
import logging


def _create_icon_image():
    # Creates a basic 64x64 icon
    img = Image.new("RGB", (64, 64), color=(60, 60, 60))
    draw = ImageDraw.Draw(img)
    draw.rectangle([20, 20, 44, 44], fill=(255, 255, 255))
    return img


def _on_quit(icon, item):
    icon.stop()
    logging.info("👋 Hyperdirmic exited via tray menu.")
    print("👋 Hyperdirmic exiting.")
    # If running in a thread, we want to stop the full app too
    threading.Thread(target=sys.exit, args=(0,), daemon=True).start()


def run_tray_app():
    icon = Icon("Hyperdirmic")
    icon.icon = _create_icon_image()

    icon.menu = Menu(
        MenuItem("Quit Hyperdirmic", _on_quit)
    )

    print("🧹 Tray icon running.")
    icon.run()
