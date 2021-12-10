'''
dogTraining.py
Date Created: 12/01/21 
Last Edited: 12/01/21
Authors: Sawyer Paccione, 
Description: TODO
'''

from os import name
import serial
import time
import subprocess
import random

class RobotDog:
    def __init__(self):

        self.wordBank   = ['down', 'come', 'spin']
        self.weightDict = {}

        self.lastAction = None # a string in wordBank

        for word in self.wordBank:
            self.weightDict[word] = [0.33, 0.33, 0.33]

        self.updateWeight = 0.05

        random.seed()

        self.setupSerial()

        self.initializeSpike()

    def initializeSpike(self):
        print("initializing SPike")

        self.ser.write('\x03\r\n'.encode())
        self.ser.write('import hub\r\n'.encode())
        self.ser.write('m1 = hub.port.F.motor\r\n'.encode())
        self.ser.write('m2 = hub.port.E.motor\r\n'.encode())
        self.ser.write('m3 = hub.port.D.motor\r\n'.encode())
        self.ser.write('m4 = hub.port.C.motor\r\n'.encode())

        self.ser.write('m1.pwm(0)\r\n'.encode())
        self.ser.write('m2.pwm(0)\r\n'.encode())
        self.ser.write('m3.pwm(0)\r\n'.encode())
        self.ser.write('m4.pwm(0)\r\n'.encode())
        # print("here")
        
        # self.ser.write('hub.sound.beep()\r\n'.encode())

        time.sleep(2)

    def setupSerial(self):
        '''
        Setup the serial connection to the SPike PRIME via the microUSB port
        '''
        print("Setup Serial")
        # Connect to Spike
        self.ser = serial.Serial(
            port='/dev/ttyACM0',
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

    def selfTrain(self):
        '''
        Set the weights for each word to the perfectly trained states
        '''
        self.weightDict['down'] = [1,0,0]
        self.weightDict['come'] = [0,1,0]
        self.weightDict['spin'] = [0,0,1]

    def updateWeights(self, word, action, good):
        '''
        Updates the weights associated with the word given by the user. Increasing the weight of the action
        the dog choose, and decreasing the weights of every other action. good is either 1 or -1, 1 is good, -1 is bad
        '''
        weightList  = self.weightDict[word]
        updateIndex = self.wordBank.index(action)

        print("Original Weights", weightList)

        if weightList[updateIndex] >= 1:
            print(word, "is trained!")
        else: 
            for index in range(len(weightList)):
                # Update the weights in the list of the specified key
                if index == updateIndex:
                    weightList[index] += self.updateWeight * good
                else :
                    weightList[index] -= (self.updateWeight / 3) * good

                if weightList[index] < 0:
                    weightList[index] = 0
                elif weightList[index] > 1:
                    weightList[index] = 1

            self.weightDict[word] = weightList

        print("New Weights", weightList)

    def chooseAction(self, word):
        '''
        Choose an action given the weights of the word, return the action chosen
        '''
        weightList = self.weightDict[word]
        
        randNum = random.random()

        if randNum < weightList[0]:
            self.down()
            return "down"
        elif randNum < weightList[0] + weightList[1]:
            self.come()
            return "come"
        elif randNum < 1:
            self.spin()
            return "spin"

        return 'confused'

    def checkPraised(self):
        '''
        Call a file on the SPIKE that waits five seconds to get a press on the force sensor
        '''
        self.ser.write('\x03\r\n'.encode())

        self.ser.read(1000)

        self.ser.write('exec(open("awaitPraise.py").read())\r\n'.encode())
        line = ''

        while ("True" not in line) and "False" not in line:
            line = self.ser.readline().decode('utf-8')
            # print("Line:", line)
            # print("True" not in line)
            time.sleep(0.1)

        self.stand()

        time.sleep(2)
        
        if "True" in line:
            return True
        else:
            return False

    def listen(self):
        self.ser.write('hub.sound.beep()\r\n'.encode())
        output = subprocess.run(['python3', 'listen.py'], capture_output=True)
        ready = output.stdout.decode('ascii')
        readyList = ready.split("\n")
        print("Listening")

        if "down" in readyList:
            return "down"
        elif "come" in readyList:
            return "come"
        elif "spin" in readyList:
            return "spin"

    def down(self):
        # print("Executing: down")
        self.ser.write('m3.run_to_position(90, 60)\r\n'.encode())
        self.ser.write('m4.run_to_position(-90, 60)\r\n'.encode())

    def stand(self):
        # print("Executing: stand")
        self.ser.write('m3.run_to_position(0, 70)\r\n'.encode())
        self.ser.write('m4.run_to_position(0, 70)\r\n'.encode())

    def come(self):
        self.stand()
        time.sleep(1)
        self.ser.write('exec(open("come.py").read())\r\n'.encode())

    def spin(self):
        # print("Executing: spin")
        self.stand()
        time.sleep(1)
        self.ser.write('m1.pwm(50)\r\n'.encode())
        self.ser.write('m2.pwm(50)\r\n'.encode())
        time.sleep(2.8)
        
        self.ser.write('m1.pwm(0)\r\n'.encode())
        self.ser.write('m2.pwm(0)\r\n'.encode())

if __name__ == '__main__':
    try:
        while True:
            output = subprocess.run(['python3', 'listen.py'], capture_output=True)
            ready = output.stdout.decode('ascii')
            readyList = ready.split("\n")
    except KeyboardInterrupt:
        print("Interrupted")

