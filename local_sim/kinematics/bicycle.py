from local_sim.kinematics.kinematics import Kinematics
import numpy as np


class BicycleKinematics(Kinematics):
    def __init__(self, initial_state):
        self.state = initial_state

    def get_constraints(self, inputs, dT, N):
        """
        inputs: [velocity, steering angle]
        state: [x, y, 𝜃, 𝛿] (𝜃 is the heading angle, 𝛿 is the steering angle)
        """

        constraints = []
        for i in range(N - 1):
            constraints.append(self.state[0, i + 1] == self.state[0, i] + self.state[2, i] * np.cos(self.state[3, i]) * dT)
            constraints.append(self.state[1, i + 1] == self.state[1, i] + self.state[2, i] * np.sin(self.state[3, i]) * dT)
            constraints.append(self.state[2, i + 1] == self.state[2, i] + inputs[0, i] * dT)
            constraints.append(self.state[3, i + 1] == self.state[3, i] + inputs[1, i] * dT)
        return constraints
