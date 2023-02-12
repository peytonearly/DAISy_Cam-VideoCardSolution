int sensorPin = A0; // Assign analog pin used for temperature sensor

void setup() {
  Serial.begin(9600);
}

void loop() {
  int reading = analogRead(sensorPin); // Collect voltage reading from temperature sensor
  float voltage = reading * (5.0/1024.0); // Convert to voltage value

  Serial.print(voltage); Serial.println(" volts")

  float tempC = (voltage - 0.5) * 100; // Convert to Celsius
  Serial.print(tempC); Serial.println( "degrees C");

  float tempF = (tempC * 9.0 / 5.0) + 32.0; // Convert to Fahrenheit
  Serial.print(tempF); Serial.println(" degrees F");

  delay(1000);
}