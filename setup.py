from setuptools import setup

APP = ['src/organizer.py']
DATA_FILES = ['icon.icns']  # Only if you plan to use it as the app icon
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',  # Comment this out if you're not using a custom icon
    'packages': ['watchdog', 'pystray', 'PIL'],
    'includes': ['watchdog.observers', 'watchdog.events'],
    'plist': {
        'CFBundleName': 'Hyperdirmic',
        'CFBundleDisplayName': 'Hyperdirmic',
        'CFBundleIdentifier': 'com.yourname.hyperdirmic',
        'CFBundleVersion': '0.1.0',
        'CFBundleShortVersionString': '0.1.0',
    },
}

setup(
    app=APP,
    name='Hyperdirmic',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
