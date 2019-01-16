from matplotlib import pyplot as plt

class Vehicle:
    def __init__(self):
        """
        Creates new vehicle at (0,0) with a heading pointed East.
        """
        self.x       = 0 # meters
        self.y       = 0
        self.heading = "E" # Can be "N", "S", "E", or "W"
        self.history = []
        
    # Done- Implement this function 
    def drive_forward(self, displacement):
        """
        Updates x and y coordinates of vehicle based on 
        heading and appends previous (x,y) position to
        history.
        """
        
        # this line appends the current (x,y) coordinates
        # to the vehicle's history. Useful for plotting 
        # the vehicle's trajectory. You shouldn't need to
        # change this line.
        self.history.append((self.x, self.y))
        
        # vehicle currently pointing east...
        if   self.heading == "E":
            self.x += displacement
        
        # north
        elif self.heading == "N":
            self.y += displacement
        
        # west
        elif self.heading == "W":
            self.x -= displacement
        
        # south
        else:
            self.y += displacement
        
    def turn(self, direction):
        if direction == "L":
            self.turn_left()
        elif direction == "R":
            self.turn_right()
        else:
            print("Error. Direction must be 'L' or 'R'")
            return
        
    def turn_left(self):
        """
        Updates heading (for a left turn) based on current heading
        """
        next_heading = {
            "N" : "W",
            "W" : "S",
            "S" : "E",
            "E" : "N",
        }
        self.heading = next_heading[self.heading]
        
    
    # TODO-2 - implement this function
    def turn_right(self):
        pass
    
    def show_trajectory(self):
        """
        Creates a scatter plot of vehicle's trajectory.
        """
        X = [p[0] for p in self.history]
        Y = [p[1] for p in self.history]
        
        X.append(self.x)
        Y.append(self.y)
        
        plt.scatter(X,Y)
        plt.plot(X,Y)
        plt.show()