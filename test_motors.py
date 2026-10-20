
import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
left = kit.continuous_servo[1]

try:
    left.throttle = 0
    print("Neutral signal sent. Connect motor power when ready.")
    time.sleep(2)

    left.throttle = 0.1
    print("Right motor test: low speed.")
    time.sleep(0.5)

finally:
    left.throttle = 0
    kit._pca.channels[1].duty_cycle = 0
    print("Test finished. Disconnect motor power if the motor keeps running.")
