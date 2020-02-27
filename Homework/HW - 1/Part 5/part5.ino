#include <Arduino.h>

int n = 4;
int sum = 0;
int fin = 0;

void setup() {
  Serial.begin(115200);
  for(int i = 1; i<=n; i++){
    for (int j = 1; j <= i-1; j++)
      {
        sum+=j;
        fin = j;
        Serial.print(j);
        Serial.print('+');
      }
      sum += fin+1;
      Serial.print(fin+1);
      Serial.print('=');
      Serial.println(sum);
    sum = 0;
  }
}

void loop(){}