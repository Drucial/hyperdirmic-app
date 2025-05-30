from setuptools import setup

APP = ["src/organizer.py"]
DATA_FILES = [
    "icon.icns",  # App icon (goes to Resources)
    ("", ["tray_icon.png"]),  # tray_icon.png goes to Resources
    ("", ["src/assets/images/folder_dark.icns"]),  # folder_dark.icns goes to Resources
    # Add more icons here if needed, e.g. ("", ["folder_light.icns"])
]
OPTIONS = {
    "argv_emulation": False,
    "iconfile": "icon.icns",
    "packages": ["rumps", "watchdog", "objc"],
    "includes": [
        "watchdog.observers",
        "watchdog.events",
        "Foundation",
        "AppKit",
        "imp",  # 👈 THIS is the missing piece
    ],
    "plist": {
        "CFBundleName": "Hyperdirmic",
        "CFBundleDisplayName": "Hyperdirmic",
        "CFBundleIdentifier": "com.drew.hyperdirmic",
        "CFBundleVersion": "0.1.0",
        "CFBundleShortVersionString": "0.1.0",
        "LSUIElement": True,  # Hide from Dock
        "NSImageIsTemplate": True,
    },
}


setup(
    app=APP,
    name="Hyperdirmic",
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
