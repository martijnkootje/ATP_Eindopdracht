//#ifndef V1OOPC_EXAMPLES_MAGNETOSENSOR_H
//#define V1OOPC_EXAMPLES_MAGNETOSENSOR_H
//
//#include <array>
//#include <string>
//#include "../../pythonConnection.h"
//
//class magnetoSensor {
//private:
//    pythonConnection & python;
//
//    std::array<float, 7> intervalTable = { //intervals voor de sensor in seconden
//            0.75, 1.5, 3, 7.5, 15, 30, 75
//    };
//
//    std::array<int, 8> configurrationRegisterB_gain = { //
//            0,1,2,3,4,5,6,7
//    };
//    std::array<int, 4> configurrationRegisterB_operatingMode = { //
//            0,1,2,3
//    };
//    //todo? measurementMode
//
//    // 2 bytes, MSB+LSB, data output X
//    uint8_t x1 = 0;
//    uint8_t x2 = 0;
//
//    // 2 bytes, MSB+LSB, data output Z
//    uint8_t z1 = 0;
//    uint8_t z2 = 0;
//
//    // 2 bytes, MSB+LSB, data output Y (unused)
//    uint8_t y1 = 0;
//    uint8_t y2 = 0;
//
//    int interval = 4; //15hz, default for this sensor module
//
//    int operating = 1; //single measurement, default for this sensor module
//
//    float gain = 1.1;
//
//    bool dataReady = false; //dataReady bit, set high when a measurement is done, normally used in single measurement mode
//
//public:
//    magnetoSensor(pythonConnection & python);
//
//    std::array<uint8_t, 2> I2C_readRegister(int adres, int internalAddres);
//
//    int I2C_writeRegister(int address, uint8_t data);
//
//    void update();
//
//};
//
//
//#endif //V1OOPC_EXAMPLES_MAGNETOSENSOR_H
