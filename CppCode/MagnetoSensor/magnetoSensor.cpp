//#define _USE_MATH_DEFINES
//
//#include <iostream>
//#include "magnetoSensor.h"
//#include "math.h"
//
//
//magnetoSensor::magnetoSensor(pythonConnection & python) : python(python){
//
//}
//
//void magnetoSensor::update() {
//
//    int hoek = python.getMeaurement();
//
//    float radialen = (float) hoek/(float)180*(float)M_PI;
//
//    float gainx = (rand() % 100)-50 / gain*25;
//    float gainy = (rand() % 100)-50 / gain*25;
//    float gainz = (rand() % 100)-50 / gain*25;
//
//    int x = cos(radialen)*((float)60-gainx)*gain;
//    int y = sin(radialen)*((float)60-gainy)*gain;
//    int z = (rand() % 600) *((float)60-gainz)*gain; //z is not used for this project, so I cant simulate a real value
//
//    x2 = (int8_t) (x & 0xFF);
//    x1 = (int8_t) ((x >> 8) & 0xFF);
//
//    y2 = (int8_t) (y & 0xFF);
//    y1 = (int8_t) ((y >> 8) & 0xFF);
//
//    z2 = (int8_t) (z & 0xFF);
//    z1 = (int8_t) ((z >> 8) & 0xFF);
//
//    dataReady = true;
//
//    //todo verwerken van gebruik van instellingen
//}
//
//std::array<uint8_t, 2> magnetoSensor::I2C_readRegister(int address, int internalAddres) {
//
//    if(address != 0x3d){
//        return {0, 0};
//    }
//
//    if(internalAddres ==  0x00) {
//        return {x1, x2};
//    }
//
//    if(internalAddres == 0x01) {
//        return {z1, z2};
//    }
//
//    if(internalAddres == 0x02) {
//        return {y1, y2};
//    }
//    return {0, 0};
//}
//
//int magnetoSensor::I2C_writeRegister(int address, uint8_t data) {
//    //todo instellngen aanpassen
//    uint8_t data1 = data;
//    if(address == 0x00){
//        uint8_t optionGain = ((data1 >> 5) & 0); //Get the last 3 bits (gain bits)
//        gain = optionGain;
//
//        data1 = data;
//        uint8_t optionOperatingMode = ((data1) & 0x01); //Get the first 5 bits (operationmode bits)
//        operating = optionOperatingMode;
//    }
//
//
//    return 1;
//}
