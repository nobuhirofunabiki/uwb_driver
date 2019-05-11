#!/usr/bin/python2.7

import serial
import os
import signal
import time

from serial import SerialException

def shutdown_q(dev,ser):
    def shutdown_handler(signum,frame):
        print "Shut down sequence"
        # sending command to DWM1001-DEVKIT
        # Sending 'lec' command multiple times will turn on/off the functionality of 'lec'.
        os.system('echo -e -n "lec" > ' + dev)
        os.system('echo -e -n "\r" > ' + dev)
        ser.close()
        exit()
    return shutdown_handler

ser = None
try:
    ser = serial.Serial('/dev/ttyACM0')
    ser.baudrate = 115200
except SerialException as error:
    print "Serial device is not found."
    exit()

# Display general information and open/close status of the serial port
print ser
print ser.is_open

# Run the shell script for DWM1001-DEVKIT
os.system("bash " + os.path.join(os.path.dirname(__file__),"dwm1001_logging.sh") + " " + '/dev/ttyACM0')

signal.signal(signal.SIGINT,shutdown_q('/dev/ttyACM0',ser))

print "Tag ready!"

while True:
    lines = ser.read(100)
    print(lines)
    time.sleep(1.0) 