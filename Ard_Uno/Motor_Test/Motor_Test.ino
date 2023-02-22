int x;
void setup() {
pinMode(9,OUTPUT); // set Pin9 as PUL
pinMode(8,OUTPUT); // set Pin8 as DIR
}
void loop() {
digitalWrite(8,HIGH); // set high level direction
for(x = 0; x < 400; x++) // repeat 400 times a revolution when setting 400 on driver
{
digitalWrite(9,HIGH); // Output high
delayMicroseconds(5000); // set rotate speed
digitalWrite(9,LOW); // Output low
delayMicroseconds(5000); // set rotate speed
}

}

int input = 0; // Contains incoming arm command
int step = 0; // Current 
float TotalRev = 13/4; // [revs/open]
int DeployTime = 15*60; // [s] 
int StepperRes = 40000; // [steps/rev] Resolution set by dip switch on driver
int StepLim = TotalRev * (StepperRes); // [steps]
int StepRate = StepLim/DeployTime; // [steps/sec]
int Delay = 1 / (2*StepRate); // [s] Pulse time length

void setup() {
    pinMode(9, OUTPUT); // Set pin 9 as PUL+
    pinMode(8, OUTPUT); // Set pin 8 as Dir+
    Serial.begin(9600); // Start serial communication
}