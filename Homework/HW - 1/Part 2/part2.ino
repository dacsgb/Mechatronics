#include <Arduino.h>

int i = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  do{
  Serial.println("Diego Colón");
  i++;
  delay(1000);
  }
  while(i<5);
  delay(1000);
  Serial.print("Printed ");
  Serial.print(i);
  Serial.println(" Times");
  delay(1000);
  i = 0;
}