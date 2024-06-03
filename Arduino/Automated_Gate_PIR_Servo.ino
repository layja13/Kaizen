#This code allows you to rotate a Servo once a human is detected, simulating an automated gate

#include <Servo.h>

byte sensorpir=2;
bool estado=0;
Servo servo1;
int angulo=0;

void setup()
{
  Serial.begin(9600);
  
  pinMode(sensorpir, INPUT);
  
  servo1.attach(A0);
}

void loop()
{
  estado = digitalRead(sensorpir);
  angulo = analogRead(A0);
  
  if(estado == 1){
    servo1.write(90);
  }
  
  if(estado==0){
    servo1.write(0);
  }


   

Serial.print(estado);
Serial.print("    ");
Serial.println(angulo);
  
}
