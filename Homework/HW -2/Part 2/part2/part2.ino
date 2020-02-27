int LED = 8;
int INTER = 2;
bool state = false;

void setup() {
  pinMode(LED,OUTPUT);
  pinMode(INTER, INPUT_PULLUP);
  Serial.begin(115200);
  attachInterrupt(digitalPinToInterrupt(INTER), detected, FALLING);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(state ==true){
    digitalWrite(LED,HIGH);
    delay(3000);
    digitalWrite(LED,LOW);
    state = !state;
  }
  Serial.println(state);
}

void detected(){
  state = !state;
}
