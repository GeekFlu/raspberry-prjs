import processing.io.*;

int GPIO_YELLOW = 17;    //define GPIO Pin
int GPIO_GREEN = 4;
int GPIO_RED = 27;

boolean ledState = false;    //define ledState

void setup() {
  println("Available LEDs:");
  printArray(LED.list());
  size(500, 500);
  frameRate(1);        //set frame rate
  GPIO.pinMode(GPIO_YELLOW, GPIO.OUTPUT);    //set the ledPin to output mode
  GPIO.pinMode(GPIO_GREEN, GPIO.OUTPUT);    //set the ledPin to output mode
  GPIO.pinMode(GPIO_RED, GPIO.OUTPUT);    //set the ledPin to output mode
}

void draw() {
  ledState = !ledState;
  if (ledState) {
    GPIO.digitalWrite(GPIO_RED, GPIO.HIGH);    //led on
    GPIO.digitalWrite(GPIO_GREEN, GPIO.LOW);    //led on
    GPIO.digitalWrite(GPIO_YELLOW, GPIO.HIGH);    //led on
    background(255, 0, 0); //set the fill color of led on
  } else {
    GPIO.digitalWrite(GPIO_RED, GPIO.LOW);    //led off
    GPIO.digitalWrite(GPIO_GREEN, GPIO.HIGH);    //led off
    GPIO.digitalWrite(GPIO_YELLOW, GPIO.LOW);    //led off
    background(102); //set the fill color of led off
  }
}

void keyPressed() {
  GPIO.releasePin(GPIO_YELLOW);
  GPIO.releasePin(GPIO_GREEN);
  GPIO.releasePin(GPIO_RED);
  exit();
}
