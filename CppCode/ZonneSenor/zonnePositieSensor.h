#ifndef V1OOPC_EXAMPLES_ZONNEPOSITIESENSOR_H
#define V1OOPC_EXAMPLES_ZONNEPOSITIESENSOR_H

#include <array>
#include "../../pythonConnection.h"

class zonnePositieSensor {
private:
    pythonConnection & connection;
public:
    zonnePositieSensor(pythonConnection & python);

    std::array<int, 5> inputSensorValues();

    std::array<int, 5> inputAngleToSensorValues();

};


#endif //V1OOPC_EXAMPLES_ZONNEPOSITIESENSOR_H
