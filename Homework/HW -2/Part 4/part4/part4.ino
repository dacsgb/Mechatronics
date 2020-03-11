int cm = 0;

int PWM = 0;
const int LED = 9;

long readUltrasonicDistance(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT);
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  return pulseIn(echoPin, HIGH);
}

void setup()
{
  Serial.begin(115200);
}

void loop()
{
  cm = 0.01723 * readUltrasonicDistance(7, 6);
  float a = -(0.1*cm +5.6);
  PWM = 255/(1+pow(2.71828,a));
  PWM = map(cm,0,20,255,0);
  if(PWM<=255 && PWM >= 0){
  	analogWrite(LED,PWM);
  }
  else{
    analogWrite(LED,0);
  }
  Serial.print(cm);
  Serial.print("\t");
  Serial.println(PWM);
}
