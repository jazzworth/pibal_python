import math


class Pibal:
    def __init__(self):
        self.radius = 0.0
        self.pibal_ascent_rate = 0.0
        # pressure of air estimated but can be calculated at a later date
        self.p_air = 1.29
        # pressure of helium
        self.p_he = .179
        # gravity in m/s
        self.gravity = 9.81
        # drag coefficient average .50
        self.drag_coefficient = .50


    def set_radius_of_pibal(self):
        self.radius = (float(input("what is the diameter of the pibal? "))) / 2 *.0254
        print('The radius is ' + str(self.radius) + ' meters.')
        return self.radius

    
    def set_ascent_rate(self):
        # calcualtes the horizontal velocity in feet/min
        self.pibal_ascent_rate = math.sqrt((8.0*(self.gravity)*(self.radius)/(3.0*(self.drag_coefficient)))*(self.p_air - self.p_he)/self.p_air) * 196.85
        print('the pibal ascends at: ' + str(self.pibal_ascent_rate) + ' feet per minute')
        return self.pibal_ascent_rate

class Interval:
    def __init__(self):
        self.time_interval = 0
        self.number_of_intervals = 0
        self.max_altitude = 0


    # this will ask the user how many seconds between readings and how many readings
    def time_interval(self):
        while self.time_interval not in (30, 60):
            time_interval = float(input('How many seconds between readings (enter 30 or 60?) '))
            if self.time_interval not in (30, 60):
                print('***PLEASE ENTER 30 OR 60***')
            else:
                return self.time_interval



def main():
    pibal_object = Pibal()
    pibal_object.set_radius_of_pibal()
    pibal_object.set_ascent_rate()
    

if __name__ == "__main__":
     main()   
