/*******************************************************************************
* Copyright 2016 ROBOTIS CO., LTD.
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*     http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*******************************************************************************/

#include <DynamixelShield.h>

#if defined(ARDUINO_AVR_UNO) || defined(ARDUINO_AVR_MEGA2560)
  #include <SoftwareSerial.h>
  SoftwareSerial soft_serial(7, 8); // DYNAMIXELShield UART RX/TX
  #define DEBUG_SERIAL soft_serial
#elif defined(ARDUINO_SAM_DUE) || defined(ARDUINO_SAM_ZERO)
  #define DEBUG_SERIAL SerialUSB    
#else
  #define DEBUG_SERIAL Serial
#endif

const uint8_t DXL_ID = 1;
const float DXL_PROTOCOL_VERSION = 2.0;
uint32_t BAUDRATE = 57600;
uint32_t NEW_BAUDRATE = 1000000; //1Mbsp

DynamixelShield dxl;

void setup() {

  // Set Port baudrate to 57600bps. This has to match with DYNAMIXEL baudrate.
  dxl.begin(BAUDRATE);
  // Set Port Protocol Version. This has to match with DYNAMIXEL protocol version.
  dxl.setPortProtocolVersion(DXL_PROTOCOL_VERSION);
  int i;
  for(i=0; i<10; i++){
    dxl.torqueOff(i);
    // Set a new baudrate(1Mbps) for DYNAMIXEL
    dxl.setBaudrate(i, NEW_BAUDRATE);
    dxl.torqueOn(i);
  }

}

void loop() {
  // put your main code here, to run repeatedly:
}
