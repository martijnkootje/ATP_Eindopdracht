#include "Servo.h"
#include "../../extern/pybind11/include/pybind11/pybind11.h"
namespace py = pybind11;

PYBIND11_MODULE(servo, m) {
    m.doc() = "Servo class";
    py::class_<Servo>(m, "Servo")
        .def(py::init<>())
        .def("toPosition", &Servo::toPos, "set the position(degrees 0-90)")
        .def("getPosition", &Servo::getPosition, "returns the position of the servo");
}