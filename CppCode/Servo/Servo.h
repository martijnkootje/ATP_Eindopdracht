#ifndef ZONNESENSOR_SERVO_H
#define ZONNESENSOR_SERVO_H


class Servo {
private:
    int position = 0;
//todo pwm simuleren?
public:
    Servo(){}
    void toPos(int pos) {
        position = pos;
    }
    int getPosition(){
        return position;
    }
};


#endif //ZONNESENSOR_SERVO_H
