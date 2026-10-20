import threading
import time

from database_connector import log_status

class DatabaseLogger(threading.Thread):
     """Log robot telemetry data to the database at regular intervals."""
    def __init__(self, telemetry, interval=1.0):
        super().__init__(daemon=True)

        self.telemetry = telemetry
        self.interval = interval
        self.running = True
        
    def run(self):
        while self.running:
            #get the telemetry data
            state, direction, acceleration, speed = self.telemetry.get()
            
            #log into database
            log_status(state, direction, acceleration, speed)
            
            #wait before logging again
            time.sleep(self.interval)
            
    def stop(self):
        self.running = False