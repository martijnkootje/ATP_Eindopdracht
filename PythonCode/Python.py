from zonneSensor import *
from magnetoSensor import *
from servo import *
from motor import *
from cppFunctions import *

zonneSensor = zonnePositieSensor()
magnetoSensor = magnetoSensor()
servo = Servo()
motor = Motor()

# print(zonneSensor.inputSensorValues())
magnetoSensor.update()

def updateZonneSensor(hoekA, hoekE):
    hoekA += 1
    hoekE += 0.3
    return hoekA,hoekE

def getMagnetoSensorValues():
    sensorX = [0, 0]
    sensorY = [0, 0]
    print(type(sensorX))
    sensorX[0] = magnetoSensor.I2Cread(0x3d, 0x00)
    sensorX[1] = magnetoSensor.I2Cread(0x3d, 0x01)

    sensorY[0] = magnetoSensor.I2Cread(0x3d, 0x02)
    sensorY[1] = magnetoSensor.I2Cread(0x3d, 0x03)

    x = SensorValueToInt(sensorX) #function in c++
    y = SensorValueToInt(sensorY) #function in c++

    return x, y

def updateServo(zonnehoekE, zonnewijzerhoekE):
    if not zonnehoekE == zonnewijzerhoekE:
        servo.toPosition(zonnehoekE)

def updateMotor(zonnewijzerhoekA, zonnehoekA):
    if zonnehoekA == zonnewijzerhoekA:
        motor.turnOFF()
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
    zonnehoekA = 0
    zonnehoekE = 0
    zonnewijzerhoekA = 0
    zonnewijzerhoekE = 0

    while(True):
        zonnehoekA, zonnehoekE = updateZonneSensor(zonnehoekA, zonnehoekE)
        x,y = getMagnetoSensorValues()
        zonnewijzerhoekA = AzimutAngle(x,y) #function in c++
        zonnewijzerhoekE = Servo.getPosition()


        updateServo(zonnehoekE, zonnewijzerhoekE)
        updateMotor(zonnewijzerhoekA, zonnehoekA)


Mainloop()

