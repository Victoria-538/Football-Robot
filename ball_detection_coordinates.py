import numpy as np
import cv2

def detect_ball(frame):
    """
    Detect a yellow ball in a camera frame.

    The frame is converted to HSV colour space, and a colour mask
    is used to identify yellow objects. Contours with an area greater
    than 1000 pixels are considered potential ball detections.

    Args:
        frame: Input camera frame in BGR format.

    Returns:
        Tuple containing the ball centre coordinates (x, y) and
        bounding box dimensions (width, height). Returns four None
        values if no suitable object is detected.
    """
    
    # Convert the BGR frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define lower and upper thresholds
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([35, 255, 255])

    #  Create a binary mask containing pixels within the range
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Find contours
    contours, _ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    # Examine each contour and ignore objects that are too small
    for contour in contours:

        area = cv2.contourArea(contour)
        # Ignore small objects
        if area > 1000:

            x, y, w, h = cv2.boundingRect(contour)
            centre_x = x + w // 2
            centre_y = y + h // 2
            print("Ball:", centre_x, centre_y)

            # Draw rectangle
            cv2.rectangle(frame,(x,y),(x+w, y+h),(0, 255, 0),2)

            # Draw centre point
            cv2.circle(frame,(centre_x,centre_y),5,(0, 0, 255),-1)

            return centre_x,centre_y, w, h

    # No ball found
    return None, None, None, None
