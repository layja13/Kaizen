byte pinX = A0;
byte pinY = A1;
byte pinB = 8;

byte ledArriba =10;
byte ledDerecha = 11;
byte ledAbajo = 12;
byte ledIzquierda = 7;

int ejeX;
int ejeY;
bool estadoB;


void setup() {
  Serial.begin(9600);
  pinMode(pinX, INPUT);
  pinMode(pinY, INPUT);
  pinMode(pinB, INPUT_PULLUP);
  
  pinMode(ledArriba, OUTPUT);
  pinMode(ledDerecha, OUTPUT);
  pinMode(ledAbajo, OUTPUT);
  pinMode(ledIzquierda, OUTPUT);
  
}

void loop() {

  ejeX = analogRead(pinX);
  ejeY = analogRead(pinY);
  estadoB = digitalRead(pinB);

  if(ejeX > 489 && ejeX < 532){
    digitalWrite(ledDerecha,LOW);
    digitalWrite(ledIzquierda,LOW);
  }
  
  if(ejeX > 532){
    
    
    digitalWrite(ledDerecha,HIGH);
    digitalWrite(ledIzquierda,LOW);  
  }

  if(ejeX < 489){
    
    
    digitalWrite(ledDerecha,LOW);
    digitalWrite(ledIzquierda,HIGH);  
  }

  
  if(ejeY > 489 && ejeY < 532){
    digitalWrite(ledArriba,LOW);
    digitalWrite(ledAbajo,LOW);
  }
    
  if(ejeY > 532){
    digitalWrite(ledArriba,LOW);
    digitalWrite(ledAbajo,HIGH);
  }  

  
  if(ejeY < 489){
    digitalWrite(ledArriba,HIGH);
    digitalWrite(ledAbajo,LOW);
  } 
  
  
  
  Serial.print("ejeX: ");
  Serial.print(ejeX);
  Serial.print("      ejeY: ");
  Serial.print(ejeY);
  Serial.print("      boton: ");
  Serial.println(estadoB);
}
