import mimetypes
import shutil
import logging
from pathlib import Path

# Base folders
DOWNLOADS_DIR = Path.home() / "Downloads"
LOG_DIR = Path.home() / "Library/Logs/Hyperdirmic"
LOG_FILE = LOG_DIR / "hyperdirmic.log"

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
        logger.info("�� No mime type found, using Other")
        return DOWNLOADS_DIR / "Other"

    # Try full match, then fallback to top-level type
    logger.info(f"🔍 Trying full match: {mime_type}")
    folder_name = FILE_DESTINATIONS.get(
        mime_type,
        FILE_DESTINATIONS.get(mime_type.split("/")[0], "Other"),
    )
    logger.info(f"🔍 Folder name: {folder_name}")
    return DOWNLOADS_DIR / folder_name


def safe_move_file(file_path: Path, dest_dir: Path):
    dest_dir.mkdir(exist_ok=True)
    dest_path = dest_dir / file_path.name

    try:
        shutil.move(str(file_path), str(dest_path))
        logger.info(f"✅ Moved: {file_path.name} → {dest_dir.name}")
        print(f"✅ Moved: {file_path.name} → {dest_dir.name}")
    except Exception as e:
        logger.error(f"❌ Failed to move {file_path.name}: {e}")
        print(f"❌ Failed to move {file_path.name}: {e}")
