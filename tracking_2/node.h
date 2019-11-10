// dir = 0 : advance(先停2s)
// dir = 1 : left(原地轉彎90度，一個輪子動)
// dir = 2 : right
// dir = 3 : 迴轉(整個翻)

#ifndef NODE_H_
#define NODE_H_

#include "track.h"
#include "bluetooth.h"

const int turn_time = 1200;
static int m=0;
static int l1=0;
static int r1=0;
static int l2=0;
static int r2=0;
extern float output;

void MotorWriting(double vR, double vL);
void Tracing_Mode();
byte* rfid(byte* idSize=NULL);

// TODO: determine the behavior of each port when occuring a node(here represented as an integer)
void node(int dir){
  
  if(dir==0)
  {
    //MotorWriting((200)/1.3,(200));
    MotorWriting((255),(255/1.3));
    delay(250);
    Tracing_Mode();
  }
  else if(dir==1)
  { 
    /*static int r2=0; 
    MotorWriting(255,150);
    delay(turn_time);
    r2=digitalRead(R2);
    if(r2==1){
    Tracing_Mode();
    }
    else{
      MotorWriting(255,150);
      delay(50);
    }*/
    MotorWriting((127),(127/(1.3)));
    //MotorWriting((255),(255/(1.3)));
    delay(800);
    MotorWriting((127),0);
    delay(turn_time);
    while(!digitalRead(L2)){}
    while(!digitalRead(L1)){}
    Tracing_Mode();
  }
  else if(dir==2)
  {
    /*static int l2=0;
    MotorWriting(255,150);
    delay(turn_time);
    l2=digitalRead(L2);
    m=digitalRead(M);
    if((l2==1)){
    Tracing_Mode();
    }
    else{
      MotorWriting(255,150);
      delay(50);
    }
    Tracing_Mode();*/
    MotorWriting((127),(127/1.3));
    //MotorWriting((255),(255/1.3));
    delay(600);
    MotorWriting(0,(127/1.3));
    delay(turn_time);
    while(!digitalRead(R2)){}
    while(!digitalRead(R1)){}
    Tracing_Mode();
  }
  else if(dir==3)
  {
    //static int m=0;
    //MotorWriting(100/1.8,100);
    while(!rfid()){I2CBT.write("543\n");}
    I2CBT.write("read uid here\n");
    digitalWrite(L298N_IN3, HIGH);
    digitalWrite(L298N_IN4, LOW);
    MotorWriting(255,(255/1.3));
    delay((turn_time));
    while(!(digitalRead(R1)+digitalRead(M)+digitalRead(L1))){}
    digitalWrite(L298N_IN3, LOW);
   digitalWrite(L298N_IN4, HIGH);
    Tracing_Mode();
  }
}

#endif
