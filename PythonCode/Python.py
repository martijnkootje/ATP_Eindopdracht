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

def logger(function):
    def functie(*args, **kwargs):
        tme = time.ctime()
        result = function(*args, **kwargs)
        print(str(tme) + "; Function: "+ function.__name__ + "; retrun value: "+ str(result) + "\n")
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

@timer
def highestValueIndex(sensoren, index=0,  max=0, highest=0):
    if sensoren[index] > max:
        if sensoren[index] < 1:
            sensoren[index] = 1 #for the next calculation sensors cant be 0
        max = sensoren[index]
        highest = index
    if index == 4:
        return highest
    return highestValueIndex(sensoren, index+1, max, highest)

@logger
def zonneSensorValuestoAngles(sensoren):
    #calculate wich sensorvalue is highest
    index = highestValueIndex(sensoren)

    elevatie = float(sensoren[4]) / (float(sensoren[index]) + float(sensoren[4])) * 90
    azimut = 0
    print(sensoren, index)

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

    if azimut < 0:
        azimut += 360
    if azimut > 360:
        azimut -= 360
    return azimut, elevatie


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
    #values for the simulation
    zonnehoekA = 45
    zonnehoekE = 45

    while(True):
        #updaten sensoren ivm simulatie
        magnetoSensor.setCurrentPosition(int(currenthoekA)) #Give the sensor a angle it needs to simulate
        magnetoSensor.update()
        zonnehoekA, zonnehoekE = updateZonneSensor(zonnehoekA, zonnehoekE)
        zonneSensor.setSunPosition(int(zonnehoekA), int(zonnehoekE)) #give the sensor a position of the sun to simulate


        #uitlezen sensorwaarden
        sensorvalues = zonneSensor.getADCvalues()
        x,y = getMagnetoSensorValues()
        currenthoekE = servo.getPosition()

        zonnewijzerhoekA = magnetoSensorValuesToAngle(x, y)
        zonneStandA, zonneStandE = zonneSensorValuestoAngles(sensorvalues)


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

        #todo testen toevoegen die zonnesensor input invullen op sensor en uitkomende waarde testen
        #todo test die invoerwaarden test (< 360 > 0

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

keuzemenu()


# for i in range(10):
#     testSunSensor(110, 45)