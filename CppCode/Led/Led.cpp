#include "Led.h"
#include "../../extern/pybind11/include/pybind11/pybind11.h"
namespace py = pybind11;

PYBIND11_MODULE(led, m) {
m.doc() = "Led";
py::class_<Led>(m, "Led")
.def(py::init<>())
.def("turnON", &Led::turnON, "turn on led")
.def("turnOFF", &Led::turnOFF, "turn off led")
.def("status", &Led::getStatus, "returns if led is on or off");
}