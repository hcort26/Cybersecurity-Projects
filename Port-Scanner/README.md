# Port Scanner

This project is a Python-based port scanner that scans a specified remote host for open TCP ports, reporting the service running on each open port. The script provides real-time feedback and scan duration information.

## 📂 Project Files
- `port_scanner.py`: Python script for scanning ports and identifying services on a target host.

## 🔑 Key Features
- **Full Range Scan**: Scans all 65,535 TCP ports (in descending order).
- **Service Detection**: Attempts to identify the service running on each open port using `socket.getservbyport()`.
- **User Input**: Prompts for the target host.
- **Timeout Handling**: Includes a 1-second timeout to avoid long waits on unresponsive ports.
- **Cross-Platform**: Uses `socket` and `subprocess` libraries for compatibility.
- **Error Handling**: Manages interruptions, unknown hostnames, and connection errors gracefully.
- **Duration Tracking**: Records and reports total scan time.
