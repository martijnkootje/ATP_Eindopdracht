#ifndef V1OOPC_EXAMPLES_MAGNETOSENSOR_H
#define V1OOPC_EXAMPLES_MAGNETOSENSOR_H

#include <array>
#include <string>

class magnetoSensor {
private:

    std::array<float, 7> intervalTable = { //intervals voor de sensor in seconden
            0.75, 1.5, 3, 7.5, 15, 30, 75
    };

    std::array<int, 8> configurrationRegisterB_gain = { //
            0,1,2,3,4,5,6,7
    };
    std::array<int, 4> configurrationRegisterB_operatingMode = { //
            0,1,2,3
    };
    //todo? measurementMode

    // 2 bytes, MSB+LSB, data output X
    std::array<uint8_t, 1> x1 = {0};
    std::array<uint8_t, 1> x2 = {0};
//    int x = 0; //python doesn't have support for uint8_t or any other unsigned or short values

    // 2 bytes, MSB+LSB, data output Z
    std::array<uint8_t, 1> y1 = {0};
    std::array<uint8_t, 1> y2 = {0};

    // 2 bytes, MSB+LSB, data output Y (unused)
    std::array<uint8_t, 1> z1 = {0};
    std::array<uint8_t, 1> z2 = {0};

    int measurement = 0;

    int interval = 4; //15hz, default for this sensor module

    int operating = 1; //single measurement, default for this sensor module

    float gain = 1.1;

    bool dataReady = false; //dataReady bit, is high when a measurement is done, used in single measurement mode

    int AzimutAngle(int x, int y);

    signed short IntIntergration(std::array<uint8_t, 2> values);

public:
    magnetoSensor();

    uint8_t I2C_readRegister(int adres, int internalAddres);

    int I2C_writeRegister(int address, uint8_t data);

    void update();

    ///Set the value of the angle(normally measured by the sensor)
    void setMeasueredValue(int angle);

    ///Python doesn't have support for uints and different sizes of ints,
    ///In this case it is easier to use c++ to convert the 8 bit unsigned sensor values to a 16+ bit signed int.
    ///Python has no support for bit shifting too, to keep this software as functional as possible I prefer using c++ code instead of a library.
    std::array<short, 2> readSensorValuesAndConvertToShort();

};


#endif //V1OOPC_EXAMPLES_MAGNETOSENSOR_H
