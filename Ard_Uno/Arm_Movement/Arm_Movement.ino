
// Associate pin numbers with outputs to driver
int pul_plus_out = 2; //define which pin connects to PUL+
int pul_minus_out = 3; //define which pin connects to PUL-
int dir_plus_out = 4; //define which pin connects to DIR+
int dir_minus_out = 5; //define which pin connects to DIR-

//Associate pin numbers with inputs from Raspberry Pi
int  pul_plus_in = 14; //define which pin is is responsible for turning on PUL+
int  pul_minus_in = 15; //define which pin is is responsible for turning on PUL-
int  dir_plus_in = 16; //define which pin is is responsible for turning on DIR+
int  dir_minus_in = 17; //define which pin is is responsible for turning on DIR-

// Set delay time in miliseconds
int t = 1000; //[ms] //delay time to send high signal to stepper motor

int input = 0; // Contains incoming arm command code

void setup() {
  //Configure pins to output to motor driver
  pinMode(pul_plus_out, OUTPUT);
  pinMode(pul_minus_out, OUTPUT);
  pinMode(dir_plus_out, OUTPUT);
  pinMode(dir_minus_out, OUTPUT);

  //Configure pins to recieve input from Pi
  // pinMode(pul_plus_in, INPUT);
  // pinMode(pul_minus_in, INPUT);
  // pinMode(dir_plus_in, INPUT);
  // pinMode(dir_minus_in, INPUT);

  Serial.begin(9600); // Start serial communication with baudrate=9600
}

void loop() {
  input = Serial.read(); // Read input from serial port

  // Perform action depending on received input
  switch (input) {
    case -1: // Returned when no input > Do nothing
      break;
    case 0: // Arm fully closed
      digitalWrite(pul_plus_out, HIGH); //send high signal to PUL+ on driver
      delay(t); // wait for time t
      digitalWrite(pul_plus_out, LOW); // reset to low signal to PUL+ on driver
      delay(t); // wait for time t
      break;
    case 1: // Arm fully opened
      digitalWrite(pul_minus_out, HIGH); //send high signal to PUL- on driver
      delay(t); // wait for time t
      digitalWrite(pul_minus_out, LOW); // reset to low signal to PUL- on driver
      delay(t); // wait for time t
      break;
    case 2: // Stop in place
      digitalWrite(dir_plus_out, HIGH); //send high signal to DIR+ on driver
      delay(t); // wait for time t
      digitalWrite(dir_plus_out, LOW); // reset to low signal to DIR+ on driver
      delay(t); // wait for time t
      break;
    case 3: // Loop between open and closed
      digitalWrite(dir_minus_out, HIGH); //send high signal to DIR- on driver
      delay(t); // wait for time t
      digitalWrite(dir_minus_out, LOW); // reset to low signal to DIR- on driver
      delay(t); // wait for time t
      break;
  }

}
