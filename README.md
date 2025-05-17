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

```bash
python3 --version
pip3 --version
```

---

## ▶️ Run (Developer Only)

```bash
# Clone the repo
git clone https://github.com/yourname/hyperdirmic.git
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

## 🛠 Development Roadmap

### ✅ Local Development

- [x] Clone the repo
- [x] Create a virtualenv
- [x] Install dependencies
- [ ] Run app using `organizer.py`
- [ ] Test file drops in `~/Downloads/`
- [ ] Verify log output and file movement

---

### ✅ macOS `.app` Bundle with `py2app`

- [x] Install `py2app`:

  ```
  pip install -r requirements-dev.txt
  ```

- [ ] Build the app:

  ```
  python setup.py py2app
  ```

- [ ] Output: `dist/Hyperdirmic.app`

---

### ✅ Create a Homebrew Cask (Once Deployed)

1. [ ] Zip the app bundle:

   ```
   cd dist
   zip -r Hyperdirmic.zip Hyperdirmic.app
   ```

2. [ ] Calculate the SHA256 hash:

   ```
   shasum -a 256 Hyperdirmic.zip
   ```

3. [ ] Create a GitHub release and upload the `.zip`

4. [ ] In your `homebrew-hyperdirmic` tap:

   - [ ] Create `Casks/hyperdirmic.rb` formula
   - [ ] Fill in metadata and hash

5. [ ] Test with:

   ```
   brew tap yourname/hyperdirmic
   brew install --cask hyperdirmic
   ```

---

## 📄 License

MIT

---

## 💡 Why "Hyperdirmic"?

Because it's like a **hypodermic needle**... but for **directories**.  
It injects **organization** right into the **veins** of your file system.

🤓💉📂
