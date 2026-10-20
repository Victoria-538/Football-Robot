from sense_hat import SenseHat

class Search:
     """Track the robot's cumulative yaw rotation during a search."""
    def __init__(self):
        self.sense = SenseHat()
        self.previous_yaw = None
        self.total_rotation = 0.0
        self.target_rotation = 720.0 #spin around twice
    
    def update(self):
          """
        Update the cumulative rotation using the current IMU yaw.

        Returns:
            True when the target rotation is reached, otherwise False.
        """
        
        #get current yaw
        orientation = self.sense.get_orientation()
        current_yaw = orientation["yaw"]
        
        #first reading
        if self.previous_yaw is None:
            self.previous_yaw = current_yaw
            return False
        
        #change in yaw since last reading
        delta = current_yaw-self.previous_yaw
        
        #adjust for sign
        if delta > 180:
            delta -= 360
        elif delta < -180:
            delta+=360
            
        #add rotations
        self.total_rotation += abs(delta)
        
        self.previous_yaw = current_yaw
        
        print(
            f"Yaw: {current_yaw:.1f}° | "
            f"Rotation: {self.total_rotation:.1f}°"
        )
        
        #check for 2 rotations
        if self.total_rotation >= self.target_rotation:
            return True
        
        return False
    
    #reset stored data before next search session
    def reset(self):
        self.previous_yaw = None
        self.total_rotation = 0.0

#testing function to search for ball- confirm it works
def search_for_ball():
    search = Search()
    while True:
        finished = search.update()
        if finished:
            print("Search complete!")
            return
        time.sleep(0.05)