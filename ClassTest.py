import math
import numpy as np


class Pibal:
    def __init__(self):
        self.radius = 0.0
        self.pibal_ascent_rate = 0.0

    def get_radius_of_pibal(self):
        self.radius = (float(input("what is the diameter of the pibal? "))) / 2 *.0254
        print('The radius is ' + str(self.radius) + ' meters.')


def main():
    pibal_object = Pibal()
    pibal_object_radius = pibal_object.get_radius_of_pibal()

if __name__ == "__main__":
    main()
    
