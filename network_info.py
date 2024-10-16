from datetime import datetime

import psutil

def get_network_info():
    net_io = psutil.net_io_counters()
    return f"Sent: {net_io.bytes_sent} Bytes, Received: {net_io.bytes_recv} Bytes"

def get_cpu_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    return f"{cpu_percent}%"

def get_memory_info():
    memory = psutil.virtual_memory()
    return f"{memory.percent}% ({memory.used / (1024 ** 3):.2f} GB / {memory.total / (1024 ** 3):.2f} GB)"

def get_disk_info():
    disk = psutil.disk_usage('/')
    return f"{disk.percent}% ({disk.used / (1024 ** 3):.2f} GB / {disk.total / (1024 ** 3):.2f} GB)"

def get_uptime():
    uptime = psutil.boot_time()
    current_time = datetime.now()
    uptime_duration = current_time - datetime.fromtimestamp(uptime)
    return f"{str(uptime_duration).split('.')[0]}"

def get_process_count():
    processes = len(psutil.pids())
    return f"{processes}"