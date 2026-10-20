import cv2
import time
import os

from ball_detection_coordinates import detect_ball
from ball_chassis_control import control_chassis
from search_imu import Search
from telemetry import Telemetry
from database_logger import DatabaseLogger
from velocity import Velocity
from motor_control_func import turn_left, stop
from LED_matrix import show_left

# Robot operating states
STATE_SEARCH = "SEARCH"
STATE_APPROACH = "APPROACH"
STATE_SLEEP = "SLEEP"
STATE_WAITING = "WAITING"

# File used to receive START commands from the website
COMMAND_FILE = "/var/lib/football_robot/robot_command.txt"

# Remove any old command left from a previous run
if os.path.exists(COMMAND_FILE):
    os.remove(COMMAND_FILE)
def check_start_command():
    if not os.path.exists(COMMAND_FILE):
        return False

    with open(COMMAND_FILE, "r") as file:
        command = file.read().strip()

    if command == "START":
        os.remove(COMMAND_FILE)
        return True
    return False


# Initialise the camera and robot control modules
cap = cv2.VideoCapture(0) #to capture video
search = Search()         #search module(spinning around its axis)
telemetry = Telemetry()   #updating all database values
logger = DatabaseLogger(telemetry, interval =1.0) #thread that periodically logs database values
logger.start()
velocity_thread = Velocity(telemetry) #velocity measurement thread
velocity_thread.start()
print("Velocity thread started")

# Initialise the robot in the waiting state
state = STATE_WAITING
telemetry.update(state=state)

# Main robot control loop
while True:
    
    # Capture frame by frame
    ret, frame = cap.read()
    
    # Check for errors
    if not ret:
        print("Camera error")
        state = STATE_SLEEP
        stop()
        telemetry.update(state=state)
        continue
    
    
    # --------------------------------------------------
    # WAITING: Wait for a START command from the dashboard
    # --------------------------------------------------
    if state == STATE_WAITING:
        print("Waiting for dashboard START command...")

        if check_start_command():
            print("START command received!")
            search.reset()
            state = STATE_SEARCH
            telemetry.update(state=state)

        time.sleep(0.1)
        
    # --------------------------------------------------
    # SEARCH: Rotate the robot until the ball is detected
    # --------------------------------------------------
    elif state == STATE_SEARCH:
        print("SEARCH")

        # Look for the ball in current camera frame
        ball_x, ball_y, ball_width, ball_height = detect_ball(frame)

        if ball_x is not None:
            # Ball found: stop searching and start approaching
            stop()
            print("Ball found!")
            state = STATE_APPROACH
            telemetry.update(state=state)

        else:
            # Rotate the chassis while searching
            turn_left(0.05)
            show_left()
            time.sleep(0.02)
            stop()
            time.sleep(0.02)
        
            # Check cumulative rotation using the Sense HAT
            search_finished = search.update()

            if search_finished:
                stop()
                print("Search complete - ball not found")
                state = STATE_WAITING
                telemetry.update(state=state)

    # --------------------------------------------------
    # APPROACH: Move towards the detected ball
    # --------------------------------------------------
    elif state == STATE_APPROACH:
        print("APPROACH")
        
        # Re-detect the ball in current frame
        ball_x, ball_y, ball_width, ball_height = detect_ball(frame)
        
        if ball_x is not None:
            
            # Get image width
            image_width = frame.shape[1]
            
            # Send ball information to chassis controller
            control_chassis(ball_x,ball_width,image_width)
            
            # Success
            if ball_width >= 150:
                print("Target distance reached")
                stop()  # Stop both motors
                state = STATE_WAITING
                telemetry.update(state=state)
        else:
            # Stop and restart the search if the ball is lost
            print("Ball lost")
            stop()
            time.sleep(0.5)
            search.reset()
            state = STATE_SEARCH
            telemetry.update(state=state)
   
    # --------------------------------------------------
    # SLEEP: Stop the robot and exit the main loop
    # --------------------------------------------------
    elif state == STATE_SLEEP:

        print("SLEEP")
        stop()
        print("Robot stopped")

        break
    
    # Display frame for local monitoring
    cv2.imshow('frame', frame)

    # Quit with q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        stop()
        break
    
# Stop the threads
velocity_thread.stop()
velocity_thread.join()
logger.stop()

# Stop the camera
cap.release()
cv2.destroyAllWindows()