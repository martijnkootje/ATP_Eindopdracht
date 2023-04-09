#include "zonnePositieSensor.h"
#include <iostream>
#include "../../extern/pybind11/include/pybind11/pybind11.h"
#include "../../extern/pybind11/include/pybind11/stl.h"
namespace py = pybind11;

zonnePositieSensor::zonnePositieSensor(){

}

using std::string;
using std::array;
using std::cout;
using std::cin;
using std::stoi;


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
std::array<int, 5> zonnePositieSensor::inputAngleToSensorValues() {
    std::cout << "Geef een zonnepositie X: ";
    std::string s1 = "";
    std::cin >> s1;

    std::cout << "\nGeef een zonnepositie Y: ";
    std::string s2 = "";
    std::cin >> s2;
    std::cout << '\n';

//    auto coords = {x, y};


    //todo afmaken

    return std::array<int, 5> {1,2,3,4,5};
}

PYBIND11_MODULE(zonneSensor, m) {
    m.doc() = "Zonnepositiesensor";
    py::class_<zonnePositieSensor>(m, "zonnePositieSensor")
        .def(py::init<>())
        .def("inputSensorValues", &zonnePositieSensor::inputSensorValues, "Fill in input values for the sensor")
        .def("inputAngleToSensorValues", &zonnePositieSensor::inputAngleToSensorValues, "Fill in 2 angles and this function returns 5 sensor values");
}
