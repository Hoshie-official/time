import tkinter as tk
import time

class StopwatchWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Stopwatch")
        self.geometry("300x150")

        self.elapsed_time = 0
        self.start_time = None
        self.is_running = False

        self.elapsed_time_label = tk.Label(self, text="00:00:00.000", font=("Helvetica", 24))
        self.elapsed_time_label.pack(pady=20)

        button_frame = tk.Frame(self)
        button_frame.pack()

        start_button = tk.Button(button_frame, text="Start", command=self.start)
        start_button.pack(side=tk.LEFT, padx=10)

        pause_button = tk.Button(button_frame, text="Pause", command=self.pause)
        pause_button.pack(side=tk.LEFT, padx=10)

        reset_button = tk.Button(button_frame, text="Reset", command=self.reset)
        reset_button.pack(side=tk.LEFT, padx=10)

    def start(self):
        if not self.is_running:
            self.start_time = time.time() - self.elapsed_time
            self.is_running = True
            self.update_timer()

    def pause(self):
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            self.is_running = False

    def reset(self):
        self.elapsed_time = 0
        self.start_time = None
        self.is_running = False
        self.update_timer()

    def update_timer(self):
        if self.is_running:
            elapsed = int((time.time() - self.start_time) * 1000)
        else:
            elapsed = int(self.elapsed_time * 1000)

        milliseconds = elapsed % 1000
        seconds = (elapsed // 1000) % 60
        minutes = (elapsed // 60000) % 60
        hours = elapsed // 3600000

        time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
        self.elapsed_time_label.config(text=time_string)

        if self.is_running:
            self.after(1, self.update_timer)

# 创建秒表窗口并运行主循环
stopwatch_window = StopwatchWindow()
stopwatch_window.mainloop()
