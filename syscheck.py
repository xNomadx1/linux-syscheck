"""Print basic Linux system information"""

import socket
import subprocess
import shutil

def print_hostname():
    """Print the system hostname."""
    print(f"Hostname: {socket.gethostname()}")
    
def print_uptime():
    """Print system uptime using the uptime command."""
    print("\nUptime:")
    subprocess.run(["uptime"], check=False)

def print_disk_usage():
    """Print disk usage for the root filesystem."""
    print("\nDisk usage")

    usage =shutil.disk_usage("/")
    total = usage.total / (1024 ** 3)
    used = usage.total / (1024 ** 3)
    free = usage.free / (1024 ** 3)

    print(f"Total: {total:.2f} GB")
    print(f"Used: {used: .2f} GB")
    print(f"Free: {free: .2f} GB")

def main():
    """Run all system checks."""
    print_hostname()
    print_uptime()
    print_disk_usage()

if __name__ == "__main__":
    main()