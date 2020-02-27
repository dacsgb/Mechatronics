void setup() {
  DDRB = B00011111;
  PORTB = B00000000;
  Serial.begin(9600);
  
  for(int i=0; i<=16; i++){
    Serial.println(i);
    PORTB = (i%16);
    delay(1000);
  }
}

void loop() {
  // put your main code here, to run repeatedly:

}
