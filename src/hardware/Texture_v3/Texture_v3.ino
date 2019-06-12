
const int analogPin = A0;   // the pin that the potentiometer is attached to
const int ledCount = 3;    // the number of LEDs in the bar graph
const int buttonPin = 6;     // the number of the pushbutton pin

int buttonState = 0;

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);

  pinMode(2, OUTPUT);    // sets the digital pin 2 as output
  pinMode(3, OUTPUT);    // sets the digital pin 4 as output
  pinMode(4, OUTPUT);    // sets the digital pin 5 as output
   
  pinMode(buttonPin, INPUT);

}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorReading = analogRead(analogPin);
  buttonState = digitalRead(buttonPin);
  //Serial.println(buttonState);

  Serial.print("sensorReading: ");
  Serial.println(sensorReading);    // print out the value you read: 

  int ledLevel = map(sensorReading, 0, 1023, 1, ledCount);
//  Serial.print("ledLevel: ");
//  Serial.println(ledLevel);    // print out the value you read: 

  // loop over the LED array:
  if (ledLevel==1){
    digitalWrite(2, HIGH);
    digitalWrite(4, LOW);
    digitalWrite(3, LOW);
    if (buttonState == HIGH) {
    //send 2 to ras;
    Serial.println("green");
    }
  }
  
  else if (ledLevel==2) {
    digitalWrite(3, HIGH);
    digitalWrite(2, LOW);
    digitalWrite(4, LOW);
    if (buttonState == HIGH) {
    //send 3 to ras;
    Serial.println("yellow");
    }
  }
  
  else if (ledLevel==3); 
    {
    digitalWrite(4, HIGH);
    digitalWrite(3, LOW);
    digitalWrite(2, LOW);
//    if (buttonState == HIGH) {
//        //send 4 to ras;
//    Serial.println("red");
    }

    delay(100);        // delay in between reads for stability


  }





    

  
