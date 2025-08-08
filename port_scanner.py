import socket
from datetime import datetime

def scan_ports(target, start_port, end_port):
    print(f"Starting scan on host: {target}")
    start_time = datetime.now()

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()

    end_time = datetime.now()
    print(f"Scan completed in: {end_time - start_time}")

if __name__ == "__main__":
    target_ip = input("Enter target IP address or hostname: ")
    scan_ports(target_ip, 1, 1024)
