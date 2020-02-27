#include "TimerOne.h"
#include <Arduino.h>

int pin = 13; // Set the output pin
volatile int state = LOW;

void setup() {
pinMode(pin,OUTPUT);
  // attach ISR to the Timer1 overflow
  Timer1.initialize(1000000);
  Timer1.attachInterrupt(blink);
}
void loop() {
digitalWrite(pin,state); 

}

void blink() { //ISR function
state = !state; }
