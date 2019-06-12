
int pin = A0; 
int val = 0;

 void setup() 
 {
   pinMode(pin, INPUT);
   Serial.begin(115200);
 }

 void loop()
 {
  val = analogRead(pin); 
  Serial.write(val/4);
  }
