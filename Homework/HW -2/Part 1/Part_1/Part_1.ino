void setup() {
  DDRB = B00011111;
  PORTB = B00000000;
  Serial.begin(115200);
  
  for(int i=0; i<=16; i++){
    Serial.println(i);
    lights(i);
    delay(1000);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
}

void lights(int n){
  PORTB = (n%16);
}
