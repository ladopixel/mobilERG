/* ┌─────────────────────────────┐
   │ Developed by ladopixel      │
   │ mobilERG for Arduino        │
   └─────────────────────────────┘
*/

#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX
String ok_number = "your_number"; // My Known number to perform the action
String call_number;

void setup(){
  Serial.begin(9600);
  mySerial.begin(9600);

  /*
    It is important to leave some time for the Arduino to get the coverage and start well.

    If our Arduino restarts repeatedly, it may be because it does not have SIM800L coverage or that there is a connection error. 
    Verify that you have inserted the SIM card correctly.

    Remember that in the example the SIM card has the security pin removed.
  */

  // We give 10 seconds of time for coverage.
  delay(10000);

  // We send verification OK
  mySerial.println("AT\r\n");
  delay(1000);
}

void loop(){

  // We detect the phone number of the incoming call and store it in call_number
  call_number = "";
  while (mySerial.available()>0){
    delay(10);
    call_number += (char)mySerial.read(); 
  }
  
  /* 
    Optionally we can show the complete message that we get when receiving the call.
    Something like this: +CLIP: "xxxxxxxxx",161,"",0,"name_contact",0
  */
  Serial.print(call_number); 

  if (call_number.indexOf("RING")>-1){
    delay(1000);


    // I separate the 9-digit number that is calling me
    String num;
    int inicio=call_number.indexOf('"')+1;
    int fin=inicio+9;

    // The num variable holds the phone number that made the call.
    num=call_number.substring(inicio,fin);
    

    // I verify if the number that is calling me is the correct one to launch the action.
    if (num==ok_number){
      Serial.print("ok number");
  }else{
      Serial.print("error number");
    }
  }

  
  // Bidirectional communication bridge between serial ports, retransmitting data from one to the other.
  if (mySerial.available()){
    Serial.write(mySerial.read());
  }
  if (Serial.available()){
    while(Serial.available()) {
     mySerial.write(Serial.read());
    }
    mySerial.println();
  }

}
