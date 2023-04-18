char inChar;

void setup() {
  // pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
//   while (!Serial.available()) {
//     // Serial.println("Awaiting input...");
//     // digitalWrite(LED_BUILTIN, HIGH);
//     // delay(500);

//     // digitalWrite(LED_BUILTIN, LOW);
//     // delay(500);
//   } // Wait until data is available
//   input = Serial.read(); // Read until timeout
//   Serial.println(char(input)); // Print received character
// }

  inChar = readInChar();
  switch (inChar) {
    case '0': // No movement
      break;
    case '1': // Move arm toward fully open
      break;
    case '2': // Move arm toward fully closed
      break;
    case '3': // Loop between open and closed
      break;
  }  
}

char readInChar(){
  if (Serial.available() > 0) {
    inChar = Serial.read();
  }
  return inChar;
}