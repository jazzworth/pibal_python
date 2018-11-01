import numpy as np
import CalculationClass


#calls the distance function using arguments from another file. Arguments may be generated from another funtion or DB
dt = np.around(CalculationClass.calculate_distance(CalculationClass.h_t, CalculationClass.e_t), decimals=0)
print("d_t = ", dt)
test = CalculationClass.test_funtion()
print("test of x calc = ", test)
x_t = np.around(CalculationClass.polar_to_rectangular_coordinate_transformation_x(dt, CalculationClass.az_t), decimals=0)
print(x_t)
y_t = np.around(CalculationClass.polar_to_rectangular_coordinate_transformation_y(dt, CalculationClass.az_t), decimals=0)
print(y_t)

