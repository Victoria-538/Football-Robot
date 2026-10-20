from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()


X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

def show_up():
    up = [
    O, O, O, X, X, O, O, O,
    O, O, X, X, X, X, O, O,
    O, X, X, O, O, X, X, O,
    X, X, O, O, O, O, X, X,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    ]
    sense.set_pixels(up)

def show_down():
    down = [
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    X, X, O, O, O, O, X, X,
    O, X, X, O, O, X, X, O,
    O, O, X, X, X, X, O, O,
    O, O, O, X, X, O, O, O,
    ]
    sense.set_pixels(down)

def show_right():
    right = [
    O, O, O, X, X, O, O, O,
    O, O, O, O, X, X, O, O,
    O, O, O, O, O, X, X, O,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    O, O, O, O, O, X, X, O,
    O, O, O, O, X, X, O, O,
    O, O, O, X, X, O, O, O,
    ]
    sense.set_pixels(right)

def show_left():
    left = [
    O, O, O, X, X, O, O, O,
    O, O, X, X, O, O, O, O,
    O, X, X, O, O, O, O, O,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    O, X, X, O, O, O, O, O,
    O, O, X, X, O, O, O, O,
    O, O, O, X, X, O, O, O,
    ]
    sense.set_pixels(left)
