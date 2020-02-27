#include <Arduino.h>

int miles =26;
int yards = 385;
float km;

void setup(){
    km = 1.609*(miles + yards/1760);
    Serial.begin(115200);
    Serial.print("marathon is ");
    Serial.print(km);
    Serial.print(" kilometers");
}

void loop(){}

1.609*( 26+ 385/1760)

