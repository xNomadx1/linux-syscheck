"""Print basic Linux system information"""

import socket
import subprocess

from pathlib import Path

AUTH_LOG = Path("/var/log/auth.log")

def print_hostname():
    """Print the system hostname."""
    print(f"Hostname: {socket.gethostname()}")
    
def print_uptime():
    """Print system uptime using the uptime command."""
    print("\nUptime:")
    subprocess.run(["uptime"], check=False)