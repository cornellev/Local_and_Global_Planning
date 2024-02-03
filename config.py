from algorithm import rrt_sid
from type_hints.types import Node

# Algorithm
algo_options = {
    "rrt_sid": rrt_sid
}

algo: str = "rrt_sid"

iters: int = 1000
start_node: Node = (100, 300)
end_node: Node = (700, 300)
initial_generate_dist: int = 50  # Sometimes, increasing leads to reaching farther areas


# Render
map_bw_reverse: bool = False  # Reverse black and white in obstacle readings
display_end: bool = False  # Display final image when program finished

# Debug
debug: bool = True  # Run while program running
debug_time: float = .3  # Time to wait after every frame displayed in seconds
debug_iters: int = 50  # Display frame ever 'debug_iters' iters

# Map Path
map_path = 'maps/img_3.png'

# Output image directory
out_path = './out/test.png'


