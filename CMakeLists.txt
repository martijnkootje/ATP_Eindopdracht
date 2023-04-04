cmake_minimum_required(VERSION 3.20)
project(ATP_Eindopdracht)

set(CMAKE_CXX_STANDARD 14)

add_subdirectory(extern/pybind11)
include_directories(C:/Python310/include)
link_libraries(C:/Python310/libs/Python310.lib)

file(GLOB SOURCES
        *.h
        *.cpp
        )

add_executable(ATP_Eindopdracht ${SOURCES})