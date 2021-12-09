import unittest
from dogTraining import RobotDog

dog = RobotDog()

class testRobotDog(unittest.TestCase):

    def test_setupSerial(self):
        dog.setupSerial()
        # self.assertEqual()
    
    def test_increaseWeights(self):
        dog.updateWeights("sit","sit",1)
        weights = {
            'sit' : [0.25,0,0,0],
            'stand' : [0,1,0,0],
            'come' : [0,0,1,0],
            'spin' : [0,0,0,1],
        }
        self.assertEqual([0])

    
    def test_selfTrain(self):
        dog.selfTrain()
        weights = {
            'sit' : [1,0,0,0],
            'stand' : [0,1,0,0],
            'come' : [0,0,1,0],
            'spin' : [0,0,0,1],
        }
        self.assertEqual(dog.weightDict, weights)

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()