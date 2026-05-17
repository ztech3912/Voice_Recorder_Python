# 🎤 Python Voice Recorder

A modern, lightweight desktop application built with Python using **Tkinter** and **PyAudio**. It allows users to record audio through their microphone and save it directly as high-quality lossless `.wav` files. 

The application utilizes background threading to keep the graphical user interface responsive and animated while managing the hardware audio stream.

---

## ✨ Features

- **Responsive Design:** Multi-threaded architecture prevents the GUI from freezing during active recording sessions.
- **Live Visual Timer:** Displays real-time recording length tracking formatted in `MM:SS`.
- **Modern Dark Theme:** Styled with Tailwind CSS inspired slate colors (`#0F172A`) for a clean, sleek appearance.
- **Dynamic Controls:** Single intuitive action button that dynamically swaps states between `Start` and `Stop`.
- **Safe File Validation:** Built-in safeguards to let you choose where to save files, complete with accidental overwrite or cancel protections.

---

## 🛠️ Tech Stack & Requirements

- **Python 3.7+**
- **Tkinter** (Included natively with standard Python installations)
- **PyAudio** (Python bindings for the cross-platform PortAudio library)
- **Wave** (Native wave file reading/writing module)
- **Threading** (Native multi-threading environment worker)

---

## 🚀 Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com
cd python-voice-recorder
```

### 2. Install System Dependencies (Linux Users Only)
If you are running the project on macOS or Windows, skip this step. On Debian/Ubuntu Linux systems, you must install the development headers for PortAudio first:
```bash
sudo apt update
sudo apt install portaudio19-dev python3-pyaudio
```

### 3. Install Python Packages
Install the required application library using `pip`:
```bash
pip install pyaudio
```

---

## 💻 How To Run

Execute the script from your terminal:
```bash
python main.py
```

### How to use:
1. Click **🎤 Start Recording** to initialize your hardware input device.
2. Monitor your session runtime with the live digital clock.
3. Click **🛑 Stop Recording** to finalize the audio frame buffers.
4. A file dialog pop-up will appear. Choose your folder destination, name the file, and press **Save**.

---

## ⚙️ Audio Properties Configuration

The project is pre-configured to record standard high-fidelity voice notes. If you wish to tweak the default specifications, open `main.py` and modify the constants at the top of the file:

```python
FORMAT = pyaudio.paInt16  # 16-bit resolution
CHANNELS = 1              # Mono track recording (Use 2 for Stereo)
fs = 44100                # CD Quality Sampling Rate (44.1 kHz)
CHUNK = 1024              # Buffer frame chunk size
```

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
