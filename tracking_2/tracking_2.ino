#include<SoftwareSerial.h>
#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN      4        // RFID resetpin
#define SS_PIN       2        // RFID selection pin
MFRC522 mfrc522(SS_PIN, RST_PIN);  // MFRC522 object declaration
SoftwareSerial I2CBT(8,7);   //bluetooth RX,TX

/*pin definition*/
#define L298N_ENA 3
#define L298N_ENB 5
#define L298N_IN1 1
#define L298N_IN2 6
#define L298N_IN3 9
#define L298N_IN4 10

#define R2  A0  // Define Second Right Sensor Pin
#define R1  A1  // Define First Right Sensor Pin
#define M   A2  // Define Middle Sensor Pin
#define L1  A3  // Define First Left Sensor Pin
#define L2  A4  // Define Second Leftt Sensor Pin

#define DEBUG

bool state = true;

#include "track.h"
#include "node.h"
#include "bluetooth.h"
#include "RFID.h"

void setup()
{
    //BT.begin(9600); //bluetooth initialization
    
    SPI.begin();         //RFID initialization
    mfrc522.PCD_Init();

    /*define your pin mode*/
   //Serial.begin(9600);
   I2CBT.begin(9600);
   pinMode(L298N_IN1,   OUTPUT);
   pinMode(L298N_IN2,   OUTPUT);
   pinMode(L298N_IN3,   OUTPUT);
   pinMode(L298N_IN4,   OUTPUT);
   pinMode(L298N_ENA, OUTPUT);
   pinMode(L298N_ENB, OUTPUT);
   pinMode(R1, INPUT); 
   pinMode(R2, INPUT);
   pinMode(M,  INPUT);
   pinMode(L1, INPUT);
   pinMode(L2, INPUT);
   digitalWrite(L298N_IN1, LOW);
   digitalWrite(L298N_IN2, HIGH);
   digitalWrite(L298N_IN3, LOW);
   digitalWrite(L298N_IN4, HIGH);

}

void loop()
{
    /*TODO*/
   if(state == true){
    Tracing_Mode();
   }
   else 
    Start_Mode();

    //I2CBT.write("a");
    //MotorCheck();
    //delay(100);
  rfid();
}

