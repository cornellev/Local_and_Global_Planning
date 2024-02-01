import heapq

def astar(start, goal, nodes, distance_function):
    def heuristic(node, goal):
        # This is the heuristic function, estimating the cost from the current node to the goal
        return distance_function(node, goal)

    def neighbors(node):
        # This function returns the neighbors of a given node
        x, y = node
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]  # Assuming 4-connected neighbors

    open_set = [(heuristic(start, goal), start, 0)]
    closed_set = set()
    came_from = {}

    while open_set:
        # Get the node with the lowest f value
        current_f, current_node, g = heapq.heappop(open_set)

        # Check if the current node is the goal
        if current_node == goal:
            return reconstruct_path(came_from, start, goal)

        # Add the current node to the closed set
        closed_set.add(current_node)

        # Explore neighbors
        for neighbor in neighbors(current_node):
            if neighbor in closed_set:
                continue

            # Calculate tentative g value
            tentative_g = g + distance_function(current_node, neighbor)

            # Check if the neighbor is already in the open set
            if not any(neighbor == node[1] for node in open_set) or tentative_g < g:
                # Update or add the neighbor in the open set
                heapq.heappush(open_set, (tentative_g + heuristic(neighbor, goal), neighbor, tentative_g))
                came_from[neighbor] = current_node

    # If the open set is empty and the goal is not reached, return None
    return None

def reconstruct_path(came_from, start, goal):
    # Reconstruct the path from the goal to the start
    current_node = goal
    path = [current_node]
    while current_node != start:
        current_node = came_from[current_node]
        path.insert(0, current_node)
    return path