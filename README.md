# Video to Transcript App

This application extracts audio from large video files and transcribes them using OpenAI Whisper.

## Requirements
- Python 3.8+
- ffmpeg (install via your package manager)
- WSL: X server required for GUI (Windows 11 WSLg supported out of the box)

## Installation

1. Install ffmpeg (if not already installed):
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the app:
   ```bash
   python app.py
   ```
2. Select a video file (drag-and-drop or browse).
3. Click "Go" to extract audio and transcribe.
4. The transcript will be saved as a `.txt` file next to your video.

## Notes
- If you want faster transcription, you can try `pip install faster-whisper` and modify the code to use it.
- For WSL users: If you don't see the GUI, ensure your X server is running (Windows 11 WSLg or VcXsrv/X410).
