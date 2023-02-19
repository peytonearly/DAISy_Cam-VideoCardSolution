
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

void setup() {
  // put your setup code here, to run once:

  //Configure pins to output to motor driver
pinMode(pul_plus_out, OUTPUT);
pinMode(pul_minus_out, OUTPUT);
pinMode(dir_plus_out, OUTPUT);
pinMode(dir_minus_out, OUTPUT);

  //Configure pins to recieve input from Pi
pinMode(pul_plus_in, INPUT);
pinMode(pul_minus_in, INPUT);
pinMode(dir_plus_in, INPUT);
pinMode(dir_minus_in, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

//Check for High pul_plus_in input from Raspberry Pi
if (digitalRead(pul_plus_in)==HIGH){
  digitalWrite(pul_plus_out, HIGH); //send high signal to PUL+ on driver
  delay(t); // wait for time t
  digitalWrite(pul_plus_out, LOW); // reset to low signal to PUL+ on driver
  delay(t); // wait for time t
}

//Check for High pul_minus_in input from Raspberry Pi
if (digitalRead(pul_minus_in)==HIGH){
  digitalWrite(pul_minus_out, HIGH); //send high signal to PUL- on driver
  delay(t); // wait for time t
  digitalWrite(pul_minus_out, LOW); // reset to low signal to PUL- on driver
  delay(t); // wait for time t
}

//Check for High dir_plus_in input from Raspberry Pi
if (digitalRead(dir_plus_in)==HIGH){
  digitalWrite(dir_plus_out, HIGH); //send high signal to DIR+ on driver
  delay(t); // wait for time t
  digitalWrite(dir_plus_out, LOW); // reset to low signal to DIR+ on driver
  delay(t); // wait for time t
}

//Check for High dir_minus_in input from Raspberry Pi
if (digitalRead(dir_minus_in)==HIGH){
  digitalWrite(dir_minus_out, HIGH); //send high signal to DIR- on driver
  delay(t); // wait for time t
  digitalWrite(dir_minus_out, LOW); // reset to low signal to DIR- on driver
  delay(t); // wait for time t
} 

}
