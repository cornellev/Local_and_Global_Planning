import math

from type_hints.types import Node

# Algorithm - rrt_star or rrt_sid
algo: str = "rrt_sid"


# Vehicle
max_turning_angle: float = math.pi / 2.5  # In radians
vehicle_length: float = 18  # In pixels
vehicle_width: float = 8  # In pixels

iters: int = 1500
start_node: Node = (5, 5)
end_node: Node = (340, 340)
initial_generate_dist: int = 50  # Sometimes, increasing leads to reaching farther areas
padding: int = int(vehicle_width / 2) + 2  # Padding around obstacles

# Render
map_bw_reverse: bool = False  # Reverse black and white in obstacle readings
display_end: bool = False  # Display final image when program finished

# Debug
debug_global: bool = False  # Run while program running
debug_local: bool = True  # Run while program running
debug_time: float = 0  # Time to wait after every frame displayed in seconds
debug_iters: int = 50  # Display frame ever 'debug_iters' iters

# Map Path
map_path = 'maps/img_6.png'

# Output image directory
out_path = 'global_sim/out/test.png'


