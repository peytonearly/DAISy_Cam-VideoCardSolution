int sensorPin = A0; // Assign analog pin 0 for temperature sensor readings
float vRef = 5.0; // Assign reference voltage
float avgTemp[30]; // Variable holds the last 30 seconds of temperature readings
int idx = 0; // Variable holds current avgTemp array index

void setup() {
  Serial.begin(9600); // Start serial connection with computer
}

// void loop() {
//   int reading = analogRead(sensorPin); // Collect temp sensor voltage reading
//   float voltage = reading * vRef / 1024.0; // Convert reading to voltage
//   Serial.print(voltage); Serial.println(" volts");

//   float tempC = (voltage - 0.5) * 100; // Convert voltage reading to Celsius
//   Serial.print(tempC); Serial.println(" degrees C");

//   float tempF = (tempC * 9.0/5.0) + 32.0; // Convert Celsius to Fahrenheit
//   Serial.print(tempF); Serial.println(" degrees F");

//   delay(1000);
// }

void loop() {
  int reading = analogRead(sensorPin); // Collect temperature sensor voltage reading
  float voltage = reading * vRef / 1024.0; // Convert reading to voltage
  float temp = (voltage - 0.5) * 100; // Convert voltage reading to Celsius

  avgTemp[idx] = temp; // Add temperature value to avg array

  // Calculate 30-second average
  float sum = 0;
  float count = 0;
  for(int i=0; i < 30; i++) {
    if(avgTemp[i]){
      count++;
      sum += avgTemp[i];
    }
  }
  float avg = sum/count;

  // Print values
  Serial.print(temp); Serial.print(" "); Serial.println(avg);
  
  // Check if index needs to be reset
  idx++;
  if(idx >= 30) {
    idx = 0;
  }

  delay(1000);
}