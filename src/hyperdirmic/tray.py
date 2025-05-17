import os
import sys
import rumps

def get_tray_icon_path():
    if getattr(sys, 'frozen', False):
        # In bundled .app, Python is in Contents/MacOS
        # Resource path is one level up
        return os.path.join(sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.abspath(os.path.join(os.path.dirname(sys.executable), '..', 'Resources')), 'tray_icon.png')
    else:
        # Dev mode → tray_icon.png is in the project root
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'tray_icon.png'))

ICON_PATH = get_tray_icon_path()

class HyperdirmicApp(rumps.App):
    def __init__(self):
        super().__init__("Hyperdirmic", icon=ICON_PATH, quit_button=None)
        self.menu = ["Quit Hyperdirmic"]

    @rumps.clicked("Quit Hyperdirmic")
    def quit_app(self, _):
        rumps.quit_application()

def run_tray_app():
    HyperdirmicApp().run()
