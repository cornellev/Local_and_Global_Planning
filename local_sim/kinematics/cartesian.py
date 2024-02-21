from local_sim.kinematics.kinematics import Kinematics


class CartesianKinematics(Kinematics):
    @staticmethod
    def get_constraints(state, u, dT, N):
        """
        Returns a list of constraints given the state, input, and time steps
        """
        constraints = []
        for i in range(N - 1):
            constraints.append(state[2, i + 1] == state[2, i] + u[0, i] * dT)
            constraints.append(state[3, i + 1] == state[3, i] + u[1, i] * dT)
            constraints.append(state[0, i + 1] == state[0, i] + state[2, i] * dT)
            constraints.append(state[1, i + 1] == state[1, i] + state[3, i] * dT)

        return constraints
