#include "Motor.h"
#include "../../extern/pybind11/include/pybind11/pybind11.h"
namespace py = pybind11;

PYBIND11_MODULE(motor, m) {
m.doc() = "Motor class";
py::class_<Motor>(m, "Motor")
.def(py::init<>())
    .def("status", &Motor::getStatus, "Is the motor enabled?")
    .def("direction", &Motor::getDirection, "returns the direction the motor is turning")
    .def("turnON", &Motor::turnON, "enable the motor")
    .def("turnOFF", &Motor::turnOFF, "disable the motor")
    .def("setDirection", &Motor::setDirection, "set the direction of the motor");
}