# src/hyperdirmic/tray.py
import rumps


class HyperdirmicApp(rumps.App):
    def __init__(self):
        super().__init__("Hyperdirmic", icon=None, quit_button=None)
        self.menu = ["Quit Hyperdirmic"]

    @rumps.clicked("Quit Hyperdirmic")
    def quit_app(self, _):
        rumps.quit_application()


def run_tray_app():
    HyperdirmicApp().run()
