import numpy as np

ht = np.array([216, 414, 612, 801, 990, 1170])  # array of know height at a given time interval (Ti)
et = np.array([37.3, 45.8, 51.3, 52.3, 51.1, 48.1])  # elevation angle in degrees measurements taken a Ti


def calculate_distance(height, elevation_angle):
    etan = np.tan(elevation_angle * np.pi / 180)  # tangent of all values in et
    # since arrays are implicit in numpy, this populates the distance array with out an iterating for loop
    distance = height / etan
    return distance


def test(x, y):
    a = x + y
    return a




