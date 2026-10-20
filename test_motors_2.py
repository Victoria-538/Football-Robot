import time
from sense_hat import SenseHat

from motor_control_func import (
    forward,
    backward,
    turn_left,
    turn_right,
    stop
)

sense = SenseHat()

# LED colours
X = (255, 0, 0)       # Red
O = (255, 255, 255)   # White

# Arrow patterns
arrows = {
    "BACKWARD": [
        O, O, O, X, X, O, O, O,
        O, O, X, X, X, X, O, O,
        O, X, O, X, X, O, X, O,
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
    ],
    "FORWARD": [
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
        O, O, O, X, X, O, O, O,
        O, X, O, X, X, O, X, O,
        O, O, X, X, X, X, O, O,
        O, O, O, X, X, O, O, O,
    ],
    "LEFT": [
        O, O, O, O, O, O, O, O,
        O, O, X, O, O, O, O, O,
        O, X, O, O, O, O, O, O,
        X, X, X, X, X, X, X, O,
        X, X, X, X, X, X, X, O,
        O, X, O, O, O, O, O, O,
        O, O, X, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
    ],
    "RIGHT": [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, X, O, O,
        O, O, O, O, O, O, X, O,
        O, X, X, X, X, X, X, X,
        O, X, X, X, X, X, X, X,
        O, O, O, O, O, O, X, O,
        O, O, O, O, O, X, O, O,
        O, O, O, O, O, O, O, O,
    ],
}


def test_movement(name, movement_function):
    print(f"Testing {name}")

    sense.set_pixels(arrows[name])

    movement_function(0.2)  # Use your defined function
    time.sleep(2)

    stop()
    sense.clear()
    time.sleep(1)


try:
    print("Starting motor and LED tests.")

    test_movement("FORWARD", forward)
    test_movement("BACKWARD", backward)
    test_movement("LEFT", turn_left)
    test_movement("RIGHT", turn_right)

    print("All tests completed.")

finally:
    stop()
    sense.clear()
    print("Motors stopped; LED matrix cleared.")
