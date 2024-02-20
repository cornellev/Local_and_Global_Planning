import matplotlib.pyplot as plt
import numpy as np
from casadi import casadi


class Obstacle:
    def __init__(self, center_x, center_y, radius):
        self.x = center_x
        self.y = center_y
        self.radius = radius

    def plot(self):
        circle = plt.Circle((self.x, self.y), self.radius, color='r', fill=False)

        plt.gca().add_patch(circle)
