"""Print basic Linux system information"""

import shutil
import socket
import subprocess

from pathlib import Path

AUTH_LOG = Path("/var/log/auth.log")

def print_hostname():
    """Print the system hostname."""
    print(f"Hostname: {socket.gethostname()}")
    
