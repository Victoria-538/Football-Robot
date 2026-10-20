from sense_hat import SenseHat
import time

sense = SenseHat()

#added adjustment values for testing
REST_X = -0.06
REST_Y = 0.015
REST_Z = 0.976

while True:

    acceleration = sense.get_accelerometer_raw()

    print(
        f"x: {acceleration['x']:.3f}, "
        f"y: {acceleration['y']:.3f}, "
        f"z: {acceleration['z']:.3f}"
    )



    ax = acceleration['x'] - REST_X
    ay = acceleration['y'] - REST_Y
    az = acceleration['z'] - REST_Z

    print(
        f"ax: {ax:.3f}, "
        f"ay: {ay:.3f}, "
        f"az: {az:.3f}"
    )

    time.sleep(0.1)