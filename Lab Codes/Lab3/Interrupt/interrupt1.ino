#include <Arduino.h>

int pin = 13; // Set the output pin
int inPin = 2;
volatile int state = LOW;

void setup(){
    pinMode(pin, OUTPUT);
    pinMode(inPin,INPUT_PULLUP);
    // attach ISR to pin 2 or interrupt 0
    attachInterrupt(digitalPinToInterrupt (inPin), blink, FALLING);
    Serial.begin(9600);
}

void loop() {
    digitalWrite(pin, state);
    Serial.println(digitalRead(inPin));
}

void blink() { // ISR function
    state = !state;
}
