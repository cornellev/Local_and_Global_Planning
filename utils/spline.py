import numpy as np
from scipy.interpolate import CubicSpline

from type_hints.types import Node, NodeList


def smooth_path(start: Node, end: Node, waypoints: NodeList) -> np.ndarray:
    """
    Generate a smooth path between the given start and end points, passing through waypoints.

    :param start: The starting point of the path.
    :type start: Node

    :param end: The ending point of the path.
    :type end: Node

    :param waypoints: List of intermediate points to pass through.
    :type waypoints: NodeList

    :return: Smoothed path as a NumPy array, representing the coordinates of points along the path.
    :rtype: np.ndarray

    The function uses cubic spline interpolation to create a smooth curve connecting the provided
    points and waypoints. The resulting path is parameterized to ensure a smoother transition
    between the specified locations.
    """

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


def convert_to_coordinates(smoothed_path: np.ndarray) -> NodeList:
    """
    Extract x and y coordinates from a smoothed path and combine them into a list of coordinate
    pairs.

    :param smoothed_path: Smoothed path as a NumPy array, representing the coordinates of points along the path.
    :type smoothed_path: np.ndarray

    :return: List of coordinate pairs (x, y).
    :rtype: List[Tuple[float, float]]
    """

    # Extract x and y coordinates from the smoothed path
    x_coordinates = smoothed_path[:, 0]
    y_coordinates = smoothed_path[:, 1]

    # Combine x and y coordinates into a list of coordinate pairs
    coordinates = list(zip(x_coordinates, y_coordinates))

    return coordinates
