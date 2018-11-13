import numpy as np



def rectangular_to_polar_coordinate_transformation(delta_y_of_t_time, delta_x_of_t_time):
    angle = np.arctan2(delta_y_of_t_time, delta_x_of_t_time)  # array of angles
    angle = np.rad2deg(angle)
    print("orig angle", angle)

    # Step through the array to make adjustments
    for index, xp in np.ndenumerate(delta_x_of_t_time):
        x = delta_x_of_t_time[index]
        y = delta_y_of_t_time[index]

        if x < 0 and y < 0:
            angle[index] -= 20
        elif x < 0 and y > 0:
            angle[index] -= 10
        elif x > 0 and y < 0:
            angle[index] += 10
        elif x > 0 and y > 0:
            angle[index] += 20

    return (angle)


if __name__ == "__main__":
    x = np.array([-1, -1, 1, 1])
    y = np.array([-1, 1, -1, 1])

    angle = rectangular_to_polar_coordinate_transformation(y, x)

    print("mod angle", angle)