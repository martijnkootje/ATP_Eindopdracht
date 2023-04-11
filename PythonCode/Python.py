from zonneSensor import *
from magnetoSensor import *
from servo import *
from motor import *
from cppFunctions import *
import time
import math

zonneSensor = zonnePositieSensor()
magnetoSensor = magnetoSensor()
servo = Servo()
motor = Motor()

#todo vervangen voor gebruik van zonnesenssor
def updateZonneSensor(hoekA, hoekE):
    hoekA += 0.1
    hoekE += 0.3
    return hoekA,hoekE

def getMagnetoSensorValues():
    lst = magnetoSensor.getConvertedSensorValues() #This is a function I would normally have written in python, read todo to see why it is in c++
    x = lst[0]
    y = lst[1]
    return x, y

def magnetoSensorValuesToAngle(x, y):
    direction = float(math.atan2(y, x))
    if direction < 0:
        direction += 2*math.pi
    if direction > 2*math.pi:
        direction -= 2*math.pi

    return int(direction*180/math.pi)

def updateServo(zonnewijzerhoekE, zonnehoekE):
    if not zonnehoekE == zonnewijzerhoekE:
        servo.toPosition(int(zonnehoekE))

def updateMotor(zonnewijzerhoekA, zonnehoekA):
    if zonnehoekA - zonnewijzerhoekA < 6 and zonnehoekA - zonnewijzerhoekA > -6:
        motor.turnOFF()
        #todo led aan
        return

    if zonnehoekA < zonnewijzerhoekA:
        if (zonnehoekA - zonnewijzerhoekA) < 180:
            motor.setDirection(1)
        else:
            motor.setDirection(0)

    if zonnehoekA > zonnewijzerhoekA:
        if (zonnehoekA - zonnewijzerhoekA) < 180:
            motor.setDirection(0)
        else:
            motor.setDirection(1)
    motor.turnON()


def Mainloop():
    zonnehoekA = 25
    zonnehoekE = 10
    currenthoekA = 0
    currenthoekE = 0
    zonnewijzerhoekA = 0
    zonnewijzerhoekE = 0

    while(True):
        #updaten sensoren ivm simulatie
        magnetoSensor.setMeasurement(int(currenthoekA)) #Give the sensor a angle it needs to simulate
        magnetoSensor.update()

        print(zonneSensor.inputAngleToSensorValues(350, 35))

        zonnehoekA, zonnehoekE = updateZonneSensor(zonnehoekA, zonnehoekE)

        #verwerking azimut
        x,y = getMagnetoSensorValues()
        zonnewijzerhoekA = magnetoSensorValuesToAngle(x, y)

        currenthoekE = servo.getPosition()
        #todo testen toevoegen die zonnesensor input invullen op sensor en uitkomende waarde testen
        #todo test die invoerwaarden test (< 360 > 0
        if motor.status() == 1:
            if motor.direction == 1:
                currenthoekA -= 1
                if currenthoekA < 0:
                    currenthoekA += 360
            else:
                currenthoekA += 1
                if currenthoekA > 360:
                    currenthoekA -= 360

        updateServo(zonnewijzerhoekE, zonnehoekE)
        updateMotor(zonnewijzerhoekA, zonnehoekA)

        print("hoek zon azimut: " + str(zonnehoekA), "hoek sensor azimut: " + str(zonnewijzerhoekA))
        print("hoek zon elevatie: " + str(zonnehoekE), "hoek sensor elevatie: " + str(zonnewijzerhoekE) + "\n")
        time.sleep(3)


Mainloop()

