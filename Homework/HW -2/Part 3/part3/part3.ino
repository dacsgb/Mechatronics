#include "TimerOne.h"

int LED = 8;
bool state = false;

int sensorPin = A0;
volatile float T_meas = 0;
float T_sp = 75.0;

int timer_val = 500000;

void setup() {
  Timer1.initialize(timer_val);
  Timer1.attachInterrupt(measure);
  Serial.begin(9600);
  digitalWrite(LED,LOW);
}

void loop() {
  Serial.print(state);
  Serial.print("\t");
  Serial.println(T_meas);
  if(T_meas >= T_sp){
    state = true;
  }
  else{
    state = false;
  }
  digitalWrite(LED,state);
}

void measure(){
  T_meas = analogRead(sensorPin)*5.0/(1024*0.01);
}
