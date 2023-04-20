#ifndef V1OOPC_EXAMPLES_ZONNEPOSITIESENSOR_H
#define V1OOPC_EXAMPLES_ZONNEPOSITIESENSOR_H
#include <array>



class zonnePositieSensor {
private:
    int angleSunA = 0;
    int angleSunE = 0;
public:
    zonnePositieSensor();

    std::array<int, 5> inputSensorValues();

    std::array<int, 5> inputAngleToSensorValues(int azimut, int elevatie);

    std::array<int, 5> getADCvalues();

    void setCurrentSunPosition(int azimut, int elevatie);
};


#endif //V1OOPC_EXAMPLES_ZONNEPOSITIESENSOR_H
