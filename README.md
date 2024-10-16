# System Monitor

This is a simple Python application for monitoring system resource usage in real-time. It provides information about:

- **CPU Usage:** Displays the current percentage of CPU usage
- **Memory Usage**: Shows the percentage of used memory and the exact amount in gigabytes
- **Disk Usage**: Displays the percentage of used disk space and the exact amount in gigabytes
- **Network Traffic**: Shows the total amount of bytes sent and received
- **Processes**: Displays the total number of running processes
- **Uptime**: Shows how long the system has been running since the last boot

The program uses the `psutil` library to gather system data and `tkinter` to display it in a graphical user interface (GUI).

## Requirements

- **Python 3.x**
- The following Python libraries:
  - `psutil`
  - `tkinter` (included with Python by default)

## Installation

1. **Clone or download the project:**

   ```bash
   git clone https://github.com/yourusername/system-monitor.git
   cd system-monitor
   
2. **Install the required Python library:**
   ```bash
   pip install psutil
   
## How to Run

1. **Navigate to the project directory where the main.py file is located**
 
2. **Run the application by executing the following command:**
   ```bash
   python main.py