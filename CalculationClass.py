import numpy as np
import pandas as pd
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 20)
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import math as math
import itertools as it

h_t = np.array([216, 414, 612, 801, 990, 1170])  # array of know height at a given time interval (Ti)
e_t = np.array([37.3, 45.8, 51.3, 52.3, 51.1, 48.1])  # elevation angle in degrees measurements taken a Ti
az_t = np.array([88.5, 78.1, 64.3, 55.8, 57.0, 60.9])  # azimuth angle as read from north. will be converted to east
time_interval = 60 # the time interval a reading is taken in seconds
num_of_intervals = 0 #how many time intervals the user wants to track. This could be derived from time_interval and a max_altitude
"""Need to calculate the lift based on the time interval given by the user (60 sec max).  Maybe only use 30 and 60 sec
as options.  can ask user the max altitude to track and derive the num_of_intervals based on the ascent rate calculation
(a max of 5000ft or similar).  Thgis will then set the height array and thus the shape of the arrays and the 
resulting data frame.  Will create skeleton function"""

#this will take the time interval, and max altitude and output the height(h_t) at intervals to the max. row count going forward
def calculate_height_at_intervals():
    pass

def capture_elevation_and_azimuth():
    pass

#this will take the time interval and start a timer for the user.  May be an advanced function.
def interval_timer():
    pass

# this calculates the distance from the theodolite to be used
def calculate_distance(height, elevation_angle):
    etan = np.tan(elevation_angle * np.pi / 180)  # tangent of all values in et
    # distance = np.empty_like(height)
    # since arrays are implicit in numpy, this populates the distance array with out an iterating for loop
    distance = height / etan
   # print(distance)
    return distance


# Finds the length of side x.  Requires changing degrees to radians to use the function
def polar_to_rectangular_coordinate_transformation_x(distance_t, azimuth_t):
    x = distance_t * np.sin(np.deg2rad(azimuth_t))
    return x


# finds the length of side y  Requires changing degrees to radians to use the function
def polar_to_rectangular_coordinate_transformation_y(distance_t, azimuth_t):
    y = distance_t * np.cos(np.deg2rad(azimuth_t))
    return y


# requires subtracting the next x_t in the array have to initialize as the x_t array and then
# exclude the 1st element [1:]
def find_delta_x(x_of_t_time):
    delta_x_t = np.array(x_of_t_time)
    delta_x_t[1:] = [z - w for w, z in zip(delta_x_t, delta_x_t[1:])]
    return delta_x_t


# requries subtracting the next x_t in the array
def find_delta_y(y_of_t_time):
    delta_y_t = np.array(y_of_t_time)
    delta_y_t[1:] = [z - w for w, z in zip(delta_y_t, delta_y_t[1:])]
    return delta_y_t


# this is likely to have the (x, y) and will be transformed to polar in the next function
def mean_wind_speed(x_of_t_time, y_of_t_time, time_interval_of_readings):
    velocity_i = (x_of_t_time ** 2 + y_of_t_time ** 2)**.5 / time_interval_of_readings
    return velocity_i


# the result of the mean wind speed in (x, y) needs transformed to (point, angle}
def rectangular_to_polar_coordinate_transformation(delta_y_of_t_time, delta_x_of_t_time):
    non_transformed_direction = np.arctan2(delta_y_of_t_time , delta_x_of_t_time) * 180 / np.pi
    non_transformed_direction = np.where(non_transformed_direction > 360, 360 - non_transformed_direction, 270 - non_transformed_direction)
    #print("non_transformed_direction", non_transformed_direction)
    return non_transformed_direction


def non_transformed_direction_for_plot(delta_y_of_t_time, delta_x_of_t_time):
    non_transformed_direction = np.arctan(delta_y_of_t_time / delta_x_of_t_time)
    #print('non-transformed for plot:', non_transformed_direction)
    return non_transformed_direction


def create_data_frame(input_time_interval, height, elevation_angle, azimuth_angle, x, y, delta_x, delta_y, direction, speed):
    # a dict or np arrays of collected data
    data = {'Time Interval': input_time_interval, 'Height': height, 'Elevation Angle': elevation_angle, 'Azimuth_Angle': azimuth_angle,
            'x': x, 'y': y, 'Delta X': delta_x, 'Delta Y': delta_y, 'Direction (deg-from)': direction, 'Speed': speed}
    # using the data to populate the DataFrame
    all_data = pd.DataFrame.from_dict(data)
    return all_data


def polar_plot(non_transformed_direction_t, velocity_i): # https://media.readthedocs.org/pdf/windrose/latest/windrose.pdf
    plt.polar(non_transformed_direction_t, velocity_i) # https://windrose.readthedocs.io/en/latest/
    plt.show()


def test_function(d_y_t, d_x_t):# notice the
    # angle = np.empty_like(d_y_t)
    angle = np.arctan(d_y_t / d_x_t)
    angle = np.rad2deg(angle)
    #print("angle after arctan in radians", angle)
    return angle
#calculate_distance(ht, et)
#azimuth_north_to_east(azt)




