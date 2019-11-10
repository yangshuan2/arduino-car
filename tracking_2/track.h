// TODO: Write the functions from what you learned in former labs.
#ifndef TRACK_H_
#define TRACK_H_

#include "node.h"
#include "bluetooth.h"
#include<time.h>
bool R_dir = true;                  // if dir == ture, mean right-motor is forwarding. On the other hand, backwarding.
bool L_dir = true;                  // if dir == ture, mean Left-motor is forwarding. On the other hand, backwarding.

float previous_error = 0;
float integral = 0;
float output = 0;
const float dt = 0.01;
const float Kp = 1/5;//15
const float Ki = 1/3;//10
const float Kd = 1/3;//12
//151320
//153020 
//152520(good)
//132520
//15 7 18
/**************************************/
/*   Function Prototypes Define Here  */
/*   Finish TODO in Blacking Function */
/**************************************/
void Tracing_Mode();
void Start_Mode();
void MotorWriting(double vR, double vL);
void MotorInverter(int motor, bool& dir);
void Send_OK();
byte* rfid(byte* idSize=NULL);

void Start_Mode() {
   //TODO
   /****************/
   /* Stop the car */
   /****************/
   analogWrite(L298N_ENA,0);
   analogWrite(L298N_ENB,0);
   if(ask_direction() == 0)
    state = true;
}

//TODO
void Tracing_Mode() {
   //TODO
   // Simple Tracking
   /*************************************************/
   /* Read the sensor value and determine wether to */
   /* turn left or turn right or go straight        */
   /*************************************************/

   //TODO
   // Initialize Senor value
   static int r2=0;
   static int r1=0; // right-inner sensor
   static int m=0; // middle sensor
   static int l1=0; // left-inner sensor
   static int l2=0;
   clock_t t1,t2;
   t1=0;
   //TODO
   // Using "MotorWriting()" to turn or go straight
   // depending on the sensors value
   r2 = digitalRead(R2);
   r1 = digitalRead(R1);
   m = digitalRead(M);
   l1 = digitalRead(L1);
   l2 = digitalRead(L2);

   //if((r1+l1+r2+l2>2)||(r2==1&&l2==1)||(r1==1&&l2==1)||(r2==1&&l1==1)||(m==1&&r2==1)||(m==1&&l2==1)){
   if((r1+l1+r2+l2>2)||(r2==1&&l2==1)||(r1==1&&l2==1)||(r2==1&&l1==1)||(r2==1&&m==1)||(l2==1&&m==1)){
   
     //if (I2CBT.available()){
        I2CBT.write("N\n");
        //delay(200);
        //rfid();
     //}
     //MotorWriting(0,0);
     //delay(1000);
    }
   else if(r2+l2) MotorWriting(((150+50*m+50*l2-100*r2)),((150+50*m+50*r2-100*l2)/1.15));
   else MotorWriting(((150+50*m+35*l1-70*r1)),((150+50*m+35*r1-70*l1)/1.15));
   /*else if(!(r1+r2+l1+l2) && m) MotorWriting(120,120/1.8);
   else {
    int setpoint = 0;
    //int measured_value = (r2+l2)?2*(r2-l2):(r1-l1);
    int measured_value = (2*r2)+r1-l1-(2*l2);
   
    float error = setpoint - measured_value;
    integral = integral + error*dt;
    float derivative = (error - previous_error)/dt;
    output = Kp*error + Ki*integral + Kd*derivative;
    previous_error = error;
    delay(dt);
    /*if(output>=(135/8))
    {
     MotorWriting(255/1.3,0); 
    }
    else if(output<=(-135/8))
    {
     MotorWriting(0,255);  
    }
    else
    {
     MotorWriting((120+output*8)/1.3,(120-output*8));
    }*/
    
   //}
   //rfid();


  
   //delay(200);
   
   int dir = ask_direction();
   if(dir != -1){
    node(dir);
    previous_error = 0;
    integral = 0;
    output = 0;
   }
   
   
}

//TODO
void MotorWriting(double vR, double vL) {
   //TODO
   /*************************************************/
   /* Assign vR to right-motor and vL to left-motor */
   /* Reverse the motor direction if necessary      */
   /*************************************************/
   /*if(vR < 0){
    if(R_dir){
      MotorInverter(L298N_ENB, R_dir);
    }
    analogWrite(L298N_ENB,-vR);
   }
   else{
    if(!R_dir){
      MotorInverter(L298N_ENB, R_dir);
    }
    analogWrite(L298N_ENB,vR);
   }
   if(vL < 0){
    if(L_dir){
      MotorInverter(L298N_ENA, L_dir);
    }
    analogWrite(L298N_ENA,-vL);
   }
   else{
    if(!L_dir){
      MotorInverter(L298N_ENA, L_dir);
    }
    analogWrite(L298N_ENA,vL);
   }*/
   analogWrite(L298N_ENB,vR);
   analogWrite(L298N_ENA,vL);
}

//TODO
void MotorInverter(int motor, bool& dir) {
   //TODO
   /*************************************/
   /* Reverse the dir for the given dir */
   /* value and motor(Left or Right)    */
   /*************************************/
   if(motor == L298N_ENB){
    if(dir){
      digitalWrite(L298N_IN3, HIGH);
      digitalWrite(L298N_IN4, LOW);
      dir = false;
    }
    else{
      digitalWrite(L298N_IN3, LOW);
      digitalWrite(L298N_IN4, HIGH);
      dir = true;
    }
   }
   else if(motor == L298N_ENA){
    if(dir){
      digitalWrite(L298N_IN1, HIGH);
      digitalWrite(L298N_IN2, LOW);
      dir = false;
    }
    else{
      digitalWrite(L298N_IN1, LOW);
      digitalWrite(L298N_IN2, HIGH);
      dir = true;
    }
   }

}

void MotorCheck() {
   digitalWrite(L298N_IN1, LOW);
   digitalWrite(L298N_IN2, HIGH);
   digitalWrite(L298N_IN3, LOW);
   digitalWrite(L298N_IN4, HIGH);
   MotorWriting(150, 150);
}

void Send_OK() {
   I2CBT.write('O');
}

#endif

