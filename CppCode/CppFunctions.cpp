#define _USE_MATH_DEFINES
#include "math.h"
#include "array"
#include "../extern/pybind11/include/pybind11/pybind11.h"
#include "../extern/pybind11/include/pybind11/stl.h"
namespace py = pybind11;

int AzimutAngle(int x, int y) {

    float richting = atan2(y, x);

    if(richting< 0){
        richting += 2*M_PI;
    }
    if(richting > 2*M_PI){
        richting -= 2*M_PI;
    }

    richting = richting*180/M_PI;

    return (int)richting;
}

signed short IntIntergration(std::array<int8_t, 2> values){
    return (signed short) (values[1] | (values[0] << 8));
}


PYBIND11_MODULE(cppFunctions, m) {
m.doc() = "Some functions that are easier written in c++";
m.def("AzimutAngle", &AzimutAngle, "returns the azimut angle, calculated from sensor measurements");
m.def("SensorValueToInt", &IntIntergration, "returns 1 integer, made from both intgers in the input array(shifts them to 1 int)");
}