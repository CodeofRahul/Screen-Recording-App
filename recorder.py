import cv2
import pyautogui
import numpy as np
import threading
import time

class ScreenRecorder:
    def __init__(self, output_path):
        self.output_path = output_path
        self.recording = False
        self.paused = False
        self.frames = []
        self.fps = 10
        self.size = pyautogui.size()

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

    def stop(self, filename):
        self.recording = False
        self._thread.join()
        out = cv2.VideoWriter(self.output_path + "/" + filename, cv2.VideoWriter_fourcc(*'XVID'), self.fps, self.size)
        for frame in self.frames:
            out.write(cv2.resize(frame, self.size))
        out.release()
        self.frames = []

    def preview(self):
        for frame in self.frames:
            cv2.imshow("Preview", frame)
            if cv2.waitKey(int(1000 / self.fps)) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
