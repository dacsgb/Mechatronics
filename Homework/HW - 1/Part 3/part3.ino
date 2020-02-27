#include <Arduino.h>

int A = 5791;
int B = 9311;

void setup(){
    int C = A * B;
    Serial.begin(115200);
    Serial.println(A);
    Serial.println(B);
    Serial.println(C);
}

void loop(){}