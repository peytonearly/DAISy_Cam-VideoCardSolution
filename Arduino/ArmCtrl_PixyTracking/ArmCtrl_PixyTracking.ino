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
char inChar;            // Incoming serial com character
int step;               // Step that motor is currently at [0 ... NUM_STEPS]
bool loopDir;           // Specifies loop direction [false -> Closed | true -> Open]

// Create Pixy object
Pixy2 pixy;

// Create stepper object
Stepper stepper(STEPS_PER_REV, STEPPER_PUL_PIN, STEPPER_DIR_PIN);

////////////////////////////
// User-Defined Functions //
////////////////////////////
// Read characters from serial port
char readInChar() {
  if (Serial.available() > 0) {
    inChar = Serial.read();
    return inChar;
  }
  return NULL;
}

// Move arm toward open
void armOpen(int step) {
  if (step > MAX_NUM_STEPS) { // Only run if not above max step number 
    // Set direction to counterclockwise
    digitalWrite(STEPPER_DIR_PIN, LOW);

    // Send pulse to move arm
    digitalWrite(STEPPER_PUL_PIN, HIGH);
    delay(PULSE_DELAY_uS);
    digitalWrite(STEPPER_PUL_PIN, LOW);
    delay(PULSE_DELAY_uS);
  }
}

// Move arm toward closed
void armClose(int step) {
  if (step < 0) { // Only run if not below 0 
    // Set direction to clockwise
    digitalWrite(STEPPER_DIR_PIN, HIGH);

    // Send pulse to move arm
    digitalWrite(STEPPER_PUL_PIN, HIGH);
    delay(PULSE_DELAY_uS);
    digitalWrite(STEPPER_PUL_PIN, LOW);
    delay(PULSE_DELAY_uS);
  }
}

void armCommand(char inChar, int step, bool loopDir) {
  switch (inChar) {
    case '0':  // No movement
      Serial.println("Stopping arm");
      break;
    case '1':  // Open arm
      if (step < MAX_NUM_STEPS) {
        Serial.println("Opening arm");
        armOpen();
        step++;
      }
      break;
    case '2':  // Close arm
      if (step > 0) {
        Serial.println("Closing arm");      
        armClose();
        step--;
      }
      break;
    case '3':  // Loop arm
      Serial.println("Looping arm");
      if (step == 0) { // Arm is fully closed, begin opening
        loopDir = true;
        armOpen();
      }
      else if (step == MAX_NUM_STEPS) { // Arm is fully open, begin closing
        loopDir = false;
        armClose();
      }
      else if (loopDir && step < MAX_NUM_STEPS) { // Arm is opening but not fully open
        armOpen();
      }
      else if (!loopDir && step > 0) { // Arm is closing but not fully closed
        armClose();
      }
      else { // Something gotta break to get here
        continue;
      }
      break;
    default:
      break;
  }
  return step, loopDir;
}

////////////////////////////

void setup() {
  // Open serial port
  // Serial.begin(9600);
  Serial.begin(19200);

  // Set the motor speed
  stepper.setSpeed(ROTATION_SPEED);

  // Initialize pixy object
  pixy.init();

  // Set step to 0
  step = 0;
  loopDir = false;
}

void loop() {
  // Get current time
  time = millis();

  // Get incoming serial values
  inChar = readInChar();

  // Move arm based on received character value
  step, loopDir = armCommand(inChar, step, loopDir);

  // Grab pixy blocks
  pixy.ccc.getBlocks();

  // Assign as irrational values before assigning positions
  x1 = -1, x2 = -1, x3 = -1, x4 = -1;
  y1 = -1, y2 = -1, y3 = -1, y4 = -1;

  // Find positions of detected blocks
  if (pixy.ccc.numBlocks) {
    for (i = 0; i < pixy.ccc.numBlocks; i++) {
      x = pixy.ccc.blocks[i].m_x;
      y = pixy.ccc.blocks[i].m_y;

      switch (pixy.ccc.blocks[i].m_signature) {
        case 1:
          x1 = x;
          y1 = y;
          break;
        case 2:
          x2 = x;
          y2 = y;
          break;
        case 3:
          x3 = x;
          y3 = y;
          break;
        case 4:
          x4 = x;
          y4 = y;
          break;
        default:
          break;
      }
    }
  }

  // Print positions to serial com
  Serial.print(x1);
  Serial.print(",");
  Serial.print(y1);
  Serial.print(",");
  Serial.print(x2);
  Serial.print(",");
  Serial.print(y2);
  Serial.print(",");
  Serial.print(x3);
  Serial.print(",");
  Serial.print(y3);
  Serial.print(",");
  Serial.print(x4);
  Serial.print(",");
  Serial.print(y4);
  Serial.print(",");
  Serial.println(time);
}
