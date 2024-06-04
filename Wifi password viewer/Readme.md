# Wi-Fi Password Viewer

This Python script allows you to view the names and passwords of all the Wi-Fi networks that your computer has previously connected to. It uses the `subprocess` module to run the `netsh` command-line utility on Windows to retrieve the Wi-Fi profile information.

## Usage

1. Save the `wifi.py` file on your computer.
2. Open a command prompt or terminal window.
3. Navigate to the directory where the `wifi.py` file is located.
4. Run the script by typing `python wifi.py` and pressing Enter.

The script will output a table with two columns: "Wi-Fi Name" and "Password". The table will display the names of all the Wi-Fi networks and their corresponding passwords (if available).

## Requirements

This script is designed to work on Windows operating systems. It requires no additional dependencies beyond the standard Python library.

## How it Works

1. The script uses the `subprocess.check_output()` function to execute the `netsh wlan show profiles` command, which retrieves a list of all the Wi-Fi profiles on the system.
2. It then parses the output of the command to extract the Wi-Fi network names.
3. For each Wi-Fi network, the script runs the `netsh wlan show profile <network_name> key=clear` command to retrieve the password for that network.
4. The extracted network names and passwords are then formatted and printed in a tabular format.

Note: If a password is not available for a particular Wi-Fi network, the script will print an empty string in the "Password" column for that network.

## Disclaimer

This script is intended for educational and personal use only. Use it responsibly and ensure you have the necessary permissions before attempting to view Wi-Fi passwords on systems you do not own or have authorized access to.
