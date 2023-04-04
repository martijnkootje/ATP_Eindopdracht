#ifndef V1OOPC_EXAMPLES_PYTHONCONNECTION_H
#define V1OOPC_EXAMPLES_PYTHONCONNECTION_H

#include <string>

class pythonConnection {
private:
    int currentAngle = 0;

    void setCurrentAngle(int x){
        currentAngle = x;
    }

public:
    pythonConnection();

    int getMeaurement(){
        return currentAngle; //get the angle (instead of measuring because of the simulator)
    }

    bool sendToPython(std::string key, std::string data);

    bool receiveFromPython(std::string key, std::string data);
};


#endif //V1OOPC_EXAMPLES_PYTHONCONNECTION_H
