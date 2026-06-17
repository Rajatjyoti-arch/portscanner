# Python Multithreaded Port Scanner

A fast, multithreaded TCP port scanner written in Python. This tool uses Python's built-in `socket` and `threading` modules to scan ports across a specified IP address efficiently.

## Features
- **Multithreaded Scanning**: Utilizes a configurable number of threads to concurrently scan multiple ports, drastically reducing scan times.
- **Queue-based Task Distribution**: Leverages Python's thread-safe `Queue` to distribute target ports evenly across the worker threads.
- **Customizable Timeout**: Each socket connection has a built-in timeout so the scanner does not hang on unresponsive, filtered ports.
- **Automated Resource Management**: Sockets are cleanly closed after each check to prevent resource leaks and OS limitations.

## Requirements
- Python 3.x
- No external libraries required (uses only standard library modules).

## Usage
1. Clone or download the repository.
2. Run the script using Python:
   ```bash
   python main.py
   ```
3. When prompted, enter the **target IP address**.
   > **Note:** The script expects a single valid IPv4 address (e.g., `192.168.1.1` or `10.59.248.0`). It does not currently support CIDR notation (like `10.59.248.0/24`) or domain name resolution natively without modification.
4. The scanner will initiate its threads and begin checking ports 1 through 1023.
5. Open ports will be printed to the terminal, followed by a final summarized list of all open ports.

## Configuration
To scan a different range of ports or change the thread count, you can edit `main.py` directly:
- **Port Range**: Change the argument in `range(1, 1024)` to scan different port blocks.
- **Thread Count**: Modify the number in `for i in range(1000):` to allocate more or fewer threads depending on your system's capabilities and network constraints.
