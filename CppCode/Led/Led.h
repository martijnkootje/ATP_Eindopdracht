#ifndef ZONNESENSOR_LED_H
#define ZONNESENSOR_LED_H


class Led {
private:
    bool status = false;

public:
    Led(){

    }

    void turnON(){
        status = 1;
    }
    void turnOFF(){
        status = 0;
    }
    bool getStatus(){
        return status;
    }

};


#endif //ZONNESENSOR_LED_H
