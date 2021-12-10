import subprocess
import time
import RPi.GPIO as GPIO
import serial 

#Connect to Spike
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

while True:
    print(ser.readline())
    time.sleep(1)