import random
import time

import pygame

import utils.occupancy_grid


def draw_obstacles(obstacles):
    """
    Draw obstacles on the Pygame window.

    :param obstacles: List of obstacles to draw.
    :type obstacles: List[List[int, int, int]]
    """
    for obstacle in obstacles:
        pygame.draw.circle(screen, (0, 0, 255), obstacle[:2], obstacle[2])


def draw_waypoints(waypoints):
    """
    Draw waypoints on the Pygame window.

    :param waypoints: List of waypoints to draw.
    :type waypoints: List[List[int, int]]
    """
    for waypoint in waypoints:
        pygame.draw.circle(screen, (255, 0, 0), [waypoint.x, waypoint.y], 2)


def draw_path(path):
    """
    Draw a path on the Pygame window.

    :param path: List of coordinates representing the path to draw.
    :type path: List[Tuple[int, int]]
    """
    for point in path:
        pygame.draw.circle(screen, (255, 255, 255), point[:2], 5)


# --- MAIN --- #
class Waypoint:
    def __init__(self, x, y, target_waypoint):
        self.x = x + random.randrange(-5, 5)
        self.y = y + random.randrange(-5, 5)
        self.v = [0, 0]
        self.f = [0, 0]
        self.target = target_waypoint

        self.m = 1

    def update(self, force, dt):
        """
        Update values given a force vector.

        :param force: Force vector to update the values with.
        :type force: List[float, float]

        :param dt: Time step.
        :type dt: float
        """

        # Update velocity
        self.v[0] += force[0] / self.m * dt
        self.v[1] += force[1] / self.m * dt

        # Update position
        self.x += self.v[0] * dt
        self.y += self.v[1] * dt

        # Update force
        self.f = force


def obstacle_force(waypoint: Waypoint, obstacles):
    """
    Calculate the force exerted by obstacles repelling waypoints.

    :param waypoint: Point to calculate the force on.
    :type waypoint: Waypoint

    :param obstacles: List of obstacles.
    :type obstacles: List[List[int, int, int]]
    """

    force = [0, 0]

    for obstacle in obstacles:
        repulsive_force = 1 / ((waypoint.x - obstacle[0]) ** 2 + (waypoint.y - obstacle[1]) ** 2)
        force[0] += repulsive_force * (waypoint.x - obstacle[0])
        force[1] += repulsive_force * (waypoint.y - obstacle[1])

    return force


# --- PYGAME SETUP --- #
pygame.init()

# center_x, center_y, radius
obstacles = [
    [100, 100, 10],
    [200, 200, 10],
    [300, 300, 10],
]

start_point = [0, 0]
end_point = [500, 500]

# Form waypoints at regular intervals from start to end
waypoints = [Waypoint(x[0], x[1], end_point) for x in utils.occupancy_grid.waypoints_gen([
    start_point, end_point], 20)]

# --- PYGAME SETUP --- #

pygame.init()

# Open 800x800 Pygame window
screen = pygame.display.set_mode((800, 800))


def draw():
    """
    Draw obstacles, waypoints, and path on the Pygame window.
    """
    # Draw obstacles as circles
    draw_obstacles(obstacles)

    # Draw waypoints as circles
    draw_waypoints(waypoints)

    # Draw start and end points as circles
    draw_path([start_point, end_point])

    # Update the screen
    pygame.display.flip()


for i in range(1000):
    screen.fill((0, 0, 0))
    draw()
    for waypoint in waypoints:
        force = obstacle_force(waypoint, obstacles)
        waypoint.update(force, 0.1)

input('Press Enter to continue...')
