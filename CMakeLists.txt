cmake_minimum_required(VERSION 3.20)
project(ATP_Eindopdracht)

set(CMAKE_CXX_STANDARD 14)

include(extern/pybind11/CMakeLists.txt)

file(GLOB SOURCES
        *.h
        *.cpp
        )

add_executable(ATP_Eindopdracht ${SOURCES})

