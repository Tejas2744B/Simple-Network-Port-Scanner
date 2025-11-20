# Simple-Network-Port-Scanner
Simple Network Port Scanner


Example Session
The script will first present a mandatory ethical warning before proceeding.

--- 🛡️ Simple Network Port Scanner Tool 🛡️
WARNING: Only scan targets you own or have explicit authorization for.
--------------------------------------------------


*** ETHICAL HACKING NOTE ***
Scanning unauthorized networks is illegal and unethical. This tool is for educational purposes only.
Press Enter to continue (by doing so, you acknowledge the ethical warning):

Enter the target IP address or hostname: 127.0.0.1
Enter starting port (e.g., 1): 20
Enter ending port (e.g., 100): 100

Scanning target: 127.0.0.1 (Range: 20-100)
Start Time: 21:50:00
--------------------------------------------------
[+] Port 22   is OPEN  | Service: SSH (Secure Shell)
[+] Port 80   is OPEN  | Service: HTTP (HyperText Transfer Protocol)
--------------------------------------------------
✅ Scan Complete. Found Open Ports:
  > Port 22 (SSH (Secure Shell))
  > Port 80 (HTTP (HyperText Transfer Protocol))
End Time: 21:50:02
--------------------------------------------------
🛠️ Implementation Details
The core functionality relies on the following steps for each port:

Socket Creation: socket.socket(socket.AF_INET, socket.SOCK_STREAM) creates a TCP socket.

Timeout Setting: sock.settimeout(timeout) limits the waiting time.

Connection Attempt: sock.connect_ex((target_ip, port)) attempts a non-blocking connection. A return value of 0 indicates the port is open.

Resource Cleanup: sock.close() ensures system resources are released.
