from algorithm import rrt_sid

# Algorithm
algo_options = {
    "rrt_sid": rrt_sid
}

algo = "rrt_sid"

iters = 1000
start_node = (255, 200)
end_node = (500, 150)
initial_generate_dist = 50  # Sometimes, increasing leads to reaching farther areas


# Render
map_bw_reverse = False  # Reverse black and white in obstacle readings
display_end = False  # Display final image when program finished

# Debug
debug = True  # Run while program running
debug_time = 0  # Time to wait after every frame displayed in seconds
debug_iters = 500  # Display frame ever 'debug_iters' iters

# Map Path
map_path = 'maps/img_3.png'

# Output image directory
out_path = './out/test.png'


