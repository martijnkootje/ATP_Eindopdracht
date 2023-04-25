import random
import unittest
from zonneSensor import *
from magnetoSensor import *
from servo import *
from motor import *
from cppFunctions import *
import Python


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
    def test_zonne_sensor_input_to_value_90degrees_elevation(self):
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


#integration tests
#For testing all functions in and around the sensors. Test cases will show if the
#simulations and the functions that calculate values from the sensors work correctly
class TestSensors(unittest.TestCase):

    #testing the import of c++ modules in python before running tests with them
    def test_cpp_includes(self):
        zonneSensor = zonnePositieSensor()
        magneto = magnetoSensor()
        servo = Servo()
        motor = Motor()

        self.assertIsInstance(zonneSensor, zonnePositieSensor)
        self.assertIsInstance(magneto, magnetoSensor)
        self.assertIsInstance(servo, Servo)
        self.assertIsInstance(motor, Motor)

    #Testing the working of the magnetosensor(simulator) and functions that calculate the angles from the sensor values
    def ZonneSensor(self, zonneSensor, a, e):
        zonneSensor.setSunPosition(a, e)
        sensorvalues = zonneSensor.getADCvalues()
        azi, ele = Python.zonneSensorValuestoAngles(sensorvalues)
        return ((a - azi) < 12 and (a - azi) > -12) and ((e - ele) < 6 and (e - ele) > -6)

    def test_zonne_sensor_normal_values(self):
        zonneSensor = zonnePositieSensor()
        result = []
        for a in range(360):
            e = int(a/4)
            result.append(self.ZonneSensor(zonneSensor, a, e))
        print(result)
        self.assertTrue(min(result) == 1)

    #Testing the working of the magnetosensor(simulator) and functions that calculate the angles from the sensor values
    def MagnetoSensor(self, magneto, a):
        magneto.setCurrentPosition(int(a)) #Give the sensor a angle it needs to simulate
        magneto.update()
        x,y = Python.getMagnetoSensorValues()
        azimut = Python.magnetoSensorValuesToAngle(x,y)
        return (((a - azimut) < 5 and (a - azimut) > -5))

    def test_magneto_sensor(self):
        magneto = magnetoSensor()
        result = []
        for a in range(360):
            result.append(self.MagnetoSensor(magneto, a))
        print(result)
        self.assertTrue(min(result) == 1)


#System test
class TestSystem(unittest.TestCase):

    def TestLoop(self, result, i=0, lst = []):
        if i == len(result[0]):
            return lst
        if (result[0][i] - result[2][i]) > 3 or (result[0][i] - result[2][i]) < -3:
            lst.append(0)
            return self.TestLoop(result, i+1, lst)
        if (result[1][i] - result[3][i]) > 3 or (result[1][i] - result[3][i]) < -3:
            lst.append(0)
            return self.TestLoop(result, i+1, lst)
        lst.append(1)
        return self.TestLoop(result, i+1, lst)

    #Test if the system does what it is suposed to do
    def test_sun_pointer(self):
        result = Python.Mainloop()
        testresult = self.TestLoop(result)
        score = sum(testresult)
        self.assertGreater(score, (len(testresult)*0.8))