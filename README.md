# Linux Syscheck

A simple Python command-line script that prints basic Linux system information.

## What it does

Linux Syscheck displays:

- System hostname
- System uptime
- Root filesystem disk usage
- Memory usage

**Be sure to check out the command line arguments by running python3 stories.py -help.**

No external Python packages are required.

This project only uses the Python standard library:

- `socket`
- `subprocess`
- `shutil`
- `argparse`