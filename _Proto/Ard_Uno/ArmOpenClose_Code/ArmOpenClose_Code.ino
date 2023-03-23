#include <Stepper.h>

// Define the stepper motor pins
#define STEPPER_DIR_PIN 8
#define STEPPER_PUL_PIN 9

// Define the number of steps per revolution
const float STEPS_PER_REV = 3200;

// Define the number of rotations per direction
const float ROTATIONS_PER_DIRECTION = 3.22;

// Define the rotation speed in RPM
const long ROTATION_SPEED = 1.0;

// Calculate the delay in microseconds between pulses based on the rotation speed
const float MINUTES_PER_DEPLOY = 2;

const float PULSE_DELAY_mS = (MINUTES_PER_DEPLOY*1000*60) / (ROTATIONS_PER_DIRECTION*STEPS_PER_REV*2);

// Create a Stepper object with the number of steps per revolution and the motor pin numbers
Stepper stepper(STEPS_PER_REV, STEPPER_PUL_PIN, STEPPER_DIR_PIN);

void setup() {
  // Set the motor speed to the calculated delay
  stepper.setSpeed(ROTATION_SPEED);
}

void loop() {
  // Rotate the motor counterclockwise
  digitalWrite(STEPPER_DIR_PIN, LOW); // Set direction to counterclockwise
  for (int i = 0; i < STEPS_PER_REV * ROTATIONS_PER_DIRECTION; i++) {
    digitalWrite(STEPPER_PUL_PIN, HIGH);
    delay(PULSE_DELAY_mS);
    digitalWrite(STEPPER_PUL_PIN, LOW);
    delay(PULSE_DELAY_mS);
  }

  // Wait for 1 second before rotating in the opposite direction
  delay(1000);

  // Rotate the motor clockwise
  digitalWrite(STEPPER_DIR_PIN, HIGH); // Set direction to clockwise
  for (int i = 0; i < STEPS_PER_REV * ROTATIONS_PER_DIRECTION; i++) {
    digitalWrite(STEPPER_PUL_PIN, HIGH);
    delay(PULSE_DELAY_mS/5);
    digitalWrite(STEPPER_PUL_PIN, LOW);
    delay(PULSE_DELAY_mS/5);
  }

  // Wait for 1 second before repeating
  delay(1000);
  exit(0);
}
