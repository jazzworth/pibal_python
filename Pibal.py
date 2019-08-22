import math
import numpy as np


class Pibal:
    def __init__(self, pibal_radius,  ):
    # pressure of air estimated but can be calculated
    p_air = 1.29
    # pressure of helium
    p_he = .179
    # gravity in m/s
    gravity = 9.81
    # drag coefficient average .50
    drag_coefficient = .50