import mimetypes
import shutil
import logging
import os
from pathlib import Path
from Cocoa import NSWorkspace, NSImage

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

def safe_move_file(file_path: Path, dest_dir: Path):
    is_new_folder = not dest_dir.exists()
    dest_dir.mkdir(exist_ok=True)
    dest_path = dest_dir / file_path.name

    try:
        shutil.move(str(file_path), str(dest_path))
        logger.info(f"✅ Moved: {file_path.name} → {dest_dir.name}")
        print(f"✅ Moved: {file_path.name} → {dest_dir.name}")

        if is_new_folder:
            icon_name = FOLDER_ICONS.get(dest_dir.name, "folder_dark.icns")
            icon_path = str(ICONS_DIR / icon_name)
            set_folder_icon(str(dest_dir), icon_path)

    except Exception as e:
        logger.error(f"❌ Failed to move {file_path.name}: {e}")
        print(f"❌ Failed to move {file_path.name}: {e}")
