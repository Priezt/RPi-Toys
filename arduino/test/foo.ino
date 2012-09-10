int pin = 9;
int led = 13;


void setup(){
	pinMode(pin, INPUT);
	pinMode(led, OUTPUT);
}

void loop(){
	int pinStatus = 0;
	pinStatus = digitalRead(pin);
	if(pinStatus){
		digitalWrite(led, HIGH);
		delay(500);
	}else{
		digitalWrite(led, LOW);
		delay(10);
	}
}
