# This code allows you to control a Servomotor in proportion to the angle of a Potenciometer

int pot=A5;
byte m1=9;
byte m2=10;
int led=3;
int lectura=0;
void setup() {
 Serial.begin(9600);
 pinMode(pot,INPUT);
 pinMode(m1,OUTPUT);
 pinMode(m2,OUTPUT);
 pinMode(led,OUTPUT);
}

void loop() {
  lectura=analogRead(pot);
  lectura=map(lectura,0,1023,0,255);
  analogWrite(m1,lectura);
  analogWrite(led,lectura);
  Serial.println(lectura);
}
