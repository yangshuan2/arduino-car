#ifndef BLUETOOTH_H_
#define BLUETOOTH_H_

#include "track.h"
#include "node.h"
#include<SoftwareSerial.h>

char _cmd = 'n';
void MotorWriting(double vR, double vL);

void get_cmd(char &cmd) {
   delay(10); // Don't delete its!!
   //TODO
   /*************************************/
   /* Using I2CBT object to get command */
   /* Assign value to cmd               */
   /*************************************/
   if (I2CBT.available()){
        _cmd = I2CBT.read();
        Serial.write(_cmd);
        #ifdef DEBUG
   Serial.print("Cmd: ");
   Serial.println(cmd);
   #endif
   }
   // For debugging you can ignore this

}

// TODO: return the direction based on the command you read
int ask_direction(){  
  get_cmd(_cmd);
  /*if(_cmd != 'n') {
      MotorWriting(0,0);
  delay(1000);
  }*/
  switch(_cmd){
     case 'U':
       _cmd = 'n';
       return 0;
     case 'L':
       _cmd = 'n';
       return 1;
     case 'R':
       _cmd = 'n';
       return 2;
     case 'D':
       _cmd = 'n';
       return 3;
     case 'S':
       MotorWriting(0,0); 
       delay(2000); break;
     default:
       break;
   }
   
   _cmd = 'n';
   return -1;
}

// TODO: send the id back by BT
void send_byte(byte *id, byte idSize){

}

#endif
