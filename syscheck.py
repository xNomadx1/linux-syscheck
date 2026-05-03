"""Print basic Linux system information"""

import socket
import subprocess
import shutil
import argparse

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Shortcuts for system check functions"
    )

    parser.add_argument(
        "-hn", "--hostname",
        action="store_true",
        help="Show the system hostname.",
    )

    parser.add_argument(
        "-ut", "--uptime",
        action="store_true",
        help="Show system uptime."
    )

    return parser.parse_args()
        
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
    used = usage.used / (1024 ** 3)
    free = usage.free / (1024 ** 3)

    print(f"Total: {total:.2f} GB")
    print(f"Used: {used: .2f} GB")
    print(f"Free: {free: .2f} GB")

def print_memory_usage():
    """Print memory usage"""
    print("\nMemory usage:")
    subprocess.run(["free", "-h"], check=False)

def main():
    """Run all system checks."""
    args = parse_args()

    if not any([args.hostname, args.uptime]):
        print_hostname()
        print_uptime()
        print_disk_usage()
        print_memory_usage()

    if args.hostname:
        print_hostname()

    if args.uptime:
        print_uptime()

if __name__ == "__main__":
    main()
