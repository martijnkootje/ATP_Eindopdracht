cmake_minimum_required(VERSION 3.20)
project(zonneSensor)

set(pybind11_DIR extern/pybind11)
add_subdirectory(${pybind11_DIR})

pybind11_add_module(zonneSensor CppCode/ZonneSenor/zonnePositieSensor.cpp)
pybind11_add_module(magnetoSensor CppCode/magnetoSensor/magnetoSensor.cpp)
pybind11_add_module(motor CppCode/Motor/Motor.cpp)
pybind11_add_module(servo CppCode/Servo/Servo.cpp)
pybind11_add_module(cppFunctions CppCode/CppFunctions.cpp)