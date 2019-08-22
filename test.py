import math
import numpy as np


def ascent_rate_calc():
    # pressure of air estimated but can be calculated
    p_air = 1.29
    # pressure of helium
    p_he = .179
    # gravity in m/s
    gravity = 9.81
    # drag coefficient average .50
    drag_coefficient = .50
    # captures pibal dimater calc radius and converts to meters
    pibal_diameter = float(input('What is the diamter of the pibal (in inches)? '))
    pibal_radius = (pibal_diameter * .0254) / 2
    print('radius of the pibal is: ' + str(pibal_radius))
    # calcualtes the horizontal velocity in feet/min
    pibal_ascent_rate = math.sqrt((8.0*(gravity)*(pibal_radius)/(3.0*(drag_coefficient)))*(p_air - p_he)/p_air) * 196.85
    print('the pibal ascends at: ' + str(pibal_ascent_rate) + ' feet per minute')
    return pibal_ascent_rate


def time_interval():
    time_interval = 0
    while time_interval not in (30, 60):
        time_interval = float(input('How many seconds between readings (enter 30 or 60?) '))
        if time_interval not in (30, 60):
            print('***PLEASE ENTER 30 OR 60***')
        else:
            return time_interval
      

def number_of_intervals():
    num_of_intervals = int(input('How many readings do you want to take? '))
    return num_of_intervals


def calculate_height_at_intervals(num_of_intervals, pibal_ascent_rate, time_interval):
    lst = []
    total_height = 0
    if time_interval == 30:
        for n in range(num_of_intervals):
            total_height += pibal_ascent_rate / 2
            lst.append(total_height)
    else:
        for n in range(num_of_intervals):
            total_height += pibal_ascent_rate
            lst.append(total_height)
    h_t = np.array(lst)
    print(lst)
    print(h_t)         
    return h_t
    

# capture user input for angle and azimuth
class ElevationAndAngle:
    def __init__(self):
        self.e_t = []
        self.az_t = []
        self.lst_angle = []
        self.lst_azimuth = []
        

    # def elev_and_angle(e_t, az_t):
    def capture_elevation_and_azimuth(number_of_intervals):            
        for n in range(number_of_intervals):
            self.lst_angle_input = float(input("enter elevation angle (vertical angle in degrees): \n" ))
            self.lst_angle.append(self.lst_angle_input)
            self.lst_azimuth_input = float(input("enter azimuth (horizontal in degrees: \n" ))
            self.lst_azimuth.append(self.lst_azimuth_input)
            self.e_t = np.array(self.lst_angle)
            self.az_t = np.array(self.lst_azimuth)


def create_elevation_and_angle_object():
    return ElevationAndAngle()
    
'''def capture_elevation_and_angle(number_of_intervals):
    lst_angle = []
    lst_azimuth = []
    for i in range(number_of_intervals):
        lst_angle_input = float(input("enter elevation angle (vertical angle in degrees): \n" ))
        lst_angle.append(lst_angle_input)
        lst_azimuth_input = float(input("enter azimuth (horizontal in degrees: \n" ))
        lst_azimuth.append(lst_azimuth_input)
        e_t = np.array(lst_angle)
        az_t = np.array(lst_azimuth)
    return e_t, az_t'''


def main():
    ascent_rate = ascent_rate_calc()
    time_int = time_interval()
    interval_number = number_of_intervals()
    height = calculate_height_at_intervals(interval_number, ascent_rate, time_int)
    az_et_object = create_elevation_and_angle_object()
    get_e_t_az = az_et_object.capture_elevation_and_azimuth()
    e_t = az_et_object.e_t
    az_t = az_et_object.az_t
    print(e_t)
    print(az_t)
    

if __name__ == "__main__":
    main()
