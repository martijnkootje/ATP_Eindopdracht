from zonneSensor import *
from magnetoSensor import *
from servo import *
from motor import *
from cppFunctions import *
from led import *
import time
import math
import matplotlib.pyplot as plt

#Pybind11 imported classes
zonneSensor = zonnePositieSensor()
magnetoSensor = magnetoSensor()
servo = Servo()
motor = Motor()
led = Led()

#not working decorator for testing functions with extreme and negative values
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

#Logger decorator, logs the function name and return value
def logger(function):
    def functie(*args, **kwargs):
        tme = time.ctime()
        result = function(*args, **kwargs)
        print(str(tme) + "; Function: "+ function.__name__ + "; retrun value: ")#+ str(result) + "\n"
        return result
    return functie

#Timer decorator, logs the time a function took to run in milisecs
def timer(function):
    def functie(*args, **kwargs):
        tme = time.ctime()
        start = time.time_ns()
        result = function(*args, **kwargs)
        stop = time.time_ns()
        total = (stop-start)/1000000
        print(str(tme) + "; Function: "+ function.__name__ + "; Runtime: "+ str(total) + "\n")
        return result
    return functie

def updateZonneSensor(hoekA, hoekE, positive):
    if positive:
        hoekA += 1.6
        hoekE += 0.4
    else:
        hoekA -= 1.6
        hoekE -= 0.4
    return hoekA, hoekE

#Get the mangnetosensor values from the simulated sensor
def getMagnetoSensorValues():
    x, y = magnetoSensor.getConvertedSensorValues() #This is a function I would normally have written in python,
                                                    # read choise 1 in the attached document to see why it is in c++
    return x, y

#This function converts the x and y value, obtained from te sensor, to an elevation agle
def magnetoSensorValuesToAngle(x, y):
    direction = float(math.atan2(y, x))
    if direction < 0:
        direction += 2*math.pi
    if direction > 2*math.pi:
        direction -= 2*math.pi

    return int(direction*180/math.pi)

#Recursive function that returns the index of the highst value in a list
def highestValueIndex(sensoren, index=0,  max=0, highest=0):
    if sensoren[index] > max:
        if sensoren[index] < 1:
            sensoren[index] = 1 #for the next calculation sensors cant be 0
        max = sensoren[index]
        highest = index
    if index == 3: #above sensor
        return highest
    return highestValueIndex(sensoren, index+1, max, highest)

#Convert the 5 sensor values to an azimut and elevation angle
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

#this function returns the direction and state of the motor, calculated with the current angle and wanted angle
def motorDirectionAndState(currentPositionA, sunPositionA):
    state = False
    direction = False

    if sunPositionA - currentPositionA < 1 and sunPositionA - currentPositionA > -1:
        state = False
    elif sunPositionA < currentPositionA:
        if (sunPositionA - currentPositionA) < 180:
            direction = True
        else:
            direction = False
        state = True
    else:
        if (sunPositionA - currentPositionA) < 180:
            direction = False
        else:
            direction = True
        state = True
    return state, direction

#Updating sensor values (because of the simulation) !!This function is not functional!!
def updateSensors(currentA, currentE, currentPositionA, currentPositionE, positive):
    magnetoSensor.setCurrentPosition(int(currentPositionA))
    magnetoSensor.update()

    nextPositionA, nextPositionE = updateZonneSensor(currentA, currentE, positive)
    zonneSensor.setSunPosition(int(nextPositionA), int(nextPositionE))
    return nextPositionA, nextPositionE

#Read all sensorvalues from the sensors !!This function is not functional!!
def readSensorValues():
    sensorvalues = zonneSensor.getADCvalues()
    magnetoX, magnetoY = getMagnetoSensorValues()
    return sensorvalues, magnetoX, magnetoY

def Mainloop(lst=[[],[],[],[]], currentA=8, currentE=2, currentSunPointerA=0, currentSunPointerE=0, positive=True):

    if motor.status() == 1:
        if motor.direction() == 1:
            currentSunPointerA -= 2
        else:
            currentSunPointerA += 2

    if currentSunPointerA < 0:
        currentSunPointerA += 360

    if currentE < 1 or currentA < 1 or currentA > 356 or currentE > 88:
        positive = not positive

    currentA, currentE = updateSensors(currentA, currentE, currentSunPointerA, currentSunPointerE, positive)

    sensorValues, magnetoX, magnetoY = readSensorValues()

    #Calculate the azimut and elevation agle from the values of the sunpositionsensor and the magnetosensor
    magnetoA = magnetoSensorValuesToAngle(magnetoX, magnetoY)
    sunPositionA, sunPositionE = zonneSensorValuestoAngles(sensorValues)
    state, direction = motorDirectionAndState(magnetoA, sunPositionA)

    #update servo
    servo.toPosition(int(sunPositionE))
    currentSunPointerE = sunPositionE

    #update motor direction and state
    motor.setDirection(direction)
    if state:
        motor.turnON()
        led.turnOFF()
    else:
        motor.turnOFF
        led.turnON()

    lst[0].append(int(currentSunPointerA))
    lst[1].append(int(currentSunPointerE))
    lst[2].append(int(currentA))
    lst[3].append(int(currentE))

    if len(lst[0]) > 600:
        return lst

    return Mainloop(lst, currentA, currentE, currentSunPointerA, currentSunPointerE, positive)

def RunSimulation():
    result = Mainloop()
    time = list(range(0, 601))
    plt.plot(time, result[0])
    plt.plot(time, result[1])
    plt.plot(time, result[2])
    plt.plot(time, result[3])
    plt.xlabel("Time(cycles)")
    plt.ylabel("Value(degrees)")
    plt.show()

RunSimulation()