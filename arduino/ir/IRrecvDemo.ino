/*
 * IRremote: IRrecvDemo - demonstrates receiving IR codes with IRrecv
 * An IR detector/demodulator must be connected to the input RECV_PIN.
 * Version 0.1 July, 2009
 * Copyright 2009 Ken Shirriff
 * http://arcfn.com
 */

#define KEY_0: 0xFF6897
#define KEY_1: 0xFF30CF
#define KEY_2: 0xFF18E7
#define KEY_3: 0xFF7A85
#define KEY_4: 0xFF10EF
#define KEY_5: 0xFF38C7
#define KEY_6: 0xFF5AA5
#define KEY_7: 0xFF42BD
#define KEY_8: 0xFF4AB5
#define KEY_9: 0xFF52AD

#include <IRremote.h>

int RECV_PIN = 9;

IRrecv irrecv(RECV_PIN);

decode_results results;

void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn(); // Start the receiver
}

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
		default:
			Serial.println(results.value, HEX);
	}
    irrecv.resume(); // Receive the next value
  }
}
