/*
Use the following command to connect to serial port
	screen /dev/ttyACM0 9600
*/

int led = 13;
int x = 1;

void setup(){
	pinMode(led, OUTPUT);
	Serial.begin(9600);
	Serial.println("Hello, world");
	delay(2000);
}

void loop(){
	Serial.println(x);
	x+=1;
	digitalWrite(led, HIGH);
	delay(500);
	digitalWrite(led, LOW);
	delay(500);
}

