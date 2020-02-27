#include <Arduino.h>

int ledPin = 9; // PWM pin for the LED
void setup(){
    pinMode(ledPin,OUTPUT);
} // no setup needed

void loop()
{
    for (int i=0; i<=255; i=i+10) // ascending value for i
    {
        analogWrite(ledPin, i); // sets brightess level to i
        delay(100); // pauses for 100ms
    }

    for (int i=255; i>=0; i=i-10) // descending value for i
    {
        analogWrite(ledPin, i); // sets brightess level to i
        delay(100); // pauses for 100ms
    }
}
