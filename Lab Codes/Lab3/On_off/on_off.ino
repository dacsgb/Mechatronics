int LED = 13;
int inPin = 2;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED, OUTPUT);
  pinMode(inPin, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(inPin) == HIGH){
    digitalWrite(LED, HIGH);
    delay(1000);
    digitalWrite(LED, LOW);
    delay(1000);
    Serial.println("HIGH");
  }
  else {
    digitalWrite(LED, LOW);
    Serial.println("LOW");
  }
}
