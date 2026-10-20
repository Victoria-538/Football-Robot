"""program to test that all the database scripts are working together successfukky"""
from telemetry import Telemetry
from database_logger import DatabaseLogger
import time

telemetry = Telemetry()
logger = DatabaseLogger(telemetry, interval = 1.0)
logger.start()

telemetry.update(state = "SEARCH", direction = "LEFT", acceleration = 0.0, speed = 0.2)

time.sleep(5)
logger.stop()