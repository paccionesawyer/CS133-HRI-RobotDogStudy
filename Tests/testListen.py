import subprocess
import time

output = subprocess.run(['python3', 'listen.py'], capture_output=True)
ready = output.stdout.decode('ascii')
readyList = ready.split("\n")
print(readyList)
if "sit" in readyList:
    print("sit")
elif "stand" in readyList:
    print("stand")
elif "come" in readyList:
    print("come")
elif "spin" in readyList:
    print("spin")

    time.sleep(1)   