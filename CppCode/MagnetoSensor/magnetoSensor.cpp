#define _USE_MATH_DEFINES

#include <iostream>
#include <pybind11/pybind11.h>
#include "magnetoSensor.h"
#include "math.h"
namespace py = pybind11;

magnetoSensor::magnetoSensor() {

}

void magnetoSensor::update() {

    int hoek = measurement;

    float radialen = (float) hoek/(float)180*(float)M_PI;

    float gainx = (rand() % 100)-50 / gain*25;
    float gainy = (rand() % 100)-50 / gain*25;
    float gainz = (rand() % 100)-50 / gain*25;

    int x = cos(radialen)*((float)60-gainx)*gain;
    int y = sin(radialen)*((float)60-gainy)*gain;
    int z = (rand() % 600) *((float)60-gainz)*gain; //z is not used for this project, so I cant simulate a real value

    x2 = (int8_t) (x & 0xFF);
    x1 = (int8_t) ((x >> 8) & 0xFF);

    y2 = (int8_t) (y & 0xFF);
    y1 = (int8_t) ((y >> 8) & 0xFF);

    z2 = (int8_t) (z & 0xFF);
    z1 = (int8_t) ((z >> 8) & 0xFF);

    dataReady = true;

    //todo verwerken van gebruik van instellingen
}

uint8_t magnetoSensor::I2C_readRegister(int address, int internalAddres) {

    if(address != 0x3d){
        return 0
    }

    if(internalAddres ==  0x00) {
        return x1;
    }
    if(internalAddres ==  0x01) {
        return x2;
    }

    if(internalAddres == 0x02) {
        return z1;
    }
    if(internalAddres == 0x03) {
        return z2;
    }

    if(internalAddres == 0x04) {
        return y1;
    }
    if(internalAddres == 0x05) {
        return y2;
    }
    return 0;
}

int magnetoSensor::I2C_writeRegister(int address, uint8_t data) {
    //todo instellngen aanpassen
    uint8_t data1 = data;
    if(address == 0x00){
        uint8_t optionGain = ((data1 >> 5) & 0); //Get the last 3 bits (gain bits)
        gain = optionGain;

        data1 = data;
        uint8_t optionOperatingMode = ((data1) & 0x01); //Get the first 5 bits (operationmode bits)
        operating = optionOperatingMode;
    }
    return 1;
}


void magnetoSensor::setMeasueredValue(int angle) {
    measurement = angle;
}

PYBIND11_MODULE(magnetoSensor, m) {
    m.doc() = "magnetoSensor";
    py::class_<magnetoSensor>(m, "magnetoSensor")
        .def(py::init<>())
        .def("setMeasurement", &magnetoSensor::setMeasueredValue, "Set the input angle, simulated by the sensor")
        .def("I2Cread", &magnetoSensor::I2C_readRegister, "Read registers from the sensor")
        .def("I2Cwrite", &magnetoSensor::I2C_writeRegister, "Write in the registers of the sensor")
        .def("update", &magnetoSensor::update, "Do a 'new measurement', the sensor uses the angle set with 'setMeasurement'");
}