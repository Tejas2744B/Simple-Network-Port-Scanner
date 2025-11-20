# 🌐 Simple Network Port Scanner

This project is a basic command-line tool built using Python's standard `socket` library to scan a specified host for open TCP ports. It serves as an introduction to **network security fundamentals** and the concept of **port enumeration**.

This project was developed as a solution for **Task 4: Simple Network Port Scanner**.

## ⚠️ ETHICAL HACKING WARNING: AUTHORIZED USE ONLY

**The primary and mandatory rule of using this tool is to scan only targets that you explicitly own or for which you have written, unambiguous authorization from the owner.**

* **Scanning unauthorized networks is illegal, unethical, and can lead to severe penalties.**
* This tool is provided for **educational purposes** only: to understand network protocols, socket programming, and basic security concepts.
* By using this tool, you take full responsibility for its deployment.

## ✨ Features

* **Customizable Range:** Allows the user to specify a start and end port number (1-65535).
* **Timeout Mechanism:** Implements a connection timeout (`DEFAULT_TIMEOUT = 1.0s`) using `socket.settimeout()` to prevent the scanner from hanging indefinitely on filtered or closed ports.
* **Service Description:** Outputs a simple description for common ports (e.g., 80 is HTTP, 443 is HTTPS).
* **Robust Error Handling:** Catches `socket.gaierror` (hostname resolution failure) and other connection errors.

## ⚙️ Requirements & Installation

### Prerequisites

* Python 3.x (Uses standard library only)

### Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YourUsername/simple-port-scanner.git](https://github.com/YourUsername/simple-port-scanner.git)
    cd simple-port-scanner
    ```

2.  **No external dependencies are required.**

## 💻 Usage

Run the script directly from your terminal:

```bash
python port_scanner.py