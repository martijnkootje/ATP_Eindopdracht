from zonneSensor import *
from magnetoSensor import *
from servo import *
from motor import *
from cppFunctions import *

zonneSensor = zonnePositieSensor()
magnetoSensor = magnetoSensor()
servo = Servo()

# print(zonneSensor.inputSensorValues())
magnetoSensor.update()

def updateZonneSensor(hoekA, hoekE):
    hoekA += 1
    hoekE += 0.3
    return hoekA,hoekE

def getMagnetoSensorValues():
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

def updateMotor():



def Mainloop():
    zonnehoekA = 0
    zonnehoekE = 0
    zonnewijzerhoekA = 0
    zonnewijzerhoekE = 0

    while(True):
        zonnehoekA, zonnehoekE = updateZonneSensor(hoekA, hoekE)
        x,y = getMagnetoSensorHoek()
        zonnewijzerhoekA = AzimutAngle(x,y) #function in c++
        zonnewijzerhoekE = Servo.getPosition()




