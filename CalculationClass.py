import numpy as np
import math as math
import itertools as it

h_t = np.array([216, 414, 612, 801, 990, 1170])  # array of know height at a given time interval (Ti)
e_t = np.array([37.3, 45.8, 51.3, 52.3, 51.1, 48.1])  # elevation angle in degrees measurements taken a Ti
az_t = np.array([88.5, 78.1, 64.3, 55.8, 57.0, 60.9])  # azimuth angle as read from north. will be converted to east
time_interval = 60 # the time interval a reading is taken in seconds


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
    direction_i = np.empty_like(delta_x_of_t_time)
    x_of_t_time_signs = np.sign(delta_x_of_t_time)
    y_of_t_time_signs = np.sign(delta_x_of_t_time)
    print("delta_x_of_t", delta_x_of_t_time)
    print("delta_y_of_t", delta_y_of_t_time)
    print("x_of_t_signs", x_of_t_time_signs)
    print("y_of_t_sings", y_of_t_time_signs)
    non_transformed_direction = np.arctan(delta_y_of_t_time / delta_x_of_t_time)
    non_transformed_direction = np.rad2deg(non_transformed_direction) # the result must be transformed from rad to deg
    print("non_transformed_direction", non_transformed_direction)
    if np.any(x_of_t_time_signs) and np.any(y_of_t_time_signs) == 1: # I don't think np.any is correct
        #  for checking element sign individually
        direction_i = 270 - non_transformed_direction
    return direction_i


# changes the angle from computer east to north
def azimuth_east_to_north():
    pass


def test_funtion(d_y_t, d_x_t):# notice the
    # angle = np.empty_like(d_y_t)
    angle = np.arctan(d_y_t / d_x_t)
    angle = np.rad2deg(angle)
    print("angle after arctan in radians", angle)
    return angle
#calculate_distance(ht, et)
#azimuth_north_to_east(azt)




