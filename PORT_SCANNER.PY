import socket
import sys
from datetime import datetime

# --- Configuration ---
DEFAULT_TIMEOUT = 1.0  # seconds
COMMON_PORTS = {
    21: "FTP (File Transfer Protocol)",
    22: "SSH (Secure Shell)",
    23: "Telnet",
    25: "SMTP (Simple Mail Transfer Protocol)",
    53: "DNS (Domain Name System)",
    80: "HTTP (HyperText Transfer Protocol)",
    110: "POP3 (Post Office Protocol v3)",
    143: "IMAP (Internet Message Access Protocol)",
    443: "HTTPS (HTTP Secure)",
    3389: "RDP (Remote Desktop Protocol)",
    8080: "HTTP Proxy/Alternative HTTP"
}

# --- Core Logic ---

def scan_port(target_ip: str, port: int, timeout: float) -> bool:
    """
    Attempts to establish a connection to a specific port on the target IP.
    
    Args:
        target_ip: The IP address or hostname to scan.
        port: The port number to check.
        timeout: The connection timeout in seconds.
        
    Returns:
        True if the port is open, False otherwise.
    """
    try:
        # 1. Create a new socket object (AF_INET for IPv4, SOCK_STREAM for TCP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 2. Implement the timeout mechanism
        sock.settimeout(timeout)
        
        # 3. Attempt to connect
        result = sock.connect_ex((target_ip, port))
        
        # Check if the connection was successful (result == 0)
        if result == 0:
            return True
        else:
            return False
            
    except socket.gaierror:
        # Hostname resolution error (e.g., target IP/name is invalid)
        print("\n[!] Error: Hostname could not be resolved. Exiting.")
        sys.exit(1)
    except socket.error as e:
        # General socket error
        print(f"\n[!] Error: Could not connect to server. Details: {e}")
        sys.exit(1)
    finally:
        # Ensure the socket is closed whether connection succeeds or fails
        if 'sock' in locals():
            sock.close()

def get_port_range() -> tuple[int, int]:
    """Prompts the user for a valid start and end port."""
    while True:
        try:
            start_port = int(input("Enter starting port (e.g., 1): "))
            end_port = int(input("Enter ending port (e.g., 1024): "))
            
            if 0 < start_port <= end_port <= 65535:
                return start_port, end_port
            else:
                print("Invalid range. Ports must be between 1 and 65535, and start port must be <= end port.")
        except ValueError:
            print("Invalid input. Please enter numbers for the ports.")

def main():
    """Main function to run the port scanner tool."""
    print("-" * 50)
    print("🛡️ Simple Network Port Scanner Tool 🛡️")
    print("WARNING: Only scan targets you own or have explicit authorization for.")
    print("-" * 50)

    # Get user inputs
    target = input("Enter the target IP address or hostname: ")
    start_port, end_port = get_port_range()
    
    try:
        # Resolve hostname to IP for consistent output, but use the original target for input
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"[!] Error: Cannot resolve hostname '{target}'. Check the input.")
        return

    print(f"\nScanning target: {target_ip} (Range: {start_port}-{end_port})")
    print(f"Start Time: {datetime.now().strftime('%H:%M:%S')}")
    print("-" * 50)

    open_ports = []
    
    # Iterate through the range of ports
    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port, DEFAULT_TIMEOUT):
            service = COMMON_PORTS.get(port, "Unknown/Custom Service")
            open_ports.append((port, service))
            print(f"[+] Port {port:<5} is OPEN  | Service: {service}")
            
    print("-" * 50)
    if open_ports:
        print("✅ Scan Complete. Found Open Ports:")
        for port, service in open_ports:
            print(f"  > Port {port} ({service})")
    else:
        print("[-] Scan Complete. No open ports found in the specified range.")
    
    print(f"End Time: {datetime.now().strftime('%H:%M:%S')}")
    print("-" * 50)

if __name__ == "__main__":
    # Crucial ethical disclaimer
    print("\n\n*** ETHICAL HACKING NOTE ***")
    print("Scanning unauthorized networks is illegal and unethical. This tool is for educational purposes only.")
    input("Press Enter to continue (by doing so, you acknowledge the ethical warning):")
    main()