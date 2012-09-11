#define KEY_0 0xFF6897
#define KEY_1 0xFF30CF
#define KEY_2 0xFF18E7
#define KEY_3 0xFF7A85
#define KEY_4 0xFF10EF
#define KEY_5 0xFF38C7
#define KEY_6 0xFF5AA5
#define KEY_7 0xFF42BD
#define KEY_8 0xFF4AB5
#define KEY_9 0xFF52AD
#define KEY_POWER 0xFFA25D
#define KEY_MODE 0xFF629D
#define KEY_MUTE 0xFFE21D
#define KEY_PLAY 0xFF22DD
#define KEY_BACK 0xFF02FD
#define KEY_FORWARD 0xFFC23D
#define KEY_EQ 0xFFE01F
#define KEY_MINUS 0xFFA857
#define KEY_PLUS 0xFF906F
#define KEY_SWITCH 0xFF9867
#define KEY_USD 0xFFB04F

#include <IRremote.h>
#include <Servo.h>

int RECV_PIN = 9;
int LED = 13;
int angle = 90;
int SERVO_PORT = 11;

IRrecv irrecv(RECV_PIN);
Servo myservo;

decode_results results;

void setup()
{
//  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  irrecv.enableIRIn(); // Start the receiver
  myservo.attach(SERVO_PORT);
}

void blink(){
	digitalWrite(LED, HIGH);
	delay(50);
	digitalWrite(LED, LOW);
	delay(50);
}

void loop(){
	if(irrecv.decode(&results)){
		switch(results.value){
			case KEY_BACK:
				angle = 1;
				blink();
				break;
			case KEY_FORWARD:
				angle = 180;
				blink();
				break;
			case KEY_PLAY:
				angle = 90;
				blink();
				break;
		}
		irrecv.resume(); // Receive the next value
	}
	myservo.write(angle);
	delay(50);
}

/*
void loop() {
  if (irrecv.decode(&results)) {
  	switch(results.value){
		case KEY_0:
			Serial.println(0);
			break;
		case KEY_1:
			Serial.println(1);
			break;
		case KEY_2:
			Serial.println(2);
			break;
		case KEY_3:
			Serial.println(3);
			break;
		case KEY_4:
			Serial.println(4);
			break;
		case KEY_5:
			Serial.println(5);
			break;
		case KEY_6:
			Serial.println(6);
			break;
		case KEY_7:
			Serial.println(7);
			break;
		case KEY_8:
			Serial.println(8);
			break;
		case KEY_9:
			Serial.println(9);
			break;
		case KEY_POWER:
			Serial.println("POWER");
			break;
		case KEY_MODE:
			Serial.println("MODE");
			break;
		case KEY_MUTE:
			Serial.println("MUTE");
			break;
		case KEY_PLAY:
			Serial.println("PLAY");
			break;
		case KEY_BACK:
			Serial.println("BACK");
			break;
		case KEY_FORWARD:
			Serial.println("FORWARD");
			break;
		case KEY_EQ:
			Serial.println("EQ");
			break;
		case KEY_MINUS:
			Serial.println("MINUS");
			break;
		case KEY_PLUS:
			Serial.println("PLUS");
			break;
		case KEY_SWITCH:
			Serial.println("SWITCH");
			break;
		case KEY_USD:
			Serial.println("USD");
			break;
//		default:
//			Serial.println(results.value, HEX);
	}
    irrecv.resume(); // Receive the next value
  }else{
  	digitalWrite(LED, HIGH);
	delay(1000);
  	digitalWrite(LED, LOW);
	delay(1000);
  }
}*/
