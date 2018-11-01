import numpy as np
import math as math

h_t = np.array([216, 414, 612, 801, 990, 1170])  # array of know height at a given time interval (Ti)
e_t = np.array([37.3, 45.8, 51.3, 52.3, 51.1, 48.1])  # elevation angle in degrees measurements taken a Ti
az_t = np.array([88.5, 78.1, 64.3, 55.8, 57.0, 60.9])  # azimuth angle as read from north. will be converted to east


# this calculates the distance from the theodolite to be used
def calculate_distance(height, elevation_angle):
    etan = np.tan(elevation_angle * np.pi / 180)  # tangent of all values in et
    #distance = np.empty_like(height)
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


# requires subtracting the next x_t in the array
def find_delta_x():
    pass


# requries subtracting the next x_t in the array
def find_delta_y():
    pass


# this is likely to have the (x, y) and will be transformed to polar in the next function
def mean_wind_speed():
    pass


# the result of the mean wind speed in (x, y) needs transformed to (point, angle}
def rectangular_to_polar_coordinate_transformation():
    pass


# changes the angle from computer east to north
def azimuth_east_to_north():
    pass


def test_funtion():
    x = 284 * math.sin(math.radians(88.5))
    return x

#calculate_distance(ht, et)
#azimuth_north_to_east(azt)




