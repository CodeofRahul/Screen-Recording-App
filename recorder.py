import cv2
import pyautogui
import numpy as np
import threading
import time
import os
from datetime import datetime

class ScreenRecorder:
    def __init__(self, output_base_path, quality="Medium"):
        self.output_base_path = output_base_path
        self.quality_map = {"Low": 5, "Medium": 10, "High": 20}
        self.fps = self.quality_map.get(quality, 10)
        self.recording = False
        self.paused = False
        self.frames = []
        self.size = pyautogui.size()
        self.quality = quality

    def start_recording(self):
        self.recording = True
        self.paused = False
        self.frames = []
        self._thread = threading.Thread(target=self._record)
        self._thread.start()

    def _record(self):
        while self.recording:
            if not self.paused:
                img = pyautogui.screenshot()
                frame = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
                self.frames.append(frame)
            time.sleep(1 / self.fps)

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def stop(self):
        self.recording = False
        self._thread.join()

        # Create recordings folder if not exist
        recordings_dir = os.path.join(self.output_base_path, "Recordings")
        os.makedirs(recordings_dir, exist_ok=True)

        # Generate filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"Recording_{timestamp}.avi"
        output_file = os.path.join(recordings_dir, filename)

        # Write video
        out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'XVID'), self.fps, self.size)
        for frame in self.frames:
            out.write(cv2.resize(frame, self.size))
        out.release()

        self.frames = []
        return output_file  # Return final video path for UI use

    def preview(self):
        for frame in self.frames:
            cv2.imshow("Preview", frame)
            if cv2.waitKey(int(1000 / self.fps)) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
