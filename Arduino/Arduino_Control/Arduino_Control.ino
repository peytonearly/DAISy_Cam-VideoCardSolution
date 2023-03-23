#include <Pixy2.h>

// Create Pixy object
Pixy2 pixy;

// Initialize repeatedly used variables
int i; // Tracks loop index
int x, x1, x2; // Track x position values
int y, y1, y2; // Track y position values
unsigned long time; // Time keeper
char inChar; // Incoming serial comm character
int action = 0; // Current action

void setup() {
  Serial.begin(9600);
  Serial.print("Starting at 9600 baud...\n");

  pixy.init();
}

void loop() {
  // Read values coming from Raspberry Pi
  if (Serial.available() > 0) {
    inChar = Serial.read();
  }
  else {
    inChar = NULL;
  }

  // Update task if changed

  // Grab pixy blocks
  pixy.ccc.getBlocks();
  
  // Pre-define as irrational values
  x1=-1, x2=-1;
  y1=-1, y2=-1;

  // Find positions of detected blocks and send over serial comm
  if (pixy.ccc.numBlocks) {
    for (i=0; i<pixy.ccc.numBlocks; i++) {
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
        default:
          break;
      }
    }
  }

  // Get current time
  time = millis();
  Serial.print(x1);
  Serial.print(",");
  Serial.print(y1);
  Serial.print(",");
  Serial.print(x2);
  Serial.print(",");
  Serial.print(y2);
  Serial.print(",");
  Serial.println(time);
}

void readInChar() {
  if (Serial.available() > 0) {
    inChar = Serial.read();
    return inChar;
  }
  return NULL;
}
