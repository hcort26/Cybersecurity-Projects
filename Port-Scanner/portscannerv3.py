#!/usr/bin/env python3

import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

# Changed raw_input() to input() for Python 3 compatibility
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

# Check what time the scan started
t1 = datetime.now()

try:
    # Changed port range from 1-1024 to 65535-1 for full port scan in descending order
    for port in range(65535, 0, -1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Added timeout for faster scanning
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            # Added socket.getservbyport() to display the service name
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown service"
            print(f"Port {port}: Open")
            print(f"Service is = {service}")
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# Check the time again
t2 = datetime.now()

# Calculate total scan time
total = t2 - t1

# Print scanning duration
print('Scanning Completed in: ', total)
