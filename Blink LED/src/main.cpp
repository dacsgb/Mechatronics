#include <Arduino.h>

int A = 5; //2 //50; //1900; //5791;
int B = 7; //5; //4; //2700; //9311;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  int C = A*B;
  Serial.println(A);
  Serial.println(B);
  Serial.println(C);
}

void loop() {
}