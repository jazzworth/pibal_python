import math
import numpy as np

class Pibal():
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

class Interval():
    def __init__(self):
        self.time_interval = 0
        self.number_of_intervals = 0
        self.max_altitude = 0
        

    # this will ask the user how many seconds between readings and how many readings
    def get_time_interval(self):
        while self.time_interval not in (30, 60):
            self.time_interval = float(input('How many seconds between readings (enter 30 or 60?) '))
            if self.time_interval not in (30, 60):
                print('***PLEASE ENTER 30 OR 60***')
            else:
                return self.time_interval


    def get_number_of_intervals(self):
        self.number_of_intervals = int(input('How many readings do you want to take? '))
        return self.number_of_intervals
    

    def interval_timer(self):
        pass

          
    def max_height_of_readings(self, pibal_ascent_rate, max_altitude):
        pass

class DataSetArrays():
    def __init__(self, num_of_intervals, pibal_ascent_rate, time_interval):
        self.num_of_intervals = num_of_intervals
        self.pibal_ascent_rate = pibal_ascent_rate
        self.time_interval = time_interval
        """sub classes should be used for inheritance
        self.lst_height = []
        self.lst_angle = []
        self.lst_azimuth = []
        self.h_t = np.array(self.lst_height)
        self.e_t = np.array(self.lst_angle)
        self.az_t = np.array(self.lst_azimuth)
        """
    #change this to an inherited subclass
    def calcualte_height_at_intervals(self):
        total_height = 0
        lst_height = []
        if self.time_interval == 30:
            for n in range(self.num_of_intervals):
                total_height += self.pibal_ascent_rate / 2
                lst_height.append(total_height)
        else:
            for n in range(self.num_of_intervals):
                total_height += self.pibal_ascent_rate
                lst_height.append(total_height)
        h_t = np.array(lst_height)
        print(lst_height)
        print(h_t)
        return h_t
                    


def main():
    pibal_object = Pibal()
    pibal_object.set_radius_of_pibal()
    pibal_object.set_ascent_rate()
    interval_object = Interval()
    interval_object.get_time_interval()
    interval_object.get_number_of_intervals()
    dataset_array_object = DataSetArrays(interval_object.number_of_intervals, pibal_object.pibal_ascent_rate, interval_object.time_interval)
    dataset_array_object.calcualte_height_at_intervals()
    

if __name__ == "__main__":
     main()   
