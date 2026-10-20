
from LED_matrix import show_left, show_right, show_up
from motor_control_func import forward, turn_left, turn_right, stop


def control_chassis(ball_x, ball_width, image_width):
    """
    Control the robot chassis based on the detected ball position and size.

    The robot turns to align with the ball, then moves forward until
    the ball reaches the target width. The LED matrix indicates the
    commanded movement direction.

    Args:
        ball_x: Horizontal centre coordinate of the detected ball.
        ball_width: Width of the detected ball's bounding box in pixels.
        image_width: Width of the camera image in pixels.
    """
    image_centre_x = image_width // 2
    error_x = ball_x - image_centre_x

    target_width = 150
    deadband = 80

    # Slower turning for initial alignment
    turn_speed = 0.1
    forward_speed = 0.2
    
    #Monitoring
    print(
        f"Ball X={ball_x}, error={error_x}, "
        f"width={ball_width}"
    )

    if error_x < -deadband:
        print("COMMAND: LEFT")
        show_left()
        turn_left(turn_speed)

    elif error_x > deadband:
        print("COMMAND: RIGHT")
        show_right()
        turn_right(turn_speed)

    elif ball_width < target_width:
        print("COMMAND: FORWARD")
        show_up()
        forward(forward_speed)

    else:
        print("COMMAND: STOP")
        stop()
