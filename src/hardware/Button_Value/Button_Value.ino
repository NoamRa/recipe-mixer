
// texture
const int ledCount = 3;    // the number of LEDs in the bar graph
const int analogPin = A0;   // the pin that the potentiometer is attached to

// colors
int buttonPins[] = {8, 9, 10};       // an array of pin numbers to which LEDs are attached
int pinCount = 3;           // the number of pins (i.e. the length of the array)
int ButtonsState[3];
int index;
int ButtonValue;


void setup() {
  //start serial connection
  Serial.begin(9600);
  //configure pin 2 as an input and enable the internal pull-up resistor

//texture
  pinMode(2, INPUT_PULLUP);
  pinMode(3, OUTPUT);    // sets the digital pin 2 as output
  pinMode(4, OUTPUT);    // sets the digital pin 3 as output
  pinMode(5, OUTPUT);    // sets the digital pin 4 as output

//colors
  for (int index = 0; index < pinCount; index++) {
    pinMode(buttonPins[index], INPUT_PULLUP);
    ButtonsState[index] = digitalRead(buttonPins[index]);
  }
  
}

void loop() {
  //read the pushbutton value into a variable
  //potentiometer loop
  int sensorVal = digitalRead(2);
  int sensorAnalog = analogRead(A0);
  int sensorReading = analogRead(analogPin);
  
  int ledLevel = map(sensorReading, 0, 1023, 1, ledCount);

  //colors  loop from the lowest pin to the highest:
  for (int index = 0; index < pinCount; index++) {
      ButtonValue = digitalRead(buttonPins[index]);

      if (ButtonValue != ButtonsState[index]) {
          //Serial.print("this button has changed:");
          Serial.println(buttonPins[index]);
          
//          if (index == 8) {
//            Serial.println("yellow");
//          }
//          else {
//            if (index == 9) 
//            Serial.println("blue");
//          }
//      }
//          else {
//            if (index == 10)
//            Serial.println("green");
//          }
     
          

          ButtonsState[index] = ButtonValue;
      }
  

  

  // Keep in mind the pull-up means the pushbutton's logic is inverted. It goes
  // HIGH when it's open, and LOW when it's pressed. Turn on pin 13 when the
  // button's pressed, and off when it's not:
  if (ledLevel==1){
            //Serial.println("red");
            digitalWrite(3, HIGH);
            digitalWrite(4, LOW);
            digitalWrite(5, LOW);  
            if (sensorVal == 0) {
               Serial.println(sensorAnalog);
//               Serial.println("|");
//               Serial.println(ButtonValue);


            }
        }
        else if (ledLevel==2){
            //Serial.println("yellow");
            digitalWrite(4, HIGH);
            digitalWrite(3, LOW);
            digitalWrite(5, LOW);
            if (sensorVal == 0) {
              Serial.println(sensorAnalog);
//              Serial.println("|");
//              Serial.println(ButtonValue);
            } 
        }

       else  if (ledLevel==3){
            //Serial.println("green");
            digitalWrite(5, HIGH);
            digitalWrite(3, LOW);
            digitalWrite(4, LOW); 
            if (sensorVal == 0) {
              Serial.println(sensorAnalog);
//              Serial.println("|");
//              Serial.println(ButtonValue);
            }
        }
        
      

//    digitalWrite(13, LOW);
   else {
      //Serial.println("none");
      digitalWrite(5, LOW);
      digitalWrite(3, LOW);
      digitalWrite(4, LOW);             

//    digitalWrite(13, HIGH);
  }
    delay(500);        // delay in between reads for stability

}
}
