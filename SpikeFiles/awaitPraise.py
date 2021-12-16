import hub 
import utime

ForceSensor = hub.port.A.device

start_time = utime.ticks_ms()
curr_time = start_time
force = 0 

goodboy = False

while ((curr_time - start_time) < 5000):
    ForceSensor.mode(4)        # Force in RAW units
    force = ForceSensor.get()[0]
    curr_time = utime.ticks_ms()
    if force >= 500:
        goodboy = True
        break

if goodboy:
    print("True")
else:
    print("False")

# hub.sound.beep()    