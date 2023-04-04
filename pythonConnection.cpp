#include "pythonConnection.h"
#include <iostream>

pythonConnection::pythonConnection() {}

bool pythonConnection::sendToPython(std::string key, std::string data) {
    std::cout << key << " : " << data << '\n';
    //todo
    return 0;
}
bool pythonConnection::receiveFromPython(std::string key, std::string data) {
    if(key == "angle"){
        currentAngle = std::stoi(data);
        return 0;
    }
    return 1;
}
