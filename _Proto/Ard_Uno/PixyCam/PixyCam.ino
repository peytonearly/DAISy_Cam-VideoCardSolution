#include <Pixy2.h>

// Create Pixy object
Pixy2 pixy;

// Initialize repeatedly used variables
int i;
int x, x1, x2, x3, x4, y, y1, y2, y3, y4;

unsigned long time;

void setup()
{
  Serial.begin(9600);
  Serial.print("Starting at 9600 baud...\n");

  pixy.init();
}

void loop()
{
  // Grab blocks
  pixy.ccc.getBlocks();

  // Pre-define as irrational values
  x1=-1, x2=-1; // x3=-1, x4=-1;
  y1=-1, y2=-1; // y3=-1, y4=-1;

  // Print detected blocks
  if (pixy.ccc.numBlocks)
  {
    for (i=0; i<pixy.ccc.numBlocks; i++)
    {
      x = pixy.ccc.blocks[i].m_x;
      y = pixy.ccc.blocks[i].m_y;
      switch (pixy.ccc.blocks[i].m_signature) 
      {
        case 1:
          x1 = x;
          y1 = y;
          break;
        case 2:
          x2 = x;
          y2 = y;
          break;
        // case 3:
        //   x3 = x;
        //   y3 = y;
        //   break;
        // case 4:
        //   x4 = x;
        //   y4 = y;
        //   break;
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
  // Serial.print(x3);
  // Serial.print(",");
  // Serial.print(y3);
  // Serial.print(",");
  // Serial.print(x4);
  // Serial.print(",");
  // Serial.print(y4);
  // Serial.print(",");
  Serial.println(time);
}