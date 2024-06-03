int time=0;
float distance=0;

void setup() {
Serial.begin(9600);
pinMode(2,OUTPUT);
pinMode(A5,INPUT);
pinMode(7,OUTPUT);
pinMode(8,OUTPUT);
}

void loop() {
  digitalWrite(2,LOW);
  delayMicroseconds(10);
  digitalWrite(2,HIGH);
  delayMicroseconds(20);
  digitalWrite(2,LOW);

  time = pulseIn(A5,HIGH);
  distance = 0.01716*time;
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  if(distance<100){
    digitalWrite(7,HIGH);
    digitalWrite(8,HIGH);
    delay(distance*10);
    digitalWrite(7,LOW);
    digitalWrite(8,LOW);
    delay(distance*10);
  }

  else {
    digitalWrite(7,LOW);
    digitalWrite(8,LOW);
  }
}
