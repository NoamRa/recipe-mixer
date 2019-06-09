
const int analogPin = A0;   // the pin that the potentiometer is attached to
const int ledCount = 3;    // the number of LEDs in the bar graph
//int ledPins[] = {2,3,4};   // an array of pin numbers to which LEDs are attached

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
//  for (int thisLed = 0; thisLed < ledCount; thisLed++) {
//    pinMode(ledPins[thisLed], OUTPUT);
//  }
   pinMode(2, OUTPUT);    // sets the digital pin 2 as output
   pinMode(3, OUTPUT);    // sets the digital pin 3 as output
   pinMode(4, OUTPUT);    // sets the digital pin 4 as output
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorReading = analogRead(analogPin);
  Serial.print("sensorReading: ");
  Serial.println(sensorReading);    // print out the value you read: 

  int ledLevel = map(sensorReading, 0, 1023, 1, ledCount);
  Serial.print("ledLevel: ");
  Serial.println(ledLevel);    // print out the value you read: 

  // loop over the LED array:
  if (ledLevel==1){
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
//    Serial.println("2");
  }

  else if (ledLevel==2) {
    digitalWrite(3, HIGH);
    digitalWrite(2, LOW);
    digitalWrite(4, LOW);
//    Serial.println("3");

  }
  
  else {
    digitalWrite(4, HIGH);
    digitalWrite(3, LOW);
    digitalWrite(2, LOW);
//    Serial.println("4");

  }
  delay(100);        // delay in between reads for stability

}

//  for (int thisLed = 0; thisLed < ledCount; thisLed++) {
//    // if the array element's index is less than ledLevel,
//    // turn the pin for this element on:
//    if (thisLed < ledLevel) {
//      digitalWrite(ledPins[thisLed], HIGH);
//    }
//    // turn off all pins higher than the ledLevel:
//    else {
//      digitalWrite(ledPins[thisLed], LOW);
    

  
