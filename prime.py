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

def runSit():
    ser.write('m3.run_to_position(90, 60)\r\n'.encode())
    ser.write('m4.run_to_position(-90, 60)\r\n'.encode())

def runStand():
    ser.write('m3.run_to_position(0, 60)\r\n'.encode())
    ser.write('m4.run_to_position(0, 60)\r\n'.encode())

def runCome():
    runStand()
    time.sleep(1)
    ser.write('exec(open("come.py").read())\r\n'.encode())

def runSpin():
    runStand()
    time.sleep(1)
    ser.write('m1.pwm(50)\r\n'.encode())
    ser.write('m2.pwm(50)\r\n'.encode())
    time.sleep(2.8)
    ser.write('m1.pwm(0)\r\n'.encode())
    ser.write('m2.pwm(0)\r\n'.encode())

while True:
    output = subprocess.run(['python3', 'listen.py'], capture_output=True)
    ready = output.stdout.decode('ascii')
    readyList = ready.split("\n")


    if "down" in readyList:
        runSit()
    elif "stand" in readyList:
        runStand()
    elif "come" in readyList:
        runCome()
    elif "spin" in readyList:
        runSpin()
    time.sleep(1)

