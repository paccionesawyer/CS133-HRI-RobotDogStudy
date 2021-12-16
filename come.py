# Come Command
import hub 
import utime

m1 = hub.port.F.motor
m2 = hub.port.E.motor
m3 = hub.port.D.motor
m4 = hub.port.C.motor

ultrasonic = hub.port.B.device
dist = 1000000

m1.pwm(-50)
m2.pwm(50)

while True:
    try:
        dist = ultrasonic.get()[0]
        if dist <= 30:
            m1.pwm(0)
            m2.pwm(0)
            break
    except:
        pass
    
print("Dog Ready")