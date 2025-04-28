import os
import sys
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

# Try importing whisper, if not found, show a message
try:
    import whisper
except ImportError:
    whisper = None

# Check ffmpeg availability
FFMPEG_EXISTS = False
try:
    subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    FFMPEG_EXISTS = True
except Exception:
    FFMPEG_EXISTS = False

class STTApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Video to Transcript (Whisper)")
        self.geometry("500x220")
        self.resizable(False, False)
        self.file_path = None

        self.label = tk.Label(self, text="Drag and drop a video file or click Browse", font=("Arial", 12))
        self.label.pack(pady=20)

        self.drop_area = tk.Label(self, text="Drop file here", bg="#e0e0e0", width=40, height=4, relief=tk.RIDGE)
        self.drop_area.pack(pady=5)
        self.drop_area.bind("<Button-1>", self.browse_file)

        self.go_button = tk.Button(self, text="Go", state=tk.DISABLED, command=self.start_process)
        self.go_button.pack(pady=10)

        self.progress = tk.Label(self, text="", font=("Arial", 10))
        self.progress.pack(pady=5)

        # Drag-and-drop events removed for compatibility
        # self.drop_area.bind("<DragEnter>", self.drag_enter)
        # self.drop_area.bind("<Drop>", self.drop)
        # Fallback for drag-n-drop: click to browse
        # self.drop_area.bind("<Button-1>", self.browse_file)

    def drag_enter(self, event):
        pass  # No-op, removed for compatibility

    def drop(self, event):
        pass  # No-op, removed for compatibility

    def browse_file(self, event=None):
        path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.mkv *.mov *.avi *.flv *.webm"), ("All files", "*.*")])
        if path:
            self.set_file(path)

    def set_file(self, path):
        self.file_path = path
        self.drop_area.config(text=os.path.basename(path), bg="#e0e0e0")
        self.go_button.config(state=tk.NORMAL)
        self.progress.config(text="")

    def start_process(self):
        if not self.file_path:
            messagebox.showerror("No file", "Please select a video file.")
            return
        if not FFMPEG_EXISTS:
            messagebox.showerror("ffmpeg not found", "ffmpeg is required. Please install ffmpeg and try again.")
            return
        if whisper is None:
            messagebox.showerror("Whisper not installed", "The 'whisper' Python package is required. Please install it with 'pip install openai-whisper' or 'pip install faster-whisper'.")
            return
        self.go_button.config(state=tk.DISABLED)
        self.progress.config(text="Extracting audio...")
        threading.Thread(target=self.process_video).start()

    def process_video(self):
        audio_path = self.extract_audio(self.file_path)
        if not audio_path:
            self.progress.config(text="Audio extraction failed.")
            self.go_button.config(state=tk.NORMAL)
            return
        self.progress.config(text="Transcribing audio...")
        transcript = self.transcribe_audio(audio_path)
        if transcript:
            txt_path = os.path.splitext(self.file_path)[0] + "_transcript.txt"
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(transcript)
            self.progress.config(text=f"Done! Transcript saved to {os.path.basename(txt_path)}")
        else:
            self.progress.config(text="Transcription failed.")
        self.go_button.config(state=tk.NORMAL)
        if os.path.exists(audio_path):
            try:
                os.remove(audio_path)
            except Exception:
                pass

    def extract_audio(self, video_path):
        audio_path = os.path.splitext(video_path)[0] + "_audio.wav"
        cmd = ["ffmpeg", "-i", video_path, "-vn", "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1", audio_path, "-y"]
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return audio_path
        except Exception as e:
            return None

    def transcribe_audio(self, audio_path):
        try:
            model = whisper.load_model("base")
            result = model.transcribe(audio_path)
            return result["text"]
        except Exception as e:
            return None

def main():
    app = STTApp()
    app.mainloop()

if __name__ == "__main__":
    main()
