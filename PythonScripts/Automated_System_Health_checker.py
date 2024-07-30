# Develop a script that monitors the health of a Linux system. 
# It should check CPU usage, memory usage, disk space, and running processes. 
# If any of these metrics exceed predefined thresholds (e.g., CPU usage > 80%), the script should send an alert to the console or a log file. 

import psutil
import logging
from datetime import datetime
import time

# Setup logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        message = f"High CPU usage detected: {cpu_usage}%"
        logger.warning(message)
        print(message)
    else:
        print(f"CPU usage is at {cpu_usage}%")

def check_memory_usage():
    memory = psutil.virtual_memory()
    if memory.percent > MEMORY_THRESHOLD:
        message = f"High Memory usage detected: {memory.percent}%"
        logger.warning(message)
        print(message)
    else:
        print(f"Memory usage is at {memory.percent}%")

def check_disk_usage():
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        message = f"Low Disk space detected: {disk.percent}% used"
        logger.warning(message)
        print(message)
    else:
        print(f"Disk usage is at {disk.percent}%")

def check_running_processes():
    processes = len(psutil.pids())
    message = f"Number of running processes: {processes}"
    logger.info(message)
    print(message)

def monitor_system():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

if __name__ == "__main__":
    while True:
        monitor_system()
        print("System health check done.\n")
        time.sleep(60)
