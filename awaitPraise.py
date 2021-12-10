import hub 
import utime

ForceSensor = hub.port.A.device

start_time = utime.ticks_ms()
curr_time = start_time
force = 0 

goodboy = False

while ((curr_time - start_time) < 10000):
    # print(curr_time - start_time)
    ForceSensor.mode(4)        # Force in RAW units
    force = ForceSensor.get()[0]
    curr_time = utime.ticks_ms()
    # print(force)
    if force > 500:
        goodboy = True
        break

if goodboy:
    print("True")
else:
    print("False")

hub.sound.beep()    