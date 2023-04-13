// Import libraries
#include <Pixy2.h>
#include <Stepper.h>

// Define used pins
#define STEPPER_DIR_PIN 8
#define STEPPER_PUL_PIN 9

// Define constants
const float STEPS_PER_REV = 3200;                                                                               // Number of steps per revolution
const float ROTATIONS_PER_DIRECTION = 3.12;                                                                     // Number of rotations per direction
const long ROTATION_SPEED = 1.0;                                                                                // Rotation speed in RPM
const float MINUTES_PER_DEPLOY = 1.0;                                                                           // [min] Arm deployment time
const float PULSE_DELAY_uS = (MINUTES_PER_DEPLOY * 1000 * 60) / (ROTATIONS_PER_DIRECTION * STEPS_PER_REV * 2);  // [uS] Delay between pulses based on rotation speed
const int MAX_NUM_STEPS = STEPS_PER_REV * ROTATIONS_PER_DIRECTION;                                              // Number of steps for full deployment

/*
Comments about changing constants above:
  - ROTATIONS_PER_DIRECTION
      This variable controls how far the motor rotates.
      If the arm is going to far during deployment, decrease this number.
      If arm doesn't move far enough, increase this number.
  - ROTATION_SPEED
      This changes the deployment speed.
      This value being set to one means 1 minute open, 1 minute close, for a full 2 minute deployment.
      THE LOWEST THIS VALUE CAN GO IS 0.5. DO NOT SET ANY LOWER OR YOU RISK BREAKING THE MOTOR.
*/

// Initialize repeatedly used variables
int i;                  // Tracks loop index
int x, x1, x2, x3, x4;  // Track x position values
int y, y1, y2, y3, y4;  // Track y position values
unsigned long time;     // Time keeping variable
char inChar = '0';      // Incoming serial com character
char prevChar = '0';    // Tracks last received serial com character
int step = 0;           // Step that motor is currently at [0 ... NUM_STEPS]
int prevStep;           // Tracks last step

// Create Pixy object
Pixy2 pixy;

// Create stepper object
Stepper stepper(STEPS_PER_REV, STEPPER_PUL_PIN, STEPPER_DIR_PIN);

////////////////////////////
// User-Defined Functions //
////////////////////////////
// Read characters from serial port
char readInChar() {
  while (Serial.available() == 0) {
    inChar = Serial.read();
    return inChar;
  }
}

// Move arm toward open
void armOpen() {
  // Set direction to counterclockwise
  digitalWrite(STEPPER_DIR_PIN, LOW);
  for (i=0; i < MAX_NUM_STEPS; i++) {
    // Send pulse to move arm
    digitalWrite(STEPPER_PUL_PIN, HIGH);
    delay(PULSE_DELAY_uS);
    digitalWrite(STEPPER_PUL_PIN, LOW);
    delay(PULSE_DELAY_uS);
  }
}

// Move arm toward closed
void armClose() {
  // Set direction to clockwise
  digitalWrite(STEPPER_DIR_PIN, HIGH);
  for (i=0; i < MAX_NUM_STEPS; i++) {
    // Send pulse to move arm
    digitalWrite(STEPPER_PUL_PIN, HIGH);
    delay(PULSE_DELAY_uS);
    digitalWrite(STEPPER_PUL_PIN, LOW);
    delay(PULSE_DELAY_uS);
  }
}

int armCommand(char inChar, int step, bool loopDir) {
  switch (inChar) {
    case '0':  // No movement
      Serial.println("Stopping arm");
      break;
    case '1':  // Open arm
      if (step < MAX_NUM_STEPS) {
        Serial.println("Opening arm");
        armOpen(step);
        step++;
      }
      break;
    case '2':  // Close arm
      if (step > 0) {
        Serial.println("Closing arm");      
        armClose(step);
        step--;
      }
      break;
    case '3':  // Loop arm
      Serial.println("Looping arm");
      if (step == 0) { // Arm is fully closed, begin opening
        armOpen(step);
        step++;
      }
      else if (step == MAX_NUM_STEPS) { // Arm is fully open, begin closing
        armClose(step);
        step--;
      }
      else if (loopDir && step < MAX_NUM_STEPS) { // Arm is opening but not fully open
        armOpen(step);
        step++;
      }
      else if (!loopDir && step > 0) { // Arm is closing but not fully closed
        armClose(step);
        step--;
      }
      else { // Something gotta break to get here
        break;
      }
      break;
    default:
      Serial.println("No serial data received.");      
      break;
  }
  return step;
}

////////////////////////////

void setup() {
  // Open serial port
  Serial.begin(9600);
  // Serial.begin(19200);

  // Set the motor speed
  stepper.setSpeed(ROTATION_SPEED);

  // Initialize pixy object
  pixy.init();
}

void loop() {
  // Get current time
  time = millis();

  // Get incoming serial values
  // prevChar = inChar;
  inChar = readInChar(inChar);

  // Determine command to send to arm
  switch (inChar) {
    case '0': // No movement
      Serial.println("Stopping arm.");
      break;
    case '1': // Open arm
      Serial.println("Opening arm.");
      armOpen();
      break;
    case '2': // Close arm
      Serial.println("Closing arm.");
      armClose();
      break;
    case '3': // Loop arm
      Serial.println("Looping arm.");
      armOpen();
      delay(1000);
      armClose(); 
    default: // Invalid input
      Serial.println("Invalid input.");
      break;
  }
}
