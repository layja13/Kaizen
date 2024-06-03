// Pretty easy code
// This code measures the humidity of soil, for example, that of the ground

int sensor=A0;
int humedad=0;

void setup() {
  pinMode(A0,INPUT);
  

}

void loop() {
 humedad=analogRead(sensor);
 Serial.println(humedad);

}
