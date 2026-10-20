
from adafruit_servokit import ServoKit

# Initialise the Servo Driver HAT
kit = ServoKit(channels=16)

# Motor mapping
right_motor = kit.continuous_servo[0]
left_motor = kit.continuous_servo[1]


def stop():
    """Stop both continuous-rotation servos."""
    right_motor.throttle = 0
    left_motor.throttle = 0

    # Disable PWM output on both channels
    kit._pca.channels[0].duty_cycle = 0
    kit._pca.channels[1].duty_cycle = 0

def forward(speed=0.2):
    """Drive both motors forward."""
    
    # Apply opposite throttle signs to account for motor orientation, offset to account for motors turning at different speeds
    right_motor.throttle = -speed
    left_motor.throttle = speed+0.2


def backward(speed=0.2):
    """Drive both motors backward."""
    right_motor.throttle = speed+0.2
    left_motor.throttle = -speed


def turn_left(speed=0.2):
    """Rotate the chassis left."""
    right_motor.throttle = -speed-0.2
    left_motor.throttle = -speed


def turn_right(speed=0.2):
    """Rotate the chassis right."""
    right_motor.throttle = speed+0.2
    left_motor.throttle = speed
