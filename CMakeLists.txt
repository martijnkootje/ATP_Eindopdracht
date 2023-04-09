cmake_minimum_required(VERSION 3.20)
project(zonneSensor)

set(pybind11_DIR extern/pybind11)
add_subdirectory(${pybind11_DIR})
#include_directories(C:/Python310/include)
#link_libraries(C:/Python310/libs/Python310.lib)
pybind11_add_module(zonneSensor CppCode/ZonneSenor/zonnePositieSensor.cpp)