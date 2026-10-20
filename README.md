<<<<<<< HEAD
# README #

### What is this repository for? ###

* Football robot - finds and follows the rolling ball
* V1

### How do I get set up? ###
1. Raspberry Pi

The system runs on a Raspberry Pi with Raspberry Pi OS or a compatible Linux distribution.
Hardware requirements
Raspberry Pi with a compatible camera.
Motor-control hardware and connected drive motors.
Adafruit 16-channel PWM/Servo HAT or compatible PCA9685-based hardware.
Sense HAT for IMU-based rotation tracking and LED indicators, where used.

Software requirements
Python 3.
OpenCV.
Git.
MySQL-compatible database server.
Apache HTTP Server and PHP for the web dashboard.

The robot control program uses the command file:
/var/lib/football_robot/robot_command.txt
The website's Start button writes a START command through the command-handling script. The main Python program reads this command and transitions from the waiting state into the search routine.

Dependencies

Install the required Python libraries:
python3 -m pip install \
    opencv-python \
    numpy \
    adafruit-circuitpython-servokit \
    sense-hat \
    PyMySQL

Dependencies

Install the required Python libraries:

python3 -m pip install \
    opencv-python \
    numpy \
    adafruit-circuitpython-servokit \
    sense-hat \
    PyMySQL

Database Configuration
The application stores robot telemetry in the robot_status database table. The recorded fields include:
time
state
direction
acceleration
speed

Create the database and table using the project's SQL schema, if provided. Otherwise, configure the schema to match the fields expected by database_connector.py and robot_data.php.

Web dashboard
Deploy the website files to the configured Apache document root, commonly:
/var/www/html/
The dashboard uses PHP to handle the Start command and retrieve telemetry. JavaScript periodically requests data from robot_data.php and updates the displayed values.
Ensure Apache has the required PHP support and that the PHP scripts can connect to the database.

Command-file permissions
The Apache web-server user and the user running the robot-control program may be different Linux users. Configure permissions so that the command-handling script can write to the command file without granting broad write access to the system.
Keep the command file outside the public website directory. Do not solve permission problems by making the entire application directory world-writable or running arbitrary web requests with unrestricted root privileges.


