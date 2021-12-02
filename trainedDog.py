import subprocess
import time
import adafruit_vl53l0x
import RPi.GPIO as GPIO

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
    ser.write('m3.run_to_position(90)\r\n'.encode())
    ser.write('m4.run_to_position(-90)\r\n'.encode())

def runStand():
    ser.write('m3.run_to_position(0)\r\n'.encode())
    ser.write('m4.run_to_position(0)\r\n'.encode())

def runCome():
    ser.write('m1.pwm(30)\r\n'.encode())
    ser.write('m2.pwm(-30)\r\n'.encode())
    lidarReading = vl53.range
    while (lidarReading < 20):
        time.sleep(.1)
        lidarReading = vl53.range

def runSpin():
    ser.write('m1.pwm(50)\r\n'.encode())
    ser.write('m2.pwm(-10)\r\n'.encode())


output = subprocess.run(['python3', 'listen.py'], capture_output=True)
ready = output.stdout.decode('ascii')
readyList = ready.split("\n")

if "sit" in readyList:
    runSit()
elif "stand" in readyList:
    runStand()
elif "come" in readyList:
    runCome()
elif "spin" in readyList:
    runSpin()
    time.sleep(1)

