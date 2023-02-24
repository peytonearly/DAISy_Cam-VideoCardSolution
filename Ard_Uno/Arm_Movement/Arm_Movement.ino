#include <Stepper.h>

int PUL_POS = 2; // Assign positive pulse pin
int PUL_NEG = 3; // Assign negative pulse pin
int DIR_POS = 4; // Assign positive direction pin
int DIR_NEG = 5; // Assign negative direction pin

int input = 0; // Contains incoming arm command code
float STEP_ANG = 1.8; // [deg] Step angle
float STEPS_PER_CYCLE = 360 / STEP_ANG; // Number of steps for a full rotation

// Create instance of stepper class
Stepper stepper(STEPS_PER_CYCLE, PUL_POS, PUL_NEG, DIR_POS, DIR_NEG);

void setup() {
  //Configure pins to output to motor driver
  pinMode(PUL_POS, OUTPUT);
  pinMode(PUL_NEG, OUTPUT);
  pinMode(DIR_POS, OUTPUT);
  pinMode(DIR_NEG, OUTPUT);

  Serial.begin(9600); // Start serial communication with baudrate=9600
  stepper.setSpeed(5); // Set motor speed to 5 RPMs
}

int numRot = 0; // Number of rotations from origin (arm closed)
int maxRot = 5; // Maximum number of arm rotations -- corresponds to arm fully open 
void loop() {
  input = Serial.read(); // Read input from serial port

  // Perform action depending on received input
  switch (input) {
    case -1: // Returned when no input > Do nothing
      Serial.println("No input");
      break;
    case 0: // Arm fully closed
      Serial.println("Closing arm");
      break;
    case 1: // Arm fully opened
      Serial.println("Opening arm");
      break;
    case 2: // Pause movement
      Serial.println("Empty input");
      break;
    case 3: // Resume movement
      break;
    case 4: // Loop between open and closed
      break;
  }
}