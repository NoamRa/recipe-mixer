
// LEDs
#include <Adafruit_NeoPixel.h>
#define LED_PIN 3
#define LED_COUNT 10
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

// texture
const int ledCount = 3;    // the number of LEDs in the bar graph
const int analogPin = A0;   // the pin that the potentiometer is attached to

// colors
int buttonPins[] = {8, 9, 10};       // an array of pin numbers to which LEDs are attached
int pinCount = 3;           // the number of pins (i.e. the length of the array)
int ButtonsState[3];
int index;
int ButtonValue;

//random
int pushButton = 6;

void setup() {
  //start serial connection
  Serial.begin(9600);

  // LEDs
  strip.begin();
  strip.clear();
  strip.show();
  int brightness = 40; // (max = 255)
  strip.setBrightness(brightness); 

  
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

//random
  pinMode(pushButton, INPUT);
  
}

void loop() {
  //read the pushbutton value into a variable
  //potentiometer loop
  int sensorVal = digitalRead(2);
  int sensorAnalog = analogRead(A0);
  int sensorReading = analogRead(analogPin);
  int buttonState = digitalRead(pushButton);

  
  int dangerLevel = map(sensorReading, 0, 1023, 0, ledCount);

  //colors  loop from the lowest pin to the highest:
  for (int index = 0; index < pinCount; index++) {
      ButtonValue = digitalRead(buttonPins[index]);
      if (ButtonValue != ButtonsState[index]) {
        //Serial.print("this button has changed:");
        //Serial.println(buttonPins[index]);
        if (buttonPins[index] == 8) {
          Serial.print("|");
          Serial.print("Y");
        }
        else if (buttonPins[index] == 10) {
          Serial.print("|");
          Serial.print("B");
        }
        else if (buttonPins[index] == 9) {
          Serial.print("|");
          Serial.print("G");
        }
        ButtonsState[index] = ButtonValue;
      }
      
    // Keep in mind the pull-up means the pushbutton's logic is inverted. It goes
    // HIGH when it's open, and LOW when it's pressed. Turn on pin 13 when the
    // button's pressed, and off when it's not:
      Serial.print("|");
      Serial.print(sensorAnalog);
      Serial.println("||");
  }
  
  //random
  if (buttonState == 1){
    Serial.print("|random");
    Serial.println("||");
  }

  // handle RGB LEDs
  
  
  delay(1000);        // delay in between reads for stability
}

void showDanger(int dangerLevel) {
  //  dangerLevel is an int 1 to 9
  int hue = map(dangerLevel, 1, 9, 22000, 0);
  Serial.println("danger hue: " + String(hue));
  for (int idx = 1; idx < 9; idx++) {
    if (idx < dangerLevel) {
      int saturation = 128;
      int value = 128;
      uint32_t color = strip.gamma32(strip.ColorHSV(hue));
      strip.setPixelColor(idx, color);
    }
    else {
      strip.setPixelColor(idx, 0, 0, 0);
    }
  }
  strip.show();
}

