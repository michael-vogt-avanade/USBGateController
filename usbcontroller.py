#==============================================================================================
#==============================================================================================
#==============================================================================================
# 2023Apr27 mcvogt 952/917-9366 michael.vogt@avanade.com
# using code from...
# 4.0 out of 5 stars Inaccurate description. Required me to go hunting for the real directions.
# Reviewed in the United States on July 14, 2022
# Verified Purchase
# The product description is wrong. Like another reviewer, I found after googling the name of one of the ICs on the PCB that the actual "on" command is "A0 01 01 A2" and the off command is "A0 01 00 A1".

# 2023Apr29 mike added pip install pyserial to make sure could import serial
#           mike added pip install pytime to make sure could import time
# mike dusted off best practice for creating venv inside python for WindowsOS
# https://docs.python.org/3/library/venv.html
# c:\>python -m venv c:\path\to\myenv
# or
# python<version> -m venv <virtual-environment-name>

# pip freeze > requirements.txt
# pip install -r requirements.txt


# tailored for USBGATECONTROLLER
# c:\>python -m venv C:\Development\Github.com\USBGateController\envUSBController
# C:\> <venv>\Scripts\activate.bat
# deactivate 

# git config --global user.email "you@example.com"
# git config --global user.name "Your Name"
  
# git config --global user.email "michael.vogt@avanade.com"
# git config --global user.name "michael-vogt-avanade"

# a better source... https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/#:~:text=Python's%20official%20documentation%20says%3A%20%22A,one%20which%20is%20installed%20as
# "A virtual environment is a Python environment such that the Python interpreter, libraries and 
# scripts installed into it are isolated from those installed in other virtual environments, and 
# (by default) any libraries installed in a “system” Python, i.e., one which is installed as part 
# of your operating system"





#-------------------------------------------------------------------------------------------
# Below is a python script that I was able to control the relay with on CentOS

# Controls USB relay from Amazon to restart a Delphi P0, P1, P2 via wires
# attached to the power button
#
# Tested with Python 3.6.8
#
# https://www.amazon.com/gp/product/B07RJXCKV2/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1
# Product model E-3
# Communication chip CH340
# Communication protocol Serial port communication
# Communication format (9600, 8, NONE, 1)
# Baud rate 9600, 8 bits, no parity, 1 stop bit    typical 9600-8N1
# Weight Approx. 17g
# NOTE Use serial port assistant to send 0xAA, the relay keeps opening; Send 0xBB, the relay keeps closing; Send 0xCC, the relay works for 1 second then stop (Jog)

import serial
import time

ser = serial.Serial('/dev/ttyUSB4',9600) # open serial port
print(ser)
ON = bytes.fromhex("A0 01 01 A2")
OFF = bytes.fromhex("A0 01 00 A1")
ser.write(ON)
time.sleep(2)
ser.write(OFF)
ser.close()


