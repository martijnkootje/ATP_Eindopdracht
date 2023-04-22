import unittest
from zonneSensor import *
from magnetoSensor import *
from servo import *
from motor import *
from cppFunctions import *


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

#todo
#unit tests
#hiermee weet je dat de functies integerwarden accepteren(incliesf extreme waarden) zonder te crashen en dat aan de hand van
#de ingevgeven hoek op alle kanten van de sensor de waarde simulatie in ieder geval de goede kant de goede waarde teruggeeft
class TestSensorFunctions(unittest.TestCase):

    #   Test if the object type is correct and the object is created as the right type
    def test_creating_cpp_object(self):
        sensor = zonnePositieSensor()
        self.assertIsInstance(sensor, zonnePositieSensor)

    #   Test the calculation when sensor 0 has the highest value
    def test_zonne_sensor_input_to_value_5degrees(self):
        sensor = zonnePositieSensor()
        values = sensor.inputAngleToSensorValues(5, 0)
        result = values.index(max(values))
        self.assertEqual(result, 0)

    #   Test the calculation when sensor 1 has the highest value
    def test_zonne_sensor_input_to_value_95degrees(self):
        sensor = zonnePositieSensor()
        values = sensor.inputAngleToSensorValues(95, 0)
        result = values.index(max(values))
        self.assertEqual(result, 1)

    #   Test the calculation when sensor 2 has the highest value
    def test_zonne_sensor_input_to_value_185degrees(self):
        sensor = zonnePositieSensor()
        values = sensor.inputAngleToSensorValues(185, 0)
        result = values.index(max(values))
        self.assertEqual(result, 2)

    #   Test the calculation when sensor 3 has the highest value
    def test_zonne_sensor_input_to_value_275degrees(self):
        sensor = zonnePositieSensor()
        values = sensor.inputAngleToSensorValues(275, 0)
        result = values.index(max(values))
        self.assertEqual(result, 3)

    #   Test the calculation when sensor 4 (upper) has the highest value
    def test_zonne_sensor_input_to_value_5degrees(self):
        sensor = zonnePositieSensor()
        values = sensor.inputAngleToSensorValues(5, 90)
        result = values.index(max(values))
        self.assertEqual(result, 4)

    def test_zonne_sensor_input_to_value_handle_negative_values(self):
        sensor = zonnePositieSensor()
        try:
            values = sensor.inputAngleToSensorValues(-50, -90)
        except:
            self.assertTrue(False)

    def test_zonne_sensor_input_to_value_handle_extreme_positive_values(self):
        sensor = zonnePositieSensor()
        try:
            values = sensor.inputAngleToSensorValues(10000, 10000)
        except:
            self.assertTrue(False)

#integratie tests #toedoe toevoegen document en wiki
class TestSensoren():

def testSunSensor(a, e):
    zonneSensor.setSunPosition(a, e)
    sensorvalues = zonneSensor.getADCvalues()
    azi, ele = zonneSensorValuestoAngles(sensorvalues)
    assert (a - azi) < 5 and (a - azi) > -5, "expexted: " + str(a) + " got: " + str(azi) + "; Not the expected outcome"
    return "Test passed"
#todo allerlei waarden tesen, uiterste en errorgevoelige

def testMagnetoSensor(a):
    magnetoSensor.setCurrentPosition(int(currenthoekA)) #Give the sensor a angle it needs to simulate
    magnetoSensor.update()
    x,y = getMagnetoSensorValues()
    #assert ....#todo
    return "Test passed"