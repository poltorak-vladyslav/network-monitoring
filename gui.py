import tkinter as tk
from tkinter import ttk
from network_info import get_network_info, get_cpu_info, get_memory_info, get_disk_info, get_process_count, get_uptime

class NetworkMonitorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("System Monitor")

        self.create_table()

    def create_table(self):
        headers = ['Parameter', 'Value']
        for idx, header in enumerate(headers):
            label = ttk.Label(self.root, text=header, font=("Arial", 12, "bold"))
            label.grid(row=0, column=idx, padx=10, pady=5, sticky="w")

        # CPU Usage
        self.cpu_label_name = ttk.Label(self.root, text="CPU Usage:", font=("Arial", 12))
        self.cpu_label_name.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.cpu_value_label = ttk.Label(self.root, text="", font=("Arial", 12))
        self.cpu_value_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Memory Usage
        self.memory_label_name = ttk.Label(self.root, text="Memory Usage:", font=("Arial", 12))
        self.memory_label_name.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.memory_value_label = ttk.Label(self.root, text="", font=("Arial", 12))
        self.memory_value_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Disk usage
        self.disk_label_name = ttk.Label(self.root, text="Disk Usage:", font=("Arial", 12))
        self.disk_label_name.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.disk_value_label = ttk.Label(self.root, text="", font=("Arial", 12))
        self.disk_value_label.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Network Traffic
        self.network_label_name = ttk.Label(self.root, text="Network Traffic:", font=("Arial", 12))
        self.network_label_name.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.network_value_label = ttk.Label(self.root, text="", font=("Arial", 12))
        self.network_value_label.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Processes
        self.processes_label_name = ttk.Label(self.root, text="Processes:", font=("Arial", 12))
        self.processes_label_name.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        self.processes_value_label = ttk.Label(self.root, text="", font=("Arial", 12))
        self.processes_value_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        # Uptime
        self.uptime_label_name = ttk.Label(self.root, text="Uptime:", font=("Arial", 12))
        self.uptime_label_name.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        self.uptime_value_label = ttk.Label(self.root, text="", font=("Arial", 12))
        self.uptime_value_label.grid(row=6, column=1, padx=10, pady=5, sticky="w")

    def update_info(self):
        self.cpu_value_label.config(text=get_cpu_info())
        self.memory_value_label.config(text=get_memory_info())
        self.disk_value_label.config(text=get_disk_info())
        self.network_value_label.config(text=get_network_info())
        self.processes_value_label.config(text=get_process_count())
        self.uptime_value_label.config(text=get_uptime())

        self.root.after(1000, self.update_info)

    def run(self):
        self.update_info()
        self.root.mainloop()