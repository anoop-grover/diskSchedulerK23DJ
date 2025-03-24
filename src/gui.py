import tkinter as tk
import ttkbootstrap as ttk
from src.controllers import run_algorithm
from src.visualizer import plot_disk_movement

class DiskSchedulerGUI:
    def __init__(self):
        self.root = ttk.Window(themename="superhero")
        self.root.title("Disk Scheduling Visualizer")
        self.root.geometry("500x400")
        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text="Request Sequence:").pack()
        self.entry_requests = ttk.Entry(self.root, width=30)
        self.entry_requests.pack()
        ttk.Button(self.root, text="Run", command=self.run_scheduler).pack()

    def run_scheduler(self):
        requests = list(map(int, self.entry_requests.get().split(",")))
        head = int(self.entry_head.get())
        algorithm = self.algo_var.get()

        seek_sequence, seek_time = run_algorithm(requests, head, algorithm)
        plot_disk_movement(seek_sequence)

    def run(self):
        self.root.mainloop()
