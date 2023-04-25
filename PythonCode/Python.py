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

# class NegativeNotHandledTester(object):
#     def __init__(self, function):
#         self.function = function
#
#     def __call__(self, *args, **kwargs):
#         for key in args:
#             print(key)
#         try:
#             self.result = self.function(*args, **kwargs)
#             return self.result
#         except:
#             raise AttributeError(f"fout")


# @NegativeNotHandledTester
# def hh(x, y):
#     return x * y


# print(hh(3, 2))


def logger(function):
    def functie(*args, **kwargs):
        tme = time.ctime()
        result = function(*args, **kwargs)
        print(str(tme) + "; Function: "+ function.__name__ + "; retrun value: ")#+ str(result) + "\n"
        return result
    return functie

def timer(function):
    def functie(*args, **kwargs):
        tme = time.ctime()
        start = time.time_ns()
        result = function(*args, **kwargs)
        stop = time.time_ns()
        total = (stop-start)/1000
        print(str(tme) + "; Function: "+ function.__name__ + "; Runtime: "+ str(total) + "\n")
        return result
    return functie

def updateZonneSensor(hoekA, hoekE):
    hoekA += 0.1
    hoekE += 0.3
    return hoekA, hoekE

def getMagnetoSensorValues():
    x, y = magnetoSensor.getConvertedSensorValues() #This is a function I would normally have written in python, read todo to see why it is in c++
    return x, y

def magnetoSensorValuesToAngle(x, y):
    direction = float(math.atan2(y, x))
    if direction < 0:
        direction += 2*math.pi
    if direction > 2*math.pi:
        direction -= 2*math.pi

    return int(direction*180/math.pi)

def highestValueIndex(sensoren, index=0,  max=0, highest=0):
    if sensoren[index] > max:
        if sensoren[index] < 1:
            sensoren[index] = 1 #for the next calculation sensors cant be 0
        max = sensoren[index]
        highest = index
    if index == 4: #above sensor
        return highest
    return highestValueIndex(sensoren, index+1, max, highest)

def zonneSensorValuestoAngles(sensoren):
    #calculate wich sensorvalue is highest
    index = highestValueIndex(sensoren)

    elevatie = float(sensoren[4]) / (float(sensoren[index]) + float(sensoren[4])) * 90
    azimut = 0

    #sensor 0 has the highest value
    if index == 0:
        if sensoren[index + 1] > sensoren[index + 3]:
            sTot = float(sensoren[index] + sensoren[index + 1])
            azimut = float(sensoren[index + 1]) / sTot * 90
        else:
            sTot = float(sensoren[index]) + float(sensoren[index + 3])
            azimut = float(sensoren[index + 3]) / sTot * -90

    #sensor 1 has the highest value
    if index == 1:
        if sensoren[index + 1] > sensoren[index - 1]:
            sTot = sensoren[index] + sensoren[index + 1]
            azimut = 90 + float(sensoren[index + 1]) / sTot * 90
        else:
            sTot = float(sensoren[index]) + float(sensoren[index - 1])
            azimut = 90 - float(sensoren[index - 1]) / sTot * 90

    #sensor 2 has the highest value
    if index == 2:
        if sensoren[index + 1] > sensoren[index - 1]:
            sTot = sensoren[index] + sensoren[index + 1]
            azimut = 180 + float(sensoren[index + 1]) / sTot * 90
        else:
            sTot = float(sensoren[index]) + float(sensoren[index - 1])
            azimut = 180 - float(sensoren[index - 1]) / sTot * 90

    #sensor 3 has the highest value
    if index == 3:
        if sensoren[0] > sensoren[index - 1]:
            sTot = sensoren[index] + sensoren[0]
            azimut = 270 + float(sensoren[0]) / sTot * 90
        else:
            sTot = float(sensoren[index]) + float(sensoren[index - 1])
            azimut = 270 - float(sensoren[index - 1]) / sTot * 90

    #making sure values are not negative or higher than 360
    if azimut < 0:
        azimut += 360
    if azimut > 360:
        azimut -= 360
    return azimut, elevatie

#verpl. mainloop
def updateServo(sunPositionE):
    servo.toPosition(int(sunAngleE))

def updateMotor(currentPositionA, sunPositionA):
    state = False
    direction = False

    if zonnehoekA - currentPositionA < 6 and zonnehoekA - currentPositionA > -6:
        state = False
    elif zonnehoekA < currentPositionA:
        if (zonnehoekA - currentPositionA) < 180:
            direction = True
        else:
            direction = False
        state = True
    else:
        if (zonnehoekA - currentPositionA) < 180:
            direction = False
        else:
            direction = True
        state = True
    return state, direction

#Updating sensor values (because of the simulation) !!This function is not functional!!
def updateSensors(currentA, currentE, currentPositionA, currentPositionE):
    magnetoSensor.setCurrentPosition(int(currentPositionA))
    magnetoSensor.update()

    nextPositionA, nextPositionE = updateZonneSensor(currentA, currentE) #todo labda
    zonneSensor.setSunPosition(int(nextPositionA), int(nextPositionE))
    return nextPositionA, nextPositionE

#Read all sensorvalues from the sensors !!This function is not functional!!
def readSensorValues():
    sensorvalues = zonneSensor.getADCvalues()
    magnetoX, magnetoY = getMagnetoSensorValues()
    currentAngleE = servo.getPosition()
    return sensorvalues, currentAngleE, magnetoX, magnetoY

def Mainloop(currentA=0, currentE=0, currentSunPointerA=0, currentSunPointerE=0):
    currentA, currentE = updateSensors(currentA, currentE, currentSunPointerA, currentSunPointerE)
    if motor.status() == 1:
        if motor.direction == 1:
            currentA -= 1
        else:
            currentA += 1

    sensorValues, currentAngleE, magnetoX, magnetoY = readSensorValues()

    #Calculate the azimut and elevation agle from the values of the sunpositionsensor and the magnetosensor
    currentSunPointerA = magnetoSensorValuesToAngle(magnetoX, magnetoY)
    currentSunPointerE = currentAngleE
    sunPositionA, sunPositionE = zonneSensorValuestoAngles(sensorValues)

    updateMotor(currentSunPointerA, sunPositionA)
    updateServo(sunPositionE)

    print("hoek zon azimut: " + str(zonnehoekA), "hoek sensor azimut: " + str(zonnewijzerhoekA))
    print("hoek zon elevatie: " + str(zonnehoekE), "hoek sensor elevatie: " + str(zonnewijzerhoekE) + "\n")
    time.sleep(3)
    return Mainloop(currentA, currentE, currentSunPointerA, currentSunPointerE)
    #todo recusrief maken en afmaken

def keuzemenu():
    print("Zonnewijzer simulatie en test software. "
          "\nOptie 1: voer de simulatie uit \nOptie 2: voer de tests uit \nOptie 3: exit")
    choice = input("Geef een optie: ")
    # try:
    if int(choice) == 1:
        Mainloop()
    if int(choice) == 2:
        pass
    if int(choice) == 3:
        return
    # except:
        print("Geef a.u.b. alleen een nummer")
    #todo afmaken simulatie en plotten
    #todo test voor logger en timer
    #todo logger / timer over cpp functie
    #todo map implementeren
    #todo document en dumentatie

keuzemenu()