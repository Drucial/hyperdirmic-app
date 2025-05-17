# 🧹 Hyperdirmic

**Hyperdirmic** is a minimalist background macOS utility that automatically organizes your `Downloads/` folder in real time. It detects new files, categorizes them by type (images, documents, apps, etc.), and moves them into corresponding subfolders.

---

## 🚀 Features

- ✅ Real-time file detection in your Downloads folder
- ✅ Categorizes files based on MIME type or extension
- ✅ Moves files into clean subfolders (e.g., `Images/`, `Documents/`, `Archives/`, etc.)
- ✅ Lightweight tray icon (menubar utility) with Quit option
- ✅ Works silently in the background

---

## 🎯 Future Enhancements (Roadmap)

- ⏲️ Auto-start at login
- ⚙️ Preferences menu (folder exclusions, category overrides)
- 🖼️ Customizable tray icon
- 📄 Activity logging and error tracking
- 🔁 Update mechanism (via Homebrew or Sparkle)
- 🌙 Dark/light mode tray icon options
- 🧪 Rule-based organizing (e.g., "DMGs to Archive after 24 hours")

---

## 🛠 Developer Setup

> These steps are for development and building the `.app`, not required for end users.

### 🧱 Prerequisites

- ✅ Python 3.10+ (recommended)
- ✅ `pip` (comes with Python install)

> 💡 macOS does not come with an ideal Python version for development.  
> Download the official installer: [https://www.python.org/downloads/mac-osx/](https://www.python.org/downloads/mac-osx/)

Check your versions:

```
python3 --version
pip3 --version
```

---

## ▶️ Run (Developer Only)

```
# Clone the repo
git clone https://github.com/Drucial/hyperdirmic.git
cd hyperdirmic

# Set up a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install app dependencies
pip install -r requirements.txt

# (Optional) Install py2app for packaging
pip install -r requirements-dev.txt

# Run the app
python3 src/organizer.py
```

This will launch a background watcher and show a tray icon in your macOS menu bar.

---

## 🧪 Installation

You can install **Hyperdirmic** via [Homebrew](https://brew.sh/):

```bash
brew tap drucial/hyperdirmic
brew install --cask hyperdirmic
```

Or manually via `curl` and GitHub releases:

```bash
curl -L -o Hyperdirmic.zip https://github.com/Drucial/hyperdirmic/releases/download/v0.1.0/Hyperdirmic.zip
unzip Hyperdirmic.zip -d /Applications
open /Applications/Hyperdirmic.app
```

### 🛑 First-Time Launch Instructions

The first time you open the app, macOS may block it:

- Go to **System Settings > Privacy & Security**
- Scroll to the bottom and click **'Open Anyway'**
- Confirm that you want to run Hyperdirmic

The app will appear in your menu bar and begin organizing your `Downloads/` folder in real time.

---
## ⚙️ Configuration

Current configuration is hardcoded to watch the `~/Downloads` folder and use default subfolders:

| File Type       | Destination Subfolder |
| --------------- | --------------------- |
| Images          | `Images/`             |
| PDFs/Text       | `Documents/`          |
| Archives (.zip) | `Archives/`           |
| Applications    | `Applications/`       |
| Videos          | `Videos/`             |
| Audio           | `Audio/`              |
| Other           | `Other/`              |

In the future, config will be stored in `~/Library/Application Support/Hyperdirmic/config.json`.

---

## 🎯 Future Enhancements (Roadmap)

These are planned or potential features for upcoming versions of Hyperdirmic.

### 📦 Packaging & Distribution

- [x] Build signed `.app` with py2app
- [x] Zip for GitHub releases
- [x] Homebrew Cask support:
  - [x] Create `homebrew-hyperdirmic` tap
  - [x] `brew install --cask hyperdirmic`

---

### 🧼 Internal Functionality Enhancements

- [x] Real-time file system monitoring with `watchdog`
- [x] Classification by MIME type with fallback support
- [x] Safe file moving with error handling
- [x] Persistent logging to `~/Library/Logs/Hyperdirmic`
- [x] Add support for handling `.part` or temp download files more gracefully
- [ ] Optional log rotation or truncation strategy
- [ ] Add more granular logging levels (INFO, DEBUG, WARNING)

---

### 🛠️ Core UX Features

- [ ] Preferences menu (UI) to customize:
  - Folder destinations for each file type
  - Enable/disable auto-organizing per category
- [ ] Start automatically on login via macOS `launchd`
- [ ] Native macOS menubar integration with preferences
- [ ] Drag-and-drop files onto the tray icon (bonus)

---

### 🧙 Nice-to-Have Ideas

- [ ] GUI for viewing log history (lightweight panel)
- [ ] Notification system (optional) for file moves
- [ ] Periodic summary of organization (e.g. "You organized 22 files this week!")
- [ ] iCloud Downloads folder support

---

## 📄 License

MIT

---

## 💡 Why "Hyperdirmic"?

Because it's like a **hypodermic needle**... but for **directories**.  
It injects **organization** right into the **veins** of your file system.

🤓💉📂

---

_Last updated: 2025-05-17_