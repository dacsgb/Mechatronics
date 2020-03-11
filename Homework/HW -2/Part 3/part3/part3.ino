#include "TimerOne.h"

int LED = 9;
bool state = false;

int sensorPin = A0;
 float T_meas = 0;
volatile int flag = 0;
float T_sp = 75.0;

float timer_val = 500000.0;

void setup() {
  Timer1.initialize(timer_val);
  Timer1.attachInterrupt(measure);
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  digitalWrite(LED,LOW);
}

void loop() {
  if (flag == 1){
    T_meas = analogRead(sensorPin)*5.0/(1024*0.01);
    Serial.print(state);
    Serial.print("\t");
    Serial.println(T_meas);
    flag = 0;
  }
  if(T_meas >= T_sp){
    state = true;
  }
  else{
    state = false;
  }
  digitalWrite(LED,state);
}

void measure(){
  flag = 1;
}
