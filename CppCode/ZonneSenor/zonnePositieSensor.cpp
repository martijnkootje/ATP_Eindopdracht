#include "zonnePositieSensor.h"
#include <iostream>
#include "../../extern/pybind11/include/pybind11/pybind11.h"
#include "../../extern/pybind11/include/pybind11/stl.h"
namespace py = pybind11;

zonnePositieSensor::zonnePositieSensor(){

}

///\brief Function to get sensor values from the command line
std::array<int, 5> zonnePositieSensor::inputSensorValues() {
    std::cout << "voltage 1: ";
    std::string s1 = "";
    std::cin >> s1;

    std::cout << "voltage 2: ";
    std::string s2 = "";
    std::cin >> s2;

    std::cout << "voltage 3: ";
    std::string s3 = "";
    std::cin >> s3;

    std::cout << "voltage 4: ";
    std::string s4 = "";
    std::cin >> s4;

    std::cout << "voltage 5: ";
    std::string s5 = "";
    std::cin >> s5;

    int i1 = std::stoi(s1);
    int i2 = std::stoi(s2);
    int i3 = std::stoi(s3);
    int i4 = std::stoi(s4);
    int i5 = std::stoi(s5);

    return std::array<int, 5> {i1,i2,i3,i4,i5};
}

///\brief Function that converts an x and y coordinate from the commandline to random sensor input voltages
std::array<int, 5> zonnePositieSensor::inputAngleToSensorValues(int azimut, int elevatie){
    std::array<int, 5> sensors;

    if(azimut > 360){
        azimut -= 360;
    }else if(azimut < 0){
        azimut += 360;
    }

    float randomFactor = 0.5 * (rand() % 290 + 288) / 10.0;
    if(randomFactor < 0){
        randomFactor *= -1;
    }
    int highestSensor = 0;
    //s1 has highest value
    if(azimut >= 0 && azimut <= 90){
        if(azimut <= 45){
            sensors[0] = (90.0-((float)azimut))/90.0*100 * randomFactor + randomFactor;
            sensors[1] = (((float)azimut)/90.0*100) *randomFactor + randomFactor;
            sensors[2] = rand() % (int)randomFactor;
            sensors[3] = 1.5 * (rand() % (int)randomFactor);
        }else{
            highestSensor = 1;
            sensors[0] = (90.0-((float)azimut))/90.0*100 * randomFactor+ randomFactor;
            sensors[1] = (((float)azimut)/90.0*100) * randomFactor+ randomFactor;
            sensors[2] = rand() % (int)randomFactor;
            sensors[3] = 1.5 * (rand() % (int)randomFactor);
        }
    }else

    if(azimut > 90 && azimut <= 180){
        if(azimut <= 135){
            highestSensor = 1;
            sensors[1] = (90.0-((float)azimut-90.0))/90.0*100 * randomFactor + randomFactor;
            sensors[2] = (((float)azimut-90.0)/90.0*100) *randomFactor+ randomFactor;
            sensors[3] = rand() % (int)randomFactor;
            sensors[0] = 1.5 * (rand() % (int)randomFactor);
        }else{
            highestSensor = 2;
            sensors[1] = (90.0-((float)azimut-90.0))/90.0*100 * randomFactor + randomFactor;
            sensors[2] = (((float)azimut-90.0)/90.0*100) * randomFactor + randomFactor;
            sensors[3] = rand() % (int)randomFactor;
            sensors[0] = 1.5 * (rand() % (int)randomFactor);
        }
    }else

    if(azimut > 180 && azimut <= 270){
        if(azimut < 225){
            highestSensor = 2;
            sensors[2] = (90.0-((float)azimut-180.0))/90.0*100 * randomFactor+ randomFactor;
            sensors[3] = (((float)azimut-180.0)/90.0*100) *randomFactor+ randomFactor;
            sensors[1] = 1.5 * (rand() % (int)randomFactor);
            sensors[0] = rand() % (int)randomFactor;
        }else{
            highestSensor = 3;
            sensors[2] = (90.0-((float)azimut-180.0))/90.0*100 * randomFactor+ randomFactor;
            sensors[3] = (((float)azimut-180.0)/90.0*100) *randomFactor+ randomFactor;
            sensors[0] = rand() % (int)randomFactor;
            sensors[1] = 1.5 * (rand() % (int)randomFactor);
        }
    }else

    if(azimut > 270 && azimut <= 360){
        if(azimut < 315){
            highestSensor = 3;
            sensors[3] = (90.0-((float)azimut-270.0))/90.0*100 * randomFactor+ randomFactor;
            sensors[0] = (((float)azimut-270.0)/90.0*100) *randomFactor+ randomFactor;
            sensors[1] = 1.5 * (rand() % (int)randomFactor);
            sensors[2] = rand() % (int)randomFactor;
        }else{
            highestSensor = 0;
            sensors[3] = (90.0-((float)azimut-270.0))/90.0*100 * randomFactor+ randomFactor;
            sensors[0] = (((float)azimut-270.0)/90.0*100+2) *randomFactor+ randomFactor;
            sensors[1] = 1.5 * (rand() % (int)randomFactor);
            sensors[2] = rand() % (int)randomFactor;
        }
    }
    //upper sensor
    sensors[4] = ((float)sensors[highestSensor] / ((float)90.0-elevatie)) * elevatie;

    return sensors;
}

std::array<int, 5> zonnePositieSensor::getADCvalues() {
    return inputAngleToSensorValues(angleSunA, angleSunE);
}

void zonnePositieSensor::setCurrentSunPosition(int azimut, int elevatie) {
    angleSunA = azimut;
    angleSunE = elevatie;
}

PYBIND11_MODULE(zonneSensor, m) {
    m.doc() = "Zonnepositiesensor";
    py::class_<zonnePositieSensor>(m, "zonnePositieSensor")
        .def(py::init<>())
        .def("inputSensorValues", &zonnePositieSensor::inputSensorValues, "Fill in input values for the sensor")
        .def("inputAngleToSensorValues", &zonnePositieSensor::inputAngleToSensorValues, "Fill in 2 angles and this function returns 5 sensor values")
        .def("getADCvalues", &zonnePositieSensor::getADCvalues, "Get the current sensor values from the ADC registers")
        .def("setSunPosition", &zonnePositieSensor::setCurrentSunPosition, "Give the current position of the sun to the sensor(because of the simulation)");
}
