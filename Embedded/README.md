Description of Sensor Guided Robot:

This code is written for controlling a robot with two sensors and two motors connected to an Arduino board.

Setup Function (void setup()):

Initializes serial communication at a baud rate of 9600.
Sets pin 13 as an output pin to control an LED.
Sets pins 10, 11, 8, and 9 as output pins to control motor direction.
Sets analog pins A0 and A1 as input pins to read sensor values.
Loop Function (void loop()):

Reads analog sensor values from pins A0 and A1 and stores them in variables sensorValue1 and sensorValue2, respectively.
Prints the sensor values to the serial monitor.
Delays the program execution by 1000 milliseconds (1 second).
Checks the sensor values to determine the robot's motion:
If both sensor values are below 200, the robot moves forward.
If sensorValue2 is below 600 and sensorValue1 is above 600, the robot turns left.
If sensorValue1 is below 600 and sensorValue2 is above 600, the robot turns right.
If both sensor values are above 600, the robot stops.
Move Robot Function (void moveRobot(String motion)):

Accepts a string parameter motion to determine the desired robot motion.
Based on the value of motion, it activates the appropriate motor pins to achieve the desired motion:
"Forward": Sets the motors to move the robot forward.
"Back": Sets the motors to move the robot backward (not implemented in this code).
"Left": Sets the motors to turn the robot left.
"Right": Sets the motors to turn the robot right.
"Stop": Stops both motors.
This code essentially reads sensor values to detect obstacles and controls the robot's motion accordingly, allowing it to move forward, turn left, turn right, or stop based on the sensor readings. Additionally, it blinks an LED on pin 13 to indicate when the robot is in motion.

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Description of Temperature Measurement ESP32:

This code is for an ESP32 microcontroller-based project that involves Wi-Fi connectivity, MQTT messaging, ultrasonic distance sensing, and temperature monitoring. 
Include Libraries:

The code includes several libraries for various functionalities such as Wi-Fi connectivity (<WiFi.h>), MQTT messaging (<PubSubClient.h>), and ADC (Analog to Digital Conversion) operations (<driver/adc.h>).
Define Pins and Constants:

The code defines pin assignments for various components such as the ultrasonic sensor (trigPin and echoPin), an interrupt button (interruptButton), and LEDs (wifiLed and buttonLed). It also defines constants for Wi-Fi credentials (ssid and password) and MQTT server details (mqtt_server).
Setup Function (void setup()):

Configures pin modes for input/output.
Initializes serial communication for debugging purposes.
Connects to the Wi-Fi network specified by the ssid and password.
Establishes a connection to the MQTT broker (mqtt_server) using the client object.
Loop Function (void loop()):

Checks the status of the Wi-Fi connection and adjusts the state of the Wi-Fi LED accordingly.
Reads the temperature from an analog temperature sensor (LMT84) and publishes it to the MQTT topic "Temperatura".
Uses an ultrasonic sensor to measure distance and publishes the distance value to the MQTT topic "Capacidad" if movement is detected.
Detects button presses and decrements the counter variable if the button is pressed, publishing the updated counter value to the MQTT topic "Capacidad".
Delays the loop execution for 1 second.
This code essentially creates a system where temperature and movement data are collected and published to an MQTT broker over Wi-Fi. It can be used for various applications such as environmental monitoring, occupancy detection, or home automation.
