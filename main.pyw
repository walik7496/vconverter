# Download ffmpeg.exe!
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import subprocess
import threading
import re

class VideoConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("Video Converter")

        self.input_path_label = tk.Label(master, text="Вхідний шлях:")
        self.input_path_label.grid(row=0, column=0, sticky="w")

        self.input_path_entry = tk.Entry(master, width=50)
        self.input_path_entry.grid(row=0, column=1)

        self.browse_button = tk.Button(master, text="Обрати", command=self.browse)
        self.browse_button.grid(row=0, column=2)

        self.output_extension_label = tk.Label(master, text="Вихідне розширення:")
        self.output_extension_label.grid(row=1, column=0, sticky="w")

        self.output_extension_entry = tk.Entry(master)
        self.output_extension_entry.insert(tk.END, ".avi")
        self.output_extension_entry.grid(row=1, column=1)

        self.convert_button = tk.Button(master, text="Конвертувати", command=self.convert)
        self.convert_button.grid(row=2, column=1)

        self.stop_button = tk.Button(master, text="Перервати", command=self.stop_conversion, state="disabled")
        self.stop_button.grid(row=2, column=2)

        self.status_label = tk.Label(master, text="Статус конвертації:")
        self.status_label.grid(row=3, column=0, sticky="w")

        self.status_text = tk.Text(master, height=5, width=50)
        self.status_text.grid(row=3, column=1)

        self.progress_bar = ttk.Progressbar(master, orient='horizontal', mode='determinate', length=300)
        self.progress_bar.grid(row=4, column=1, pady=10)

        self.process = None

    def browse(self):
        filepath = filedialog.askopenfilename(filetypes=[("Video Files", "*.webm;*.mkv;*.flv;*.vob;*.ogv;*.ogg;*.avi;*.mts;*.m2ts;*.ts;*.mov;*.wmv;*.rm;*.viv;*.asf;*.amv;*.mp4;*.mpg;*.mp2;*.mpeg;*.mpe;*.mpv;*.m2v;*.m4v;*.svi;*.3gp;*.3g2")])
        self.input_path_entry.delete(0, tk.END)
        self.input_path_entry.insert(0, filepath)

    def convert(self):
        input_path = self.input_path_entry.get()
        output_extension = self.output_extension_entry.get()

        if not input_path:
            messagebox.showerror("Помилка", "Будь ласка, виберіть вхідний файл")
            return

        if not output_extension:
            messagebox.showerror("Помилка", "Будь ласка, введіть вихідне розширення")
            return

        output_path = os.path.splitext(input_path)[0] + output_extension
        command = ['ffmpeg', '-i', input_path, '-crf', '20', output_path]  # Налаштований параметр CRF

        try:
            self.stop_button.config(state="normal")
            self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
            threading.Thread(target=self.monitor_progress, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Помилка", f"Помилка конвертації: {str(e)}")

    def monitor_progress(self):
        for line in self.process.stdout:
            self.status_text.insert(tk.END, line)
            self.status_text.see(tk.END)
            if "Duration" in line:  # Шукаємо початок виводу відео
                self.progress_bar["maximum"] = self.get_video_duration(line)
            elif "time=" in line:  # Оновлення прогресу
                current_time = self.get_current_time(line)
                if current_time is not None:
                    self.progress_bar["value"] = current_time

        self.progress_bar.stop()
        self.status_text.insert(tk.END, "Конвертація завершена\n")
        self.stop_button.config(state="disabled")

    def get_video_duration(self, line):
        duration_match = re.search(r"Duration: (\d{2}):(\d{2}):(\d{2}).\d+", line)
        if duration_match:
            hours = int(duration_match.group(1))
            minutes = int(duration_match.group(2))
            seconds = int(duration_match.group(3))
            total_seconds = hours * 3600 + minutes * 60 + seconds
            return total_seconds
        return None

    def get_current_time(self, line):
        time_match = re.search(r"time=(\d{2}):(\d{2}):(\d{2}).\d+", line)
        if time_match:
            hours = int(time_match.group(1))
            minutes = int(time_match.group(2))
            seconds = int(time_match.group(3))
            total_seconds = hours * 3600 + minutes * 60 + seconds
            return total_seconds
        return None

    def stop_conversion(self):
        if self.process is not None:
            self.process.terminate()
            self.status_text.insert(tk.END, "Конвертація перервана\n")
            self.stop_button.config(state="disabled")

root = tk.Tk()
app = VideoConverterApp(root)
root.mainloop()
