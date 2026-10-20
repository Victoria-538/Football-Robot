from sense_hat import SenseHat
from telemetry import Telemetry
import threading
import time
import math

# Constants for controlling the speedometer's behavior
UPDATE_INTERVAL = 0.1  # Time interval (in seconds) between velocity updates
SCALE_FACTOR = 0.5     # Factor to scale the calculated velocity (adjust for readability)
G = 9.81
#adjustment values to account mostly for Z (includes graviation)
REST_X = -0.06
REST_Y = 0.015
REST_Z = 0.976



#adjust acceleration for the skewed data
def get_linear_acceleration(acceleration):
    
    ax = acceleration['x'] - REST_X
    ay = acceleration['y'] - REST_Y
    az = acceleration['z'] - REST_Z

    #ignore very small accelerometer noise
    threshold = 0.02

    if abs(ax) < threshold:
        ax = 0

    if abs(ay) < threshold:
        ay = 0

    if abs(az) < threshold:
        az = 0
    return ax, ay, az

#integrate acceleration to calculate velocity
def calculate_velocity(acceleration, previous_velocity, delta_time):
    
    
    ax, ay, az = acceleration
       # If there is effectively no acceleration,
    # assume the robot is stationary
    if ax == 0 and ay == 0 and az == 0:
        return (0.0, 0.0, 0.0), 0.0

    #convert g to m/s^2
    ax *= G
    ay *= G
    az *= G
    
    #integrate acceleration
    vx = previous_velocity[0] + ax * delta_time
    vy = previous_velocity[1] + ay * delta_time
    vz = previous_velocity[2] + az * delta_time
    
    #calculate the resultant velocity vector
    velocity = math.sqrt(vx**2 + vy**2 + vz**2)
    return (vx, vy, vz), velocity

class Velocity(threading.Thread):
    
    def __init__(self, telemetry):
        super().__init__(daemon=True)
        self.telemetry = telemetry
        self.running = True
    
    def run(self):
        sense = SenseHat()
        vel_vector = (0.0, 0.0, 0.0)
        previous_time = time.time()
    
        while self.running:
           #get accelerometer data
           acceleration = sense.get_accelerometer_raw()
           #adjust for gravity
           linear_acceleration = get_linear_acceleration(acceleration)
        
           #time since previous measurement
           current_time = time.time()
           delta_time = current_time-previous_time
           previous_time = current_time
        
           vel_vector, speed = calculate_velocity(linear_acceleration,vel_vector,delta_time)
        
           #update telemetry
           self.telemetry.update(speed=speed)
           print(f"Speed: {speed:.2f} m/s")

           time.sleep(UPDATE_INTERVAL)
    def stop(self):
        
        self.running=False
        
if __name__ == "__main__":

    telemetry = Telemetry()

    velocity_thread = Velocity(telemetry)
    velocity_thread.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        velocity_thread.stop()
        velocity_thread.join()
    