#!/bin/bash
# Shell script for DWM1001-DEVKIT

# Set USB port number use for UART communication
MY_DEV=$1

# Double Enter within 1 second transfers Generic mode to Shell mode in UART interface
# Try 3 times to change to Shell mode robustly
echo -en "\r" > $MY_DEV
echo -en "\r" > $MY_DEV
sleep 2
echo -en "\r" > $MY_DEV
echo -en "\r" > $MY_DEV
sleep 2
echo -en "\r" > $MY_DEV
echo -en "\r" > $MY_DEV
sleep 2

# "lec" command is for showing distances to ranging anchors and the postion if location engin is enabled.
# Sending this command multiple times will turn on/off this functionality.
echo -en "lec" > $MY_DEV
sleep 1
echo  -en "\r" > $MY_DEV

