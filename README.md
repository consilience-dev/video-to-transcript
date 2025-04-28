# Video to Transcript App

A simple, robust application for extracting audio from very large video files and transcribing them using OpenAI Whisper. Designed for ease-of-use, with a graphical interface and support for files of virtually any size.

---

## Features
- **Drag-and-drop or browse** for video selection (browse recommended for Linux/WSL)
- **Handles very large video files** (40GB+)
- **Automatic audio extraction** using ffmpeg
- **Accurate speech-to-text transcription** using Whisper
- **Transcript saved as .txt** in the same folder as your video
- **Cross-platform** (Linux, WSL, Windows with Python)
- **Minimal setup** required

---

## Architecture

1. **Frontend:**
    - Built with Tkinter for a simple GUI
    - Lets user select a video file and start processing
    - Displays progress and error messages

2. **Backend:**
    - Uses ffmpeg to extract audio from the video file efficiently (no full RAM load)
    - Uses Whisper (default: base model) for transcription
    - Writes transcript to a `.txt` file next to the video

**Flow:**
```
User selects video → ffmpeg extracts audio → Whisper transcribes audio → Transcript saved
```

---

## Requirements
- Python 3.8+
- ffmpeg (install via your package manager)
- WSL: X server required for GUI (Windows 11 WSLg supported out of the box)

---

## Installation

1. **Install ffmpeg:**
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```
2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Run the app:**
   ```bash
   python app.py
   ```
2. **Select a video file** (click the gray box to browse).
3. **Click "Go"** to extract audio and transcribe.
4. **Transcript** will be saved as a `.txt` file in the same folder as your video.

---

## Troubleshooting
- If you get `ModuleNotFoundError: No module named 'tkinter'`, install it with:
  ```bash
  sudo apt install python3-tk
  ```
- If the GUI doesn't appear on WSL, make sure you have an X server running (Windows 11 WSLg, or VcXsrv/X410 on Windows 10).
- For very large files, ensure you have enough disk space for the extracted audio.

---

## Customization
- **Change Whisper model:** Edit `model = whisper.load_model("base")` in `app.py` to use `small`, `medium`, or `large` for higher accuracy (at the cost of speed and memory).
- **CPU/GPU selection:** By default, Whisper will use GPU if available. To force CPU, change the model load line to:
  ```python
  model = whisper.load_model("base", device="cpu")
  ```
- **Chunking:** For extremely long videos, you may want to split audio into chunks and transcribe in pieces. (Not implemented by default, but can be added.)

---

## Contributing
Pull requests and issues are welcome! Please open an issue for feature requests or bug reports.

---

## License
MIT License. See [LICENSE](LICENSE) for details.

---

## Credits
- [OpenAI Whisper](https://github.com/openai/whisper)
- [ffmpeg](https://ffmpeg.org/)
- Python, Tkinter

---

## Links
- [GitHub Repo](https://github.com/consilience-dev/video-to-transcript)
- [Open Issues](https://github.com/consilience-dev/video-to-transcript/issues)

---

For any questions or support, open an issue on GitHub!
