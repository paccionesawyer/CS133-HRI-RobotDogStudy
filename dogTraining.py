'''
dogTraining.py
Date Created: 12/01/21 
Last Edited: 12/01/21
Authors: Sawyer Paccione, 
Description: TODO
'''

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
            

    def sit(self):
        # Todo
        pass

    def stand(self):
        # Todo
        pass

    def come(self):
        # Todo
        pass

    def spin(self):
        # Todo
        pass




