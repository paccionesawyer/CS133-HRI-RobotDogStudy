'''
dogTraining.py
Date Created: 12/01/21 
Last Edited: 12/01/21
Authors: Sawyer Paccione, 
Description: TODO
'''

#Connect to Spike
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

class RobotDog:
    def __init__(self):

        self.wordBank   = ['sit', 'stand', 'come', 'spin']
        self.weightDict = {}

        self.lastAction = None # a string in wordBank

        for word in self.wordBank:
            self.weightDict[word] = [0.25, 0.25, 0.25, 0.25]

        self.updateWeight = 0.05

    def updateWeights(self, word):
        weightList  = self.weightDict[word]
        updateIndex = self.wordBank.index(word)

        if weightList[updateIndex] >= 1:
            print(word, "is trained!")
        else: 
            for index in range(weightList):
                # Update the weights in the list of the specified key
                if index == updateIndex:
                    weightList[index] += self.updateWeight
                weightList[index] -= self.updateWeight / 3

            self.weightDict[word] = weightList
            
    def listen(self):
        output = subprocess.run(['python3', 'listen.py'], capture_output=True)
        ready = output.stdout.decode('ascii')
        readyList = ready.split("\n")
        if "sit" in readyList:
            return "sit"
        elif "stand" in readyList:
            return "stand"
        elif "come" in readyList:
            return "come"
        elif "spin" in readyList:
            return "spin"

    def sit(self):
        ser.write('m3.run_to_position(90)\r\n'.encode())
        ser.write('m4.run_to_position(-90)\r\n'.encode())
        pass

    def stand(self):
        ser.write('m3.run_to_position(0)\r\n'.encode())
        ser.write('m4.run_to_position(0)\r\n'.encode())
        pass

    def come(self):
        ser.write('m1.pwm(30)\r\n'.encode())
        ser.write('m2.pwm(-30)\r\n'.encode())
        lidarReading = vl53.range
        while (lidarReading < 20):
            time.sleep(.1)
            lidarReading = vl53.range
        pass

    def spin(self):
        ser.write('m1.pwm(50)\r\n'.encode())
        ser.write('m2.pwm(-10)\r\n'.encode())
        pass




