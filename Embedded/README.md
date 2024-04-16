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
