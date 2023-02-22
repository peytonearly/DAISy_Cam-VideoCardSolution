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
