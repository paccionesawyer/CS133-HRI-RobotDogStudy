

from DogTraining import RobotDog

if __name__ == '__main__':
    spike = RobotDog()

    
    try:
        while True:
            command = spike.listen()
            print("Command Heard:", command)

            action = spike.chooseAction(command)
            print("Random Action Chosen", action)

            praised = spike.checkPraised()

            if praised:
                spike.updateWeights(command, action, 1)
            else:
                spike.updateWeights(command, action, -1)

    except KeyboardInterrupt:
        print("Interrupted")