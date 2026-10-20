import threading

class Telemetry:
     """Store the latest robot status and motion measurements."""
    def __init__(self):
        self.lock = threading.Lock() #to avoid race conditions in shared resource
        self.state = "UNKNOWN"
        self.direction = "STOP"
        self.acceleration = 0.0
        self.speed = 0.0
        
    def update(self, state=None, direction=None,
               acceleration=None, speed=None):
        """
        Update the supplied telemetry fields.

        Fields passed as None retain their previous values.
        A lock prevents simultaneous access from interfering with updates.
        """
        with self.lock:
            if state is not None:
                self.state = state
            if direction is not None:
                self.direction = direction
            if acceleration is not None:
                self.acceleration = acceleration
            if speed is not None:
                self.speed = speed
                
    def get(self):
        with self.lock:
            return(
                self.state,
                self.direction,
                self.acceleration,
                self.speed
            )