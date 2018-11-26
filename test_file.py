import numpy as np
import pandas as pd

#
h_t = np.array([216., 414., 612., 801., 990., 1170.])  # array of know height at a given time interval (Ti) This will be
# calculated with a known formula and determine the number of columns in the pd.DataFrame
e_t = np.array([37.3, 45.8, 51.3, 52.3, 51.1, 48.1])  # elevation angle in degrees measurements taken a Ti
az_t = np.array([88.5, 78.1, 64.3, 55.8, 57.0, 60.9])  # azimuth angle as read from north. will be converted to east
time_int = np.array([60., 120., 180., 240., 300., 360.]) # the time interval a reading is taken in seconds
total_observation_time = 6 # total time the pibal will be observed


def create_data_frame(time_interval, height, elevation_angle, azimuth_angle):
    # a dict or np arrays of collected data
    data = {'Time Interval': time_interval, 'Height': height, 'Elevation Angle': elevation_angle, 'Azimuth_Angle': azimuth_angle}
    # using the data to populate the DataFrame
    all_data = pd.DataFrame.from_dict(data)
    return all_data

def np_where_funtion():
    direction = np.array([5, 180, 400])
    direction = np.where(direction > 360, direction - 360, 270 - direction)
    # direction = np.where(direction < 360, direction, direction - 360)
    return direction

new_df = create_data_frame(time_int, h_t, e_t, az_t)
print(new_df)

new_direction = np_where_funtion()
print(new_direction)

# dict_array = {'1st set': array1, '2nd set': array2}

# test_df = pd.DataFrame(dict_array)
# print(test_df)

