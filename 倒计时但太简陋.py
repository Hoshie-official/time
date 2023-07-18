import tkinter as tk
import tkinter.messagebox

class CountdownWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("倒计时窗口")

        # 时分秒的输入框
        self.hour_entry = tk.Entry(self, width=2)
        self.hour_entry.grid(row=0, column=0)
        self.hour_label = tk.Label(self, text="时")
        self.hour_label.grid(row=0, column=1)
        self.minute_entry = tk.Entry(self, width=2)
        self.minute_entry.grid(row=0, column=2)
        self.minute_label = tk.Label(self, text="分")
        self.minute_label.grid(row=0, column=3)
        self.second_entry = tk.Entry(self, width=2)
        self.second_entry.grid(row=0, column=4)
        self.second_label = tk.Label(self, text="秒")
        self.second_label.grid(row=0, column=5)

        # 开始、暂停、停止按钮
        self.start_button = tk.Button(self, text="开始", command=self.start_countdown)
        self.start_button.grid(row=1, column=0, pady=10)
        self.pause_button = tk.Button(self, text="暂停", command=self.pause_countdown)
        self.pause_button.grid(row=1, column=1)
        self.stop_button = tk.Button(self, text="停止", command=self.stop_countdown)
        self.stop_button.grid(row=1, column=2)

        # 倒计时显示标签
        self.timer_label = tk.Label(self, text="")
        self.timer_label.grid(row=2, columnspan=6, pady=10)

        # 初始化倒计时变量
        self.remaining_time = 0
        self.paused = False

    def start_countdown(self):
        # 获取用户输入的时分秒
        hours = int(self.hour_entry.get())
        minutes = int(self.minute_entry.get())
        seconds = int(self.second_entry.get())

        # 将时分秒转换为总秒数
        total_seconds = hours * 3600 + minutes * 60 + seconds

        # 开始倒计时
        self.remaining_time = total_seconds
        self.update_countdown()

    def update_countdown(self):
        if self.remaining_time > 0 and not self.paused:
            # 将总秒数转换为时分秒格式
            hours = self.remaining_time // 3600
            minutes = (self.remaining_time % 3600) // 60
            seconds = self.remaining_time % 60
            time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

            # 更新显示倒计时的标签
            self.timer_label.config(text=time_string)

            # 减少倒计时剩余时间
            self.remaining_time -= 1

            # 每秒调用一次更新倒计时函数
            self.after(1000, self.update_countdown)
        elif self.remaining_time == 0:
            # 倒计时完成后弹出提示窗口
            tkinter.messagebox.showinfo("提示", "时间到！")
            self.timer_label.config(text="")
        else:
            # 暂停状态下不更新倒计时
            self.after(1000, self.update_countdown)

    def pause_countdown(self):
        self.paused = not self.paused

    def stop_countdown(self):
        self.remaining_time = 0
        self.paused = False
        self.timer_label.config(text="")

if __name__ == "__main__":
    window = CountdownWindow()
    window.mainloop()
