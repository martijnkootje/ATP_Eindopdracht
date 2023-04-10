#ifndef ZONNESENSOR_MOTOR_H
#define ZONNESENSOR_MOTOR_H


class Motor {
private:
    bool enabled = false;
    bool direction = true; //true is positief, false negatief.
public:
    Motor(){}
    bool getStatus(){
        return enabled;
    }
    bool getDirection(){
        return direction;
    }

    void turnON(){
        enabled = true;
    }
    void turnOFF(){
        enabled = false;
    }
    void setDirection(bool dir){
        direction = dir;
    }
};


#endif //ZONNESENSOR_MOTOR_H
