import tkinter as tk
from tkinter import filedialog, messagebox
from recorder import ScreenRecorder
from editor import cut_video, join_videos
import os


import datetime

def auto_generate_output_path(folder="Recordings", prefix="joined_", ext=".mp4"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}{timestamp}{ext}"
    return os.path.join(folder, filename)


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Recorder App")
        self.root.geometry("420x520")
        self.root.resizable(True, True)

        self.output_path = os.getcwd()
        self.recorder = None
        self.quality_choice = tk.StringVar(value="Medium")

        self.setup_ui()

    def setup_ui(self):
        padding = {'padx': 10, 'pady': 5}

        tk.Label(self.root, text="🎥 Screen Recorder", font=("Helvetica", 16, "bold")).pack(pady=(20, 10))

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        # Buttons
        tk.Button(btn_frame, text="Start Recording", width=30, command=self.start_recording).grid(row=0, column=0, **padding)
        tk.Button(btn_frame, text="Pause Recording", width=30, command=self.pause_recording).grid(row=1, column=0, **padding)
        tk.Button(btn_frame, text="Preview (Paused)", width=30, command=self.preview_recording).grid(row=2, column=0, **padding)
        tk.Button(btn_frame, text="Resume Recording", width=30, command=self.resume_recording).grid(row=3, column=0, **padding)
        tk.Button(btn_frame, text="Stop & Save", width=30, command=self.stop_recording).grid(row=4, column=0, **padding)

        # Quality dropdown
        tk.Label(self.root, text="🎚️ Select Quality", font=("Helvetica", 12, "bold")).pack(pady=(10, 0))
        quality_menu = tk.OptionMenu(self.root, self.quality_choice, "Low", "Medium", "High")
        quality_menu.config(width=20)
        quality_menu.pack(pady=5)

        # Save path
        tk.Label(self.root, text="💾 Save Location", font=("Helvetica", 12, "bold")).pack(pady=(20, 0))
        tk.Button(self.root, text="Choose Save Path", width=30, command=self.set_save_path).pack(**padding)

        # Video editing
        tk.Label(self.root, text="✂️ Video Editing", font=("Helvetica", 12, "bold")).pack(pady=(20, 0))
        tk.Button(self.root, text="Cut Video", width=30, command=self.cut_video_ui).pack(**padding)
        tk.Button(self.root, text="Join Videos", width=30, command=self.join_videos_ui).pack(**padding)

        tk.Label(self.root, text="Developed with ❤️ in Python", font=("Arial", 9)).pack(pady=20)

    def start_recording(self):
        quality = self.quality_choice.get()
        self.recorder = ScreenRecorder(self.output_path, quality=quality)
        self.recorder.start_recording()
        messagebox.showinfo("Recording", f"Started recording in {quality} quality.")

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
            saved_path = self.recorder.stop()
            messagebox.showinfo("Saved", f"Recording saved at:\n{saved_path}")

    def set_save_path(self):
        path = filedialog.askdirectory()
        if path:
            self.output_path = path
            messagebox.showinfo("Path Updated", f"Save path set to:\n{self.output_path}")

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
