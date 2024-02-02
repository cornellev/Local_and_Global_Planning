import numpy as np
from scipy.interpolate import CubicSpline
# import matplotlib.pyplot as plt


def smooth_path(start: (int, int), end: (int, int), waypoints: [(int, int)]):
    print(start, end, waypoints)
    start = np.array(start)
    end = np.array(end)
    waypoints = np.array(waypoints)
    # Concatenate start, end, and waypoints
    waypoints = np.vstack([start, waypoints, end])

    # Create parameter values for each point
    t = np.arange(len(waypoints))

    # Create a cubic spline interpolation
    cs = CubicSpline(t, waypoints, bc_type='clamped')

    # Generate a finer parameterization for a smoother curve
    t_smooth = np.linspace(0, len(waypoints) - 1, 1000)

    # Evaluate the cubic spline at the smoother parameterization
    smoothed_path = cs(t_smooth)

    return smoothed_path


def convert_to_coordinates(smoothed_path):
    # Extract x and y coordinates from the smoothed path
    x_coordinates = smoothed_path[:, 0]
    y_coordinates = smoothed_path[:, 1]

    # Combine x and y coordinates into a list of coordinate pairs
    coordinates = list(zip(x_coordinates, y_coordinates))

    return coordinates

# Example usage:
# start_point = np.array([0, 0])
# end_point = np.array([20, 10])
# waypoints = np.array([[2, 5], [5, 7], [15, 1]])
#
# smoothed_path = smooth_path(start_point, end_point, waypoints)
#
# # Plot the original waypoints and the smoothed path
# plt.plot(waypoints[:, 0], waypoints[:, 1], 'ro', label='Waypoints')
# plt.plot(smoothed_path[:, 0], smoothed_path[:, 1], 'b-', label='Smoothed Path')
# plt.scatter([start_point[0], end_point[0]], [start_point[1], end_point[1]], c='g', marker='s',
#             label='Start/End Points')
#
# plt.legend()
# plt.xlabel('X-coordinate')
# plt.ylabel('Y-coordinate')
# plt.title('Smoothed Path using Cubic Splines')
# plt.grid(True)
# plt.show()
