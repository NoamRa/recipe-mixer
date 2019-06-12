/*
  Input Pull-up Serial

  This example demonstrates the use of pinMode(INPUT_PULLUP). It reads a digital
  input on pin 2 and prints the results to the Serial Monitor.

  The circuit:
  - momentary switch attached from pin 2 to ground
  - built-in LED on pin 13

  Unlike pinMode(INPUT), there is no pull-down resistor necessary. An internal
  20K-ohm resistor is pulled to 5V. This configuration causes the input to read
  HIGH when the switch is open, and LOW when it is closed.

  created 14 Mar 2012
  by Scott Fitzgerald

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/InputPullupSerial
*/

const int ledCount = 3;    // the number of LEDs in the bar graph
const int analogPin = A0;   // the pin that the potentiometer is attached to

void setup() {
  //start serial connection
  Serial.begin(9600);
  //configure pin 2 as an input and enable the internal pull-up resistor

  pinMode(2, INPUT_PULLUP);

  pinMode(3, OUTPUT);    // sets the digital pin 2 as output
  pinMode(4, OUTPUT);    // sets the digital pin 3 as output
  pinMode(5, OUTPUT);    // sets the digital pin 4 as output   
  
//  pinMode(13, OUTPUT);

}

void loop() {
  //read the pushbutton value into a variable
  int sensorVal = digitalRead(2);
  int sensorAnalog = analogRead(A0);
  int sensorReading = analogRead(analogPin);
  
  //print out the value of the pushbutton
  Serial.print("button mode: ");
  Serial.println(sensorVal);

  int ledLevel = map(sensorReading, 0, 1023, 1, ledCount);

  // Keep in mind the pull-up means the pushbutton's logic is inverted. It goes
  // HIGH when it's open, and LOW when it's pressed. Turn on pin 13 when the
  // button's pressed, and off when it's not:
  if (sensorVal == 1) {
      Serial.println(sensorAnalog);
        if (ledLevel==1){
            Serial.println("red");
            digitalWrite(3, HIGH);
            digitalWrite(4, LOW);
            digitalWrite(5, LOW);  
        }
        else if (ledLevel==2){
            Serial.println("yellow");
            digitalWrite(4, HIGH);
            digitalWrite(3, LOW);
            digitalWrite(5, LOW); 
        }

       else  if (ledLevel==3){
            Serial.println("green");
            digitalWrite(5, HIGH);
            digitalWrite(3, LOW);
            digitalWrite(4, LOW); 
        }
      

//    digitalWrite(13, LOW);
  } else {
      Serial.println("none");
      digitalWrite(5, LOW);
      digitalWrite(3, LOW);
      digitalWrite(4, LOW);             

//    digitalWrite(13, HIGH);
  }
    delay(1000);        // delay in between reads for stability

}
