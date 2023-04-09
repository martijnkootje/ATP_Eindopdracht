#ifndef V1OOPC_EXAMPLES_ZONNEPOSITIESENSOR_H
#define V1OOPC_EXAMPLES_ZONNEPOSITIESENSOR_H
#include <array>



class zonnePositieSensor {
private:

public:
    zonnePositieSensor();

    std::array<int, 5> inputSensorValues();

    std::array<int, 5> inputAngleToSensorValues();

};


#endif //V1OOPC_EXAMPLES_ZONNEPOSITIESENSOR_H
