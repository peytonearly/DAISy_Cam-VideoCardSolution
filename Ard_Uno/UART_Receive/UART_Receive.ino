int input = 0; // Rx input

void setup() {
  // pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  while (!Serial.available()) {
    // Serial.println("Awaiting input...");
    // digitalWrite(LED_BUILTIN, HIGH);
    // delay(500);

    // digitalWrite(LED_BUILTIN, LOW);
    // delay(500);
  } // Wait until data is available
  input = Serial.read(); // Read until timeout
  Serial.println(char(input));
}
