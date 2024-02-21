from global_sim.algorithm import rrt_sid, rrt_star
from type_hints.types import Node

# Algorithm - rrt_star or rrt_sid
algo: str = "rrt_sid"

iters: int = 500
start_node: Node = (5, 5)
end_node: Node = (340, 340)
initial_generate_dist: int = 50  # Sometimes, increasing leads to reaching farther areas
padding: int = 4

# Render
map_bw_reverse: bool = False  # Reverse black and white in obstacle readings
display_end: bool = False  # Display final image when program finished

# Debug
debug: bool = True  # Run while program running
debug_time: float = 0  # Time to wait after every frame displayed in seconds
debug_iters: int = 50  # Display frame ever 'debug_iters' iters

# Map Path
map_path = 'maps/img_3.png'

# Output image directory
out_path = 'global_sim/out/test.png'


