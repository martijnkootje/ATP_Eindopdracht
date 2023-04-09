#include "ZonneSenor/zonnePositieSensor.h"
#include "MagnetoSensor/magnetoSensor.h"
#include <iostream>
#include <string>


/////test function for calculating angle from sensor values
//#define _USE_MATH_DEFINES
//#include "math.h"
//int AzimutAngle(int x, int y) {
//
//    float richting = atan2(y, x);
//
//    if(richting< 0){
//        richting += 2*M_PI;
//    }
//    if(richting > 2*M_PI){
//        richting -= 2*M_PI;
//    }
//
//    richting = richting*180/M_PI;
//
//    return (int)richting;
//}

//int main(){
//    //mainloop
//    auto pythonconnection = pythonConnection();
//    auto zonnesensor = zonnePositieSensor(pythonconnection);
//    auto magnetosensor = magnetoSensor(pythonconnection);
//
//    while(true) {
//        std::cout << "Opties:\n";
//        std::cout << "0 : Exit.\n";
//        std::cout << "1 : geef input voltages voor de zonnesensor.\n";
//        std::cout << "2 : geef input coordinaten voor de zonnesensor.\n";
//        std::cout << "3 : geef input hoek voor de magnetosensor.\n";
//        std::cout << "4 : print de output waarden van de magnetosensor.\n";
//
//        //getting awnser
//        std::cout << "Geef een optie: ";
//        std::string str = "";
//        std::cin >> str;
//
//        //to int
//        int choice = std::stoi(str);
//
//        if (choice == 0) {
//            return 0;
//        }
//
//        if (choice == 1) {
//            std::string str = "";
//            for (int i: zonnesensor.inputSensorValues()) {
//                str.append(std::to_string(i) + ',');
//            }
//            pythonconnection.sendToPython("zonnesensor", str);
//        }
//
//        if(choice == 3){
//            std::string str = "";
//            std::cout << "Angle in degrees(0 - 360): ";
//            std::cin >> str;
//            pythonconnection.receiveFromPython("angle", str);
//            magnetosensor.update();
//        }
//
//        if (choice == 4) {
//            auto sensorX = magnetosensor.I2C_readRegister(0x3d, 0x00);
//            auto sensorZ = magnetosensor.I2C_readRegister(0x3d, 0x01);
//            auto sensorY = magnetosensor.I2C_readRegister(0x3d, 0x02);
//            std::cout << "\nValue x, byte 1: " << (int) sensorX[0] << "\nValue x, byte 2: " << (int) sensorX[1] << "\n\n";
//            std::cout << "Value y, byte 1: " << (int) sensorY[0] << "\nValue y, byte 2: " << (int) sensorY[1] << "\n\n";
//            std::cout << "Value z, byte 1: " << (int) sensorZ[0] << "\nValue z, byte 2: " << (int) sensorZ[1] << "\n\n";
//            int x = (signed short) (sensorX[1] | (sensorX[0] << 8));
//            int y = (signed short) (sensorY[1] | (sensorY[0] << 8));
//            std::cout << x << "  " << y << "\n";
//            std::cout << AzimutAngle(x, y) << "\n";
//        }
//
//    }
//}

//2 values to an angle (needs to be implemented in python)


// int x = (signed short) (sensorX[1] | (sensorX[0] << 8));
// int y = (signed short) (sensorY[1] | (sensorY[0] << 8));
// std::cout << AzimutAngle(x, y) << "\n";