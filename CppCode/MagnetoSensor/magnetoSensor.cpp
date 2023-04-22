#define _USE_MATH_DEFINES

#include <iostream>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
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


    x2[0] = (int8_t) (x & 0xFF);
    x1[0] = (int8_t) ((x >> 8) & 0xFF);

    y2[0] = (int8_t) (y & 0xFF);
    y1[0] = (int8_t) ((y >> 8) & 0xFF);

    z2[0] = (int8_t) (z & 0xFF);
    z1[0] = (int8_t) ((z >> 8) & 0xFF);

//    std::cout << (int) x1[0] << "  " << (int) x2[0] << " " <<  (int) y1[0] << "  " << (int) y2[0] << std::endl;

    dataReady = true;

    //todo verwerken van gebruik van instellingen
}

uint8_t magnetoSensor::I2C_readRegister(int address, int internalAddres) {

    if(address != 0x3d){
        return 0;
    }
    if(internalAddres ==  0x00) {
        return x1[0];
    }
    if(internalAddres ==  0x01) {
        return x2[0];
    }
    if(internalAddres == 0x02) {
        return z1[0];
    }
    if(internalAddres == 0x03) {
        return z2[0];
    }
    if(internalAddres == 0x04) {
        return y1[0];
    }
    if(internalAddres == 0x05) {
        return y2[0];
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

signed short magnetoSensor::IntIntergration(std::array<uint8_t, 2> values){
    return (signed short) (values[1] | (values[0] << 8));
}

std::array<short, 2> magnetoSensor::readSensorValuesAndConvertToShort(){
    uint8_t X1 = I2C_readRegister(0x3d, 0x00);
    uint8_t X2 = I2C_readRegister(0x3d, 0x01);
    uint8_t Y1 = I2C_readRegister(0x3d, 0x04);
    uint8_t Y2 = I2C_readRegister(0x3d, 0x05);

    short x = IntIntergration({X1, X2});
    short y = IntIntergration({Y1, Y2});

    return {x, y};
}

PYBIND11_MODULE(magnetoSensor, m) {
    m.doc() = "magnetoSensor";
    py::class_<magnetoSensor>(m, "magnetoSensor")
        .def(py::init<>())
        .def("setCurrentPosition", &magnetoSensor::setMeasueredValue, "Set the input angle, simulated by the sensor")
        .def("I2Cread", &magnetoSensor::I2C_readRegister, "Read registers from the sensor")
        .def("I2Cwrite", &magnetoSensor::I2C_writeRegister, "Write in the registers of the sensor")
        .def("update", &magnetoSensor::update, "Do a 'new measurement', the sensor uses the angle set with 'setMeasurement'")
        .def("getConvertedSensorValues", &magnetoSensor::readSensorValuesAndConvertToShort, "Returns the already converted x and y value it got over I2C from the magneto sensor");
}