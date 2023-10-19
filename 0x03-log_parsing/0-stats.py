#!/usr/bin/python3
import re
import sys
import signal
from collections import defaultdict

# Define the regular expression pattern to match the input format
pattern = r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)'

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = defaultdict(int)

# Function to print statistics
def print_statistics():
    print(f'Total file size: File size: {total_file_size}')
    for status_code in sorted(status_code_counts.keys()):
        print(f'{status_code}: {status_code_counts[status_code]}')

# Function to handle CTRL + C (KeyboardInterrupt)
def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

line_count = 0
try:
    for line in sys.stdin:
        line = line.strip()
        # Use regular expression to match the input format
        match = re.match(pattern, line)
        if match:
            # Extract data from the match
            status_code = int(match.group(3))
            file_size = int(match.group(4))

            # Update metrics
            total_file_size += file_size
            status_code_counts[status_code] += 1

            line_count += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print_statistics()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_statistics()

