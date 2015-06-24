# RFIDler-HID26-BruteForce

This is a proof of concept of HID26 Bruteforce. Just to demo how easy to play RFID system with RFIDler using Python.  

Currently this script need to know the HID site code and ID number in advance. In addition, for site code begin with number 0.  Please use "result, data=rfidler.command("emu " + str(0) + s);"  Since Number begin with 0, will be interpreted as Octal in python. 

Usage:

e.g:  python BruteHID.py /dev/ttyACM0 12387654

Video Demo: 

For video demo please visit: https://youtu.be/3o3-Oo1geJ4
