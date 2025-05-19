# 📹 Screen Recorder & Video Editor (Python + Tkinter)

[![GitHub Stars](https://img.shields.io/github/stars/CodeofRahul/Screen-Recording-App?style=social)](https://github.com/CodeofRahul/Screen-Recording-App/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/CodeofRahul/Screen-Recording-App?style=social)](https://github.com/CodeofRahul/Screen-Recording-App/network)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux-lightgrey)]()

---

> A Python desktop app to record screen, pause/resume, preview recordings, choose save location, and cut/join videos — all with a clean Tkinter UI.

---

### 🚀 Features

- 🎥 **Screen Recording with UI**
  - Start, Pause, Resume recording
  - Choose from multiple quality options (Low, Medium, High)
  - Save recordings with auto-generated filenames (timestamped)

- ⏸️ **Pause and Preview During Recording**
  - Pause the recording and preview what’s been captured so far
  - Resume recording seamlessly in the same file

- 📁 **Flexible Save Path**
  - Set a default folder to store recordings
  - Change the save location anytime from the UI

- ✂️ **Cut Video Segments**
  - Select a portion of a video based on start/end time
  - Save the cut segment as a new video file

- 🔗 **Join Multiple Videos**
  - Select multiple videos and merge them into one
  - Automatically resizes and synchronizes formats
  - Output is saved with a timestamp-based unique name

- 💾 **No File Overwrites**
  - Every output file (recorded, cut, or joined) is saved with a unique name
  - Output folder structure is auto-managed (`Recordings/`)

---

### 📸 Demo

![image](https://github.com/user-attachments/assets/3f25ad97-7202-4383-937e-74b4b0247deb)


---

### 🛠 Tech Stack

| Component        | Technology     |
|------------------|----------------|
| GUI              | Tkinter        |
| Screen Recording | OpenCV, pyautogui |
| Video Processing | moviepy        |
| Video Encoding   | ffmpeg (via moviepy) |
| File Dialogs     | tkinter.filedialog |

---

### 📂 Folder Structure

Screen-Recording-App/
 <br>
├── main.py # UI and application logic <br>
├── recorder.py # Screen recording logic <br>
├── editor.py # Video cut/join logic <br>
├── README.md # This file <br>
├── Recordings/ # Auto-generated folder for saved videos <br>
├── venv/ # (your virtual environment) <br>


---

### 🧰 Installation

1. **Clone the repository**:
```bash
git clone https://github.com/CodeofRahul/Screen-Recording-App.git
cd Screen-Recording-App
```

2. **Create a virtual environment:**

```bash
python -m venv venv
# Activate:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

If not using a `requirements.txt`:

```bash
pip install opencv-python pyautogui moviepy imageio-ffmpeg
```

### ▶️ Running the App

```bash
python main.py
```

### 📦 Features in Detail

✅ **Quality Settings**

- Low (640x480)
- Medium (1280x720)
- High (1920x1080)

✅ **File Naming Convention**

Auto-generated filenames for all outputs:

```bash
Recordings/recording_20250518_174203.avi
Recordings/cut_20250518_174547.mp4
Recordings/joined_20250518_174823.mp4
```

### 🤝 Contributions

Contributions are welcome! If you'd like to:

- Add more editing features
- Improve performance or UI
- Package as a desktop app (using PyInstaller or Tkinter Designer)

Feel free to submit a pull request or open an issue!




## Setup Instructions

- To create environment = `conda create -p <env_name> python=3.8 -y`
- To check available envs = `conda env list`
- To check available envs = `conda info --envs`
- To activate environment = `conda activate <env_name>`
- To install requirements.txt = `pip install -r requirements.txt`
- To check install packages = `pip list`
- To check detailed about package = `pip show package_name`
- To install package = `pip install package_name`
- To uninstall package = `pip uninstall package_name`
- To save all packages of env to a requirements.txt file = `pip freeze > requirements.txt`

## Git commands

- To add all file = `git add .`
- To add any particular file = `git add <file_name>`
- To commit = `git commit -m "commit message"`
- To push the code = `git push origin main`
