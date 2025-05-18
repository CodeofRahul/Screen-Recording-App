import tkinter as tk
from tkinter import filedialog, messagebox
from recorder import ScreenRecorder
from editor import cut_video, join_videos
import os

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Recorder App")
        self.root.geometry("400x450")  # Set window size
        self.root.resizable(True, True)
        self.output_path = os.getcwd()
        self.filename = "recording.avi"
        self.recorder = None

        self.setup_ui()

    def setup_ui(self):
        padding = {'padx': 10, 'pady': 5}

        title = tk.Label(self.root, text="🎥 Screen Recorder", font=("Helvetica", 16, "bold"))
        title.pack(pady=(20, 10))

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Start Recording", width=25, command=self.start_recording).grid(row=0, column=0, **padding)
        tk.Button(btn_frame, text="Pause Recording", width=25, command=self.pause_recording).grid(row=1, column=0, **padding)
        tk.Button(btn_frame, text="Preview (Paused)", width=25, command=self.preview_recording).grid(row=2, column=0, **padding)
        tk.Button(btn_frame, text="Resume Recording", width=25, command=self.resume_recording).grid(row=3, column=0, **padding)
        tk.Button(btn_frame, text="Stop & Save", width=25, command=self.stop_recording).grid(row=4, column=0, **padding)

        tk.Label(self.root, text="💾 Save Options", font=("Helvetica", 12, "bold")).pack(pady=(20, 0))
        tk.Button(self.root, text="Set Save Path", width=30, command=self.set_save_path).pack(**padding)

        tk.Label(self.root, text="✂️ Video Editing", font=("Helvetica", 12, "bold")).pack(pady=(20, 0))
        tk.Button(self.root, text="Cut Video", width=30, command=self.cut_video_ui).pack(**padding)
        tk.Button(self.root, text="Join Videos", width=30, command=self.join_videos_ui).pack(**padding)

        tk.Label(self.root, text="Developed with ❤️ in Python", font=("Arial", 9)).pack(pady=20)

    def start_recording(self):
        self.recorder = ScreenRecorder(self.output_path)
        self.recorder.start_recording()
        messagebox.showinfo("Recording", "Started recording.")

    def pause_recording(self):
        if self.recorder:
            self.recorder.pause()
            messagebox.showinfo("Paused", "Recording paused.")

    def preview_recording(self):
        if self.recorder and self.recorder.paused:
            self.recorder.preview()

    def resume_recording(self):
        if self.recorder:
            self.recorder.resume()
            messagebox.showinfo("Resumed", "Recording resumed.")

    def stop_recording(self):
        if self.recorder:
            self.recorder.stop(self.filename)
            messagebox.showinfo("Saved", f"Recording saved at {self.output_path}/{self.filename}")

    def set_save_path(self):
        path = filedialog.askdirectory()
        if path:
            self.output_path = path
            messagebox.showinfo("Path Updated", f"Save path set to: {self.output_path}")

    def cut_video_ui(self):
        input_path = filedialog.askopenfilename(title="Select video to cut")
        if not input_path:
            return
        try:
            start = int(self.simple_input("Enter Start Time (in seconds):"))
            end = int(self.simple_input("Enter End Time (in seconds):"))
            output_path = filedialog.asksaveasfilename(defaultextension=".mp4")
            cut_video(input_path, start, end, output_path)
            messagebox.showinfo("Video Cut", f"Saved to {output_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def join_videos_ui(self):
        video_paths = filedialog.askopenfilenames(title="Select videos to join")
        if not video_paths:
            return
        output_path = filedialog.asksaveasfilename(defaultextension=".mp4")
        try:
            join_videos(video_paths, output_path)
            messagebox.showinfo("Videos Joined", f"Saved to {output_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def simple_input(self, prompt):
        # Basic input dialog using Tkinter
        win = tk.Toplevel(self.root)
        win.title("Input")
        tk.Label(win, text=prompt).pack(padx=10, pady=10)
        entry = tk.Entry(win)
        entry.pack(padx=10, pady=10)
        entry.focus()

        result = []

        def on_ok():
            result.append(entry.get())
            win.destroy()

        tk.Button(win, text="OK", command=on_ok).pack(pady=5)
        self.root.wait_window(win)
        return result[0] if result else ""

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
