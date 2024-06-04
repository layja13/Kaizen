#include <Servo.h>

Servo servoX;
Servo servoY;

String str1;
String str2;
String str3;
String str4;
String str5;

int dato1 = 640; // 1280 / 2 = 640
int dato2 = 360; // 720 / 2 = 360
int dato3;
int dato4;
int dato5;

int anguloX;
int anguloY;

void setup() {
  Serial.begin(9600);
  servoX.attach(7);
  servoY.attach(8);
}

void loop() {
  if(Serial.available() > 0){
    str1 = Serial.readStringUntil('A');
    dato1 = str1.toInt();  // Coordenada X

    str2 = Serial.readStringUntil('B');
    dato2 = str2.toInt();  // Coordenada Y

    str3 = Serial.readStringUntil('\n');
    dato3 = str3.toInt();  // Distancia
  }

    servoX.write(dato1);
    servoY.write(dato2);
}
