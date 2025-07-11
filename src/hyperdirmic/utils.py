import mimetypes
import shutil
import logging
import os
from pathlib import Path
from Cocoa import NSWorkspace, NSImage
import sys

# Base folders
DOWNLOADS_DIR = Path.home() / "Downloads"
LOG_DIR = Path.home() / "Library/Logs/Hyperdirmic"
LOG_FILE = LOG_DIR / "hyperdirmic.log"

# Asset icon directory and folder icon map
ICONS_DIR = Path(__file__).parent.parent / "assets" / "images"
FOLDER_ICONS = {
    "Images": "folder_dark.icns",
    "Videos": "folder_dark.icns",
    "Audio": "folder_dark.icns",
    "Documents": "folder_dark.icns",
    "Archives": "folder_dark.icns",
    "Applications": "folder_dark.icns",
    "Other": "folder_dark.icns",
}

# Create log directory if needed
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Logging setup
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    )

logger = logging.getLogger(__name__)

# Mapping of MIME types or top-level types to folder names
FILE_DESTINATIONS = {
    "image": "Images",
    "video": "Videos",
    "audio": "Audio",
    "text": "Documents",
    "application/pdf": "Documents",
    "application/zip": "Archives",
    "application/x-bzip": "Archives",
    "application/x-tar": "Archives",
    "application/x-apple-diskimage": "Archives",  # .dmg files
    "application": "Applications",
}

def get_destination_folder(file_path: Path) -> Path:
    logger.info(f"🔍 Getting destination folder for {file_path.name}")

    # Direct extension check for installer files
    installer_extensions = [".dmg", ".pkg", ".mpkg", ".app", ".exe", ".msi"]
    if file_path.suffix.lower() in installer_extensions:
        logger.info(f"📁 Detected installer file by extension ({file_path.suffix}), using 'Applications'")
        return DOWNLOADS_DIR / "Applications"

    mime_type, _ = mimetypes.guess_type(file_path.name)
    logger.info(f"🔍 Mime type: {mime_type}")
    if not mime_type:
        logger.info("📁 No mime type found, using 'Other'")
        return DOWNLOADS_DIR / "Other"

    folder_name = FILE_DESTINATIONS.get(
        mime_type,
        FILE_DESTINATIONS.get(mime_type.split("/")[0], "Other"),
    )
    logger.info(f"📁 Folder name: {folder_name}")
    return DOWNLOADS_DIR / folder_name

def set_folder_icon(directory_path: str, icon_path: str) -> bool:
    logger.info(f"🎨 Setting icon for '{directory_path}' with '{icon_path}'")

    icon = NSImage.alloc().initWithContentsOfFile_(icon_path)
    if not icon:
        logger.error(f"❌ Failed to load icon at '{icon_path}'")
        return False

    success = NSWorkspace.sharedWorkspace().setIcon_forFile_options_(icon, directory_path, 0)
    if success:
        logger.info(f"✅ Icon set for '{directory_path}'")
        os.utime(directory_path, None)  # Touch to force Finder refresh
    else:
        logger.error(f"❌ Failed to set icon for '{directory_path}'")
    
    return success

def is_temp_file(file_path: Path) -> bool:
    return file_path.suffix.lower() in [".part", ".crdownload", ".tmp", ".download"]

def safe_move_file(file_path: Path, dest_dir: Path):

    if is_temp_file(file_path):
        logger.info(f"🔍 Skipping temp file: {file_path.name}")
        return

    is_new_folder = not dest_dir.exists()
    dest_dir.mkdir(exist_ok=True)

    # Build the destination path, avoiding name collisions
    dest_path = dest_dir / file_path.name
    
    # Only rename if there's an actual collision
    if dest_path.exists():
        stem = file_path.stem
        suffix = file_path.suffix
        counter = 1

        while dest_path.exists():
            dest_path = dest_dir / f"{stem} ({counter}){suffix}"
            counter += 1

    try:
        shutil.move(str(file_path), str(dest_path))
        logger.info(f"✅ Moved: {file_path.name} → {dest_path.name}")
        print(f"✅ Moved: {file_path.name} → {dest_path.name}")

        if is_new_folder:
            icon_name = FOLDER_ICONS.get(dest_dir.name, "folder_light.icns")
            icon_path = resource_path(icon_name)
            set_folder_icon(str(dest_dir), icon_path)

    except Exception as e:
        logger.error(f"❌ Failed to move {file_path.name}: {e}")
        print(f"❌ Failed to move {file_path.name}: {e}")

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    elif getattr(sys, 'frozen', False):
        return os.path.join(os.environ['RESOURCEPATH'], relative_path)
    else:
        # In development mode, look in src/assets/images
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "images", relative_path)
