//This code allows you to motors control with L298N motor controller

int in1 = 8;      
int in2 = 9;    
int in3 = 10;
int in4 =11;  
int ena = 6;
int enb = 5;
   

void setup(){
 pinMode(in1,OUTPUT);
 pinMode(in2,OUTPUT);
 pinMode(in3,OUTPUT);
 pinMode(in4,OUTPUT);
 }
void loop(){
  digitalWrite(in1,HIGH);
  digitalWrite(in2,LOW);
   digitalWrite(in3,0);
  digitalWrite(in4,1);
  digitalWrite(ena,200);
  digitalWrite(enb,200);
  delay(2000);

  digitalWrite(in1,LOW);
  digitalWrite(in2,LOW);
   digitalWrite(in3,0);
  digitalWrite(in4,0);
  delay(2000);

  digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
   digitalWrite(in3,1);
  digitalWrite(in4,0);
  digitalWrite(ena,255);
  digitalWrite(enb,255);
  delay(3000);

  digitalWrite(in3,0);
  digitalWrite(in4,0);
  digitalWrite(in1,LOW);
  digitalWrite(in2,LOW);
  delay(3000);

  
}
