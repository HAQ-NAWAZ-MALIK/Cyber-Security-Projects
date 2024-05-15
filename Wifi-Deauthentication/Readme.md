# Wi-Fi Deauthentication Utility

## Overview
This Wi-Fi Deauthentication Utility is a Bash script created for educational purposes. It provides functionalities to scan Wi-Fi networks, select a network for further actions, deauthenticate clients from a network, check Wi-Fi adapter status, and change the Wi-Fi adapter interface name.

## Disclaimer
**Disclaimer:** This tool is provided for educational purposes only. It should not be used for illegal activities. Only use it for legitimate penetration testing and security research purposes on network devices that you own or have permission to test. By using this tool, you agree to comply with all applicable laws and regulations.

## Prerequisites
- Linux environment
- Aircrack-ng suite installed (`airodump-ng`, `aireplay-ng`, etc.)
- Wi-Fi adapter compatible with Aircrack-ng tools

## Usage Instructions
1. Clone or download the repository to your Linux machine.
2. Open a terminal and navigate to the directory containing the script.
3. Make the script executable using `chmod +x wifi_deauth_utility.sh`.
4. Run the script using `./wifi_deauth_utility.sh`.
5. Follow the on-screen menu options to perform Wi-Fi network actions.

## Menu Options
- **1. Scan for Wi-Fi networks:** Initiates a scan for nearby Wi-Fi networks using `airodump-ng`.
- **2. Select a Wi-Fi network:** Allows you to select a specific Wi-Fi network for further actions.
- **3. Deauthenticate a client:** Deauthenticates a specific client from a selected Wi-Fi network using `aireplay-ng`.
- **4. Deauthenticate all clients:** Deauthenticates all clients from a selected Wi-Fi network using `aireplay-ng`.
- **5. Check Wi-Fi Adapter Status:** Displays the status of the Wi-Fi adapter using `iwconfig`.
- **6. Change Wi-Fi Adapter Interface Name:** Allows you to change the Wi-Fi adapter interface name dynamically.

## Important Notes
- Use this tool responsibly and only on networks you have permission to test.
- The author is not responsible for any misuse of this tool leading to legal consequences.
- Ensure compliance with applicable laws and obtain necessary permissions before using this tool.


## License
This Wi-Fi Deauthentication Utility is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
