import pymysql
import time
from datetime import datetime


def log_status(state, direction = None, acceleration=None, speed = None):
     """
    Insert a robot telemetry record into the MySQL database.

    Args:
        state: Current robot operating state.
        direction: Current movement direction.
        acceleration: Measured robot acceleration.
        speed: Measured robot speed.
    """

    #establish connection
    conn = pymysql.connect(
        host = '127.0.0.1',
        user = 'victoria',
        password = '*****',
        database = 'football_robot',
        cursorclass = pymysql.cursors.DictCursor)

    with conn:
        with conn.cursor() as c:
            #create new record
            time_now = datetime.now()
            sql = "INSERT INTO robot_status(time, state, direction, acceleration, speed) VALUES (%s, %s, %s, %s, %s)"
            c.execute(sql, (time_now, state, direction, acceleration, speed))
    
        conn.commit()
    
   
        