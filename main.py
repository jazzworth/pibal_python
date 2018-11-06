import numpy as np
import CalculationClass
import matplotlib.pyplot as plt


# calls the distance function using arguments from another file. Arguments may be generated from another funtion or DB
dt = np.around(CalculationClass.calculate_distance(CalculationClass.h_t, CalculationClass.e_t), decimals=0)
print("d_t = ", dt)

x_t = np.around(CalculationClass.polar_to_rectangular_coordinate_transformation_x(dt, CalculationClass.az_t), decimals=0)
print("x_t are", x_t)

y_t = np.around(CalculationClass.polar_to_rectangular_coordinate_transformation_y(dt, CalculationClass.az_t), decimals=0)
print("y_t are:", y_t)

delta_x_t = CalculationClass.find_delta_x(x_t)
print("delta_x_t are:", delta_x_t)

delta_y_t = CalculationClass.find_delta_y(y_t)
print("delta_y_t are:", delta_y_t)

mean_wind_speed = np.around(CalculationClass.mean_wind_speed(delta_x_t, delta_y_t, CalculationClass.time_interval), decimals=1)
print("these are the mean wind speeds:", mean_wind_speed)

pibal_direction_t = np.around(CalculationClass.rectangular_to_polar_coordinate_transformation(delta_y_t, delta_x_t))
print("the pibal direction is:", pibal_direction_t)

non_transformed_direction_polar_plot = np.around(CalculationClass.non_transformed_direction_for_plot(delta_y_t, delta_x_t))
print('Non transfomed vaues in radians:', non_transformed_direction_polar_plot)

# test = CalculationClass.test_funtion(delta_y_t, delta_x_t)
# print("test of x calc = ", test)

plot = CalculationClass.polar_plot(non_transformed_direction_polar_plot, mean_wind_speed)